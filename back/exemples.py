from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurez la base de données
SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Définissez le modèle de données pour le compte utilisateur
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)


# Créez la table dans la base de données
Base.metadata.create_all(bind=engine)


# Modèle pour la création d'un utilisateur
class CreateUserRequest(BaseModel):
    username: str
    password: str


app = FastAPI()


# Créer un compte utilisateur
@app.post("/users")
def create_user(user: CreateUserRequest):
    db = SessionLocal()
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Ce nom d'utilisateur existe déjà.")
    db_user = User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "Utilisateur créé avec succès"}


# Authentifier un utilisateur
@app.post("/login")
def login(username: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Nom d'utilisateur ou mot de passe incorrect.")
    return {"message": "Connexion réussie"}


# Récupérer les détails d'un utilisateur
@app.get("/users/{user_id}")
def get_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable.")
    return {"username": user.username}


# Mettre à jour les informations de l'utilisateur
@app.put("/users/{user_id}")
def update_user(user_id: int, user: CreateUserRequest):
    db = SessionLocal()
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user and existing_user.id != user_id:
        raise HTTPException(status_code=400, detail="Ce nom d'utilisateur existe déjà.")
    db_user = db.query(User).get(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable.")
    db_user.username = user.username
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return {"message": "Utilisateur mis à jour avec succès"}


# Supprimer un compte utilisateur
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable.")
    db.delete(user)
    db.commit()
    return {"message": "Utilisateur supprimé avec succès"}


