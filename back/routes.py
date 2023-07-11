from fastapi import APIRouter
from back.controllers.userController import user_controller, video_controller, commentaire_controller

user_router = APIRouter()
video_router = APIRouter()
commentaire_router = APIRouter()
tags_router = APIRouter()


# Utilisateurs
@user_router.post('/users/login')
@user_router.post('/users/signup')
@user_router.post('/users/create')
@user_router.get('/users/list')
def get_users():
    return user_controller.get_users()
@user_router.put('/users/update')
@user_router.delete('/users/delete')

# Vidéos
@video_router.post('/videos/create')
@video_router.get('/videos/list')
@video_router.put('/videos/update')
@video_router.delete('/videos/delete')


# Commentaires
@commentaire_router.post('/commentaires/create')
@commentaire_router.get('/commentaires/list')
@commentaire_router.put('/commentaires/update')
@commentaire_router.delete('/commentaires/delete')

# Tags
@tags_router.post('/tags/create')
@tags_router.get('/tags/list')
@tags_router.put('/tags/update')
@tags_router.delete('/tags/delete')



