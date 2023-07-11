from sqlalchemy.orm import Session
from sqlalchemy import Select
from models import User, engine

class UserController():

    def get_users():
        # Code pour récupérer la liste de tous les utilisateurs
        return 'Liste des utilisateurs'

    def get_user(user_id):
        # Code pour récupérer un utilisateur à partir de son Id
        return 'Utilisateur avec Id : ()'.format(user_id)

    def login():
        pass