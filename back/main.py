from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import engine, Base
from routes import user_router, video_router, commentaire_router


app = FastAPI()

app.include_router(user_router)
app.include_router(video_router)
app.include_router(commentaire_router)


# Créez la table dans la base de données
Base.metadata.create_all(bind=engine)

