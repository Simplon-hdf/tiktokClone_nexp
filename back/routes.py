from fastapi import APIRouter
from back.controllers.userController import UserController
from back.controllers.videoController import VideoController
from back.controllers.commentaireController import CommentaireController
from back.controllers.tagController import TagController

user_router = APIRouter()
video_router = APIRouter()
commentaire_router = APIRouter()
tag_router = APIRouter()


# Utilisateurs
@user_router.post('/users/login')
@user_router.post('/users/signup')
@user_router.post('/users/create')
def post_users():
    return user_controller.post_users()
@user_router.get('/users/list')
def get_users():
    return user_controller.get_users()
@user_router.put('/users/update')
def put_users():
    return user_controller.put_users()
@user_router.delete('/users/delete')
def delete_users():
    return user_controller.delete_users()

# Vidéos
@video_router.post('/videos/create')
def post_videos():
    return video_controller.post_videos()
@video_router.get('/videos/list')
def get_videos():
    return video_controller.get_videos()
@video_router.put('/videos/update')
def put_videos():
    return video_controller.put_videos()
@video_router.delete('/videos/delete')
def delete_videos():
    return video_controller.delete_videos()

# Commentaires
@commentaire_router.post('/commentaires/create')
def post_commentaires():
    return commentaire_controller.post_commentaires()
@commentaire_router.get('/commentaires/list')
def get_commentaires():
    return commentaire_controller.get_commentaires()
@commentaire_router.put('/commentaires/update')
def put_commentaires():
    return commentaire_controller.put_commentaires()
@commentaire_router.delete('/commentaires/delete')
def delete_commentaires():
    return commentaire_controller.delete_commentaires()

# Tags
@tag_router.post('/tags/create')
def post_tags():
    return tag_controller.post_tags()
@tag_router.get('/tags/list')
def get_tags():
    return tag_controller.get_tags()
@tag_router.put('/tags/update')
def put_tags():
    return tag_controller.put_tags()
@tag_router.delete('/tags/delete')
def delete_tags():
    return tag_controller.delete_tags()




