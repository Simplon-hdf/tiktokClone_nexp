from sqlalchemy.orm import Session
from sqlalchemy import Select
from models import User, engine
from argon2 import PasswordHasher
import jwt

class UserController():

    def __init__(self) -> None:
        self.ph = PasswordHasher()

    def get_users(self):
        # Code pour récupérer la liste de tous les utilisateurs
        return 'Liste des utilisateurs'

    def get_user(self, user_id):
        # Code pour récupérer un utilisateur à partir de son Id
        return 'Utilisateur avec Id : ()'.format(user_id)

    def login(self):
        pass

    def createUser(self,data:dict):
        with Session(engine) as session:
            newUser = User(
                email = data["email"],
                pseudo = data["pseudo"],
                password = self.ph.hash(data["password"])
            )
            session.add(newUser)
            session.commit()
        