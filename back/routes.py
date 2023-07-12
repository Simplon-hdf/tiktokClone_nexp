from fastapi import APIRouter, Request, File, Form, UploadFile
from controllers.userController import UserController
from controllers.videoController import VideoController
from controllers.commentController import CommentController
from controllers.tagController import TagController
from pydantic import BaseModel
from typing import Any, Annotated

user_router = APIRouter()
video_router = APIRouter()
commentaire_router = APIRouter()
tag_router = APIRouter()

# Utilisateurs
@user_router.post('/users/login')
def login():
    pass
@user_router.post('/users/signup')
def signup():
    pass
@user_router.post('/users/create')
def post_users():
    return UserController.post_users()
@user_router.get('/users/list')
def get_users():
    return UserController.get_users()
@user_router.put('/users/update')
def put_users():
    return UserController.put_users()
@user_router.delete('/users/delete')
def delete_users():
    return UserController.delete_users()

# Vidéos
@video_router.post('/videos/create')
def post_video(
    file: Annotated[UploadFile, File()],
    title: Annotated[str, Form()],
    description: Annotated[str, Form()]
):
    return VideoController.upload_video({
        "file": file,
        "title": title,
        "description": description
    })
#async def post_videos(request: Request):
#    return await VideoController.upload_video(request)
@video_router.get('/videos/list')
def get_videos():
    return VideoController.get_videos()
@video_router.put('/videos/update')
def put_videos():
    return VideoController.put_videos()
@video_router.delete('/videos/delete')
def delete_videos():
    return VideoController.delete_videos()

# Commentaires
@commentaire_router.post('/commentaires/create')
def post_commentaires():
    return CommentController.post_commentaires()
@commentaire_router.get('/commentaires/list')
def get_commentaires():
    return CommentController.get_commentaires()
@commentaire_router.put('/commentaires/update')
def put_commentaires():
    return CommentController.put_commentaires()
@commentaire_router.delete('/commentaires/delete')
def delete_commentaires():
    return CommentController.delete_commentaires()

# Tags
@tag_router.post('/tags/create')
def post_tags():
    return TagController.post_tags()
@tag_router.get('/tags/list')
def get_tags():
    return TagController.get_tags()
@tag_router.put('/tags/update')
def put_tags():
    return TagController.put_tags()
@tag_router.delete('/tags/delete')
def delete_tags():
    return TagController.delete_tags()




