from fastapi import APIRouter, Request, File, Form, UploadFile, Depends
from controllers.userController import UserController
from controllers.videoController import VideoController
from controllers.commentController import CommentController
from controllers.tagController import TagController
from typing import Annotated, Optional
from dependency import has_access

user_router = APIRouter()
video_router = APIRouter()
commentaire_router = APIRouter()
tag_router = APIRouter()
user = UserController()

PROTECTED = [Depends(has_access)]

# Utilisateurs
@user_router.post('/login')
async def login(request:Request):
    return user.login(await request.json())
@user_router.post('/signup')
async def signup(request:Request):
    return user.create_user(await request.json())
@user_router.post('/users/create')
def post_users():
    return user.post_users()
@user_router.get('/users/list')
def get_users():
    return user.get_users()
@user_router.get('/user/{id}')
def get_user(id):
    return user.get_user(id)
@user_router.put('/users/update')
def put_users():
    return user.put_users()
@user_router.delete('/users/delete')
def delete_users():
    return user.delete_users()

video = VideoController()
# Vidéos
@video_router.post(
    '/videos/create',
    dependencies = PROTECTED
)
def post_video(
    file: Annotated[UploadFile, File()],
    title: Annotated[str, Form()],
    description: Annotated[str, Form()],
    idUser: Annotated[int, Form()]
):
    return video.upload_video({
        "file": file,
        "title": title,
        "description": description,
        "idUser": idUser
    })
@video_router.delete(
    "/videos/{id}/delete",
    dependencies = PROTECTED
)
def delete_video(id):
    return video.delete_video(id)
@video_router.put(
        "/videos/update",
        dependencies = PROTECTED
)
def update_video(
    id: Annotated[int, Form()],
    file: Optional[UploadFile] = File(),
    title: Optional[str] = Form(),
    description: Optional[str] = Form(None)
):
    return video.update_video({
        "id": id,
        "file": file,
        "title": title,
        "description": description
    })
@video_router.get("/video/{id}")
async def stream_video(id):
    return await video.get_stream_video(id)

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




