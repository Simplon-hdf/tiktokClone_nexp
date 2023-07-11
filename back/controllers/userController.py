from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models import User, engine
from argon2 import PasswordHasher
import jwt
from fastapi import HTTPException

class UserController():

    def __init__(self) -> None:
        self.ph = PasswordHasher()

    def get_users(self):
        with Session(engine) as session:
            users = session.query(User).all()
            return users

    def get_user(self, user_id):
        with Session(engine) as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user is None:
                raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
            return user

    def login(self, email, password):
        with Session(engine) as session:
            user = session.query(User).filter(User.email == email).first()
            if user is None:
                raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
            try:
                if self.ph.verify(user.password, password):
                    # Générer et retourner le JWT pour l'authentification
                    token = self.generate_jwt_token(user.id)
                    return {"access_token": token}
                else:
                    raise HTTPException(status_code=401, detail="Mot de passe incorrect")
            except Exception as e:
                raise HTTPException(status_code=500, detail="Erreur de serveur")

    def create_user(self, data: dict):
        with Session(engine) as session:
            try:
                new_user = User(
                    email=data["email"],
                    pseudo=data["pseudo"],
                    password=self.ph.hash(data["password"])
                )
                session.add(new_user)
                session.commit()
                return new_user
            except SQLAlchemyError as e:
                session.rollback()
                raise HTTPException(status_code=500, detail="Erreur de création de l'utilisateur")

    def generate_jwt_token(self, user_id):
        # Générer et retourner le JWT en utilisant la bibliothèque jwt
        payload = {"user_id": user_id}
        token = jwt.encode(payload, "your_secret_key", algorithm="HS256")
        return token
    