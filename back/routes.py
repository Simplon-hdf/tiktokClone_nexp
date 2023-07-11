from fastapi import APIRouter
from controlers import user_controller, video_controller, commentaire_controller

user_router = APIRouter()
video_router = APIRouter()
commentaire_router = APIRouter()


# Utilisateurs
@user_router.post('/users/login')
#@user_router.post('/users/signup')
@user_router.put('/users/update')
@user_router.delete('/users/delete')

@user_router.get('/users')
def get_users():
    return user_controller.get_users()

# Vidéos
@video_router.put('/videos/update')
@video_router.delete('/videos/delete')
@video_router.get('/videos')

# Commentaires
@commentaire_router.put('/commentaires/update')
@commentaire_router.delete('/commentaires/delete')
@commentaire_router.get('/commentaires')

