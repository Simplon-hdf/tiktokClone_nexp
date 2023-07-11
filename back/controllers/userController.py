from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models import User, engine
from argon2 import PasswordHasher
import jwt
from fastapi import HTTPException
import os
from dotenv import load_dotenv

class UserController():

    def __init__(self) -> None:
        self.ph = PasswordHasher()
        self.secret_key = os.getenv("SECRET_KEY")
        
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

    def login(self, data: dict):
        with Session(engine) as session:
            email = data["email"]
            password = data["password"]
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

    def generate_jwt_token(self, user_data: dict):
        user_id = user_data["user_id"]
        user_email = user_data["user_email"]
        user_pseudo = user_data["user_pseudo"]

        payload = {
            "user_id": user_id,
            "user_email": user_email,
            "user_pseudo": user_pseudo
        }
        token = jwt.encode(payload, self.secret_key, algorithm="HS256")
        return token

    