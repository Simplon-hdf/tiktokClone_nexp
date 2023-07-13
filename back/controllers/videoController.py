from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from models import Video, engine
from fastapi import UploadFile, Security, status, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import uuid
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
import os
from typing import Generator
from starlette.responses import StreamingResponse

token_key = APIKeyHeader(name="Autorization")

class Token(BaseModel):
    token: str

def get_current_token(auth_key: str = Security(token_key)):
    return auth_key

class VideoController():

    def get_videos():
        # Code pour récupérer la liste de toutes les videos
        return 'Liste des videos'

    def upload_video(self, data: dict):
        file: UploadFile = data["file"]
        file.filename = str(uuid.uuid4())
        url: str = f"video/{file.filename}"
        with Session(engine) as session:
            try:
                new_video = Video(
                    url = url,
                    title = data["title"],
                    description = data["description"],
                    idUser = data["idUser"]
                )
                session.add(new_video)
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise HTTPException(status_code=500, detail="Erreur lors de l'insertion en base de donnée")
        try:
            with open(url, "wb") as f:
                while contents := file.file.read(1024 * 1024):
                    f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            file.file.close()
            return new_video
        
    def delete_video(self, id: int) -> None:
            session = Session(engine)
            query = select(Video).where(Video.id.in_([id]))
            for video in session.scalars(query):
                print(video.url)
                os.remove(video.url)
                session.delete(video)
                session.commit()

    def update_video(self, data: dict):
        print(data)
        session = Session(engine)
        query = select(Video).where(Video.id.in_([data["id"]]))
        for video in session.scalars(query):
            commit = False
            for index in data:
                if data[index] != None:
                    if(index == "file"):
                        file: UploadFile = data["file"]
                        os.remove(video.url)
                        with open(video.url, "wb") as f:
                            while contents := file.file.read(1024 * 1024):
                                f.write(contents)
                        file.file.close()
                    if(index == "title"):
                        video.title = data["title"]
                        commit = True
                    if(index == "description"):
                        video.description = data["description"]
                        commit = True
            if(commit):
                session.commit()

    async def get_data_from_file(self,file_path: str) -> Generator:
        with open(file = file_path, mode = "rb") as f:
            yield f.read()

    async def get_stream_video(self, id):
        session = Session(engine)
        query = select(Video).where(Video.id.in_([id]))
        result = session.scalars(query)
        for video in result:
            try:
                file_contents = self.get_data_from_file(video.url)
                response = StreamingResponse(
                    content = file_contents,
                    status_code = status.HTTP_200_OK,
                    media_type="video/mp4"
                )
                return response
            except FileNotFoundError:
                raise HTTPException(detail="File not found.", status_code=status.HTTP_404_NOT_FOUND)