from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, DateTime, Text, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

# Configurez la base de données
SQLALCHEMY_DATABASE_URL = "sqlite:///./bdd.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Définissez le modèle de données pour le compte utilisateur
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False, unique=True)
    pseudo = Column(String(255), unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())

class Video(Base):
    __tablename__ = "video"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(255), nullable=False, unique=True)
    title = Column(String(255), unique=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())
    id_1 = Column(Integer, ForeignKey('user.id'), nullable=False)
    
class Commentaire(Base):
    __tablename__ = "commentaire"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())
    id_1 = Column(Integer, ForeignKey('video.id'), nullable=False)
    id_2 = Column(Integer, ForeignKey('user.id'), nullable=False)
    
class Tags(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, unique=True, nullable=False)

class Aime(Base):
    __tablename__ = "aime"
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    id_1 = Column(Integer, ForeignKey('video.id'), primary_key=True)    
    

class View(Base):
    __tablename__ = "view"
    id = Column(Integer, primary_key=True, index=True)    
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    id_1 = Column(Integer, ForeignKey('video.id'), primary_key=True)    

class Contient(Base):
    __tablename__ = "contient"
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    id_1 = Column(Integer, ForeignKey('video.id'), primary_key=True)    



