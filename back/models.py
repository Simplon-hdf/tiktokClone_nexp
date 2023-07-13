from sqlalchemy import create_engine, Column, Integer, DateTime, Text, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship, Mapped, mapped_column
from sqlalchemy.sql import func
import datetime
from typing_extensions import Annotated
from typing import List

# Configurez la base de données
SQLALCHEMY_DATABASE_URL = "sqlite:///./bdd.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
intpk = Annotated[int, mapped_column(primary_key=True)]
timestamp_create = Annotated[datetime.datetime, mapped_column(nullable=False, default=func.CURRENT_TIMESTAMP())]
timestamp_update = Annotated[datetime.datetime, mapped_column(nullable=True, server_onupdate=func.CURRENT_TIMESTAMP())]
Base = declarative_base()

class Based(DeclarativeBase):
    pass


# Définissez le modèle de données pour le compte utilisateur
class User(Based):
    __tablename__ = "user"
    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(String(255), unique=True)
    pseudo: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[timestamp_create]
    updated_at: Mapped[timestamp_update]
    videos: Mapped[List["Video"]] = relationship()
    comments: Mapped[List["Commentaire"]] = relationship()
    videosLiked: Mapped[List["Aime"]] = relationship()
    videosViewed: Mapped[List["View"]] = relationship()

class Video(Based):
    __tablename__ = "video"
    id: Mapped[intpk]
    url: Mapped[str] = mapped_column(String(255), unique=True)
    title: Mapped[str] = mapped_column(String(255), unique=True)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[timestamp_create]
    updated_at: Mapped[timestamp_update]
    idUser: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="videos")
    commentaires: Mapped[List["Commentaire"]] = relationship()
    tags: Mapped[List["Contient"]] = relationship()
    likedBy: Mapped[List["Aime"]] = relationship()
    viewedBy: Mapped[List["View"]] = relationship()
    
class Commentaire(Based):
    __tablename__ = "commentaire"
    id: Mapped[intpk]
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[timestamp_create]
    updated_at: Mapped[timestamp_update]
    idVideo: Mapped[int] = mapped_column(ForeignKey("video.id"))
    video: Mapped["Video"] = relationship(back_populates="commentaires")
    idUser: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="comments")
    
class Tags(Based):
    __tablename__ = "tags"
    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(255), unique=True)
    videos: Mapped[List["Contient"]] = relationship()

class Aime(Based):
    __tablename__ = "aime"
    id: Mapped[intpk]
    idUser: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="videosLiked")
    idVideo: Mapped[int] = mapped_column(ForeignKey("video.id"))
    video: Mapped["Video"] = relationship(back_populates="likedBy")    
    

class View(Based):
    __tablename__ = "view"
    id: Mapped[intpk]
    idUser: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="videosViewed")
    idVideo: Mapped[int] = mapped_column(ForeignKey("video.id"))
    video: Mapped["Video"] = relationship(back_populates="viewedBy")     

class Contient(Based):
    __tablename__ = "contient"
    id: Mapped[intpk]
    idTag: Mapped[int] = mapped_column(ForeignKey("tags.id"))
    tag: Mapped["Tags"] = relationship(back_populates="videos")
    idVideo: Mapped[int] = mapped_column(ForeignKey("video.id"))
    video: Mapped["Video"] = relationship(back_populates="tags")   