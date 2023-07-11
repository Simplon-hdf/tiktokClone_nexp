from sqlalchemy.orm import Session
from sqlalchemy import Select
from models import Video, engine
from fastapi import File, UploadFile
import uuid

class VideoController():

    def get_videos():
        # Code pour récupérer la liste de toutes les videos
        return 'Liste des videos'

    def upload_video(data:dict):
        print(data)
        file: UploadFile = File(data["file"])
        file.filename = uuid.uuid4()
        try:
            with open(file.filename, "wb") as f:
                while contents := file.file.read(1024 * 1024):
                    f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            file.file.close()

        return {"message": f"Successfully uploaded {file.filename}"}
