from sqlalchemy.orm import Session
from sqlalchemy import Select
from models import Commentaire, engine
import jwt

class CommentController():
    
    def create_commentaire(self, commentaire: Commentaire):
       with Session(engine) as session:
            newCommentaire = Commentaire(
                content = data["content"],
                created_at = data["created_at"],
                updated_at = data["updated_at"],
                idVideo = data["idVideo"],
                idUser = data["idUser"]       
                )
            session.add(newCommentaire)
            session.commit()
        return commentaire

     def get_commentaires(self):
        commentaires = session.query(Commentaire).all()
        return 'Liste des commentaires'

    def get_commentaire(self, commentaire_id: int):
        commentaire = session.query(Commentaire).filter(Commentaire.id == commentaire_id).first()
        if not commentaire:
            raise HTTPException(status_code=404, detail="Commentaire not found")
        return commentaire

    def update_commentaire(self, commentaire_id: int, updated_commentaire: Commentaire):
        commentaire = session.query(Commentaire).filter(Commentaire.id == commentaire_id).first()
        if not commentaire:
            raise HTTPException(status_code=404, detail="Commentaire not found")
        commentaire.content = updated_commentaire.content
        session.commit()
        session.refresh(commentaire)
        return commentaire

    def delete_commentaire(self, commentaire_id: int):
        commentaire = session.query(Commentaire).filter(Commentaire.id == commentaire_id).first()
        if not commentaire:
            raise HTTPException(status_code=404, detail="Commentaire not found")
        session.delete(commentaire)
        session.commit()
        return {"message": "Commentaire deleted"}

   