from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import engine, Base

app = FastAPI()

# Créez la table dans la base de données
Base.metadata.create_all(bind=engine)