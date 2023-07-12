from sqlalchemy.orm import Session
from sqlalchemy import Select
from models import Video, engine
from fastapi import File, UploadFile
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import uuid

class VideoController():

    def get_videos():
        # Code pour récupérer la liste de toutes les videos
        return 'Liste des videos'

    def upload_video(data: dict):
        file: UploadFile = data["file"]
        file.filename = str(uuid.uuid4())
        print(file.filename)
        try:
            url: str = f"video/{file.filename}"
            with open(url, "wb") as f:
                while contents := file.file.read(1024 * 1024):
                    f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            file.file.close()
            with Session(engine) as session:
                try:
                    new_video = Video(
                        url = url,
                        title = data["title"],
                        description = data["description"],
                        idUser = 1
                    )
                    session.add(new_video)
                    session.commit()
                    return new_video
                except SQLAlchemyError as e:
                    session.rollback()
                    raise HTTPException(status_code=500, detail="Erreur lors de l'insertion en base de donnée")