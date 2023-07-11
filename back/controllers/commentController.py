from sqlalchemy.orm import Session
from sqlalchemy import Select
from bdd import get_db
from models import Commentaire, engine

class CommentController():
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_commentaire(self, commentaire: Commentaire):
        self.db.add(commentaire)
        self.db.commit()
        self.db.refresh(commentaire)
        return commentaire

    def get_commentaire(self, commentaire_id: int):
        commentaire = self.db.query(Commentaire).filter(Commentaire.id == commentaire_id).first()
        if not commentaire:
            raise HTTPException(status_code=404, detail="Commentaire not found")
        return commentaire

    def update_commentaire(self, commentaire_id: int, updated_commentaire: Commentaire):
        commentaire = self.db.query(Commentaire).filter(Commentaire.id == commentaire_id).first()
        if not commentaire:
            raise HTTPException(status_code=404, detail="Commentaire not found")
        commentaire.content = updated_commentaire.content
        self.db.commit()
        self.db.refresh(commentaire)
        return commentaire

    def delete_commentaire(self, commentaire_id: int):
        commentaire = self.db.query(Commentaire).filter(Commentaire.id == commentaire_id).first()
        if not commentaire:
            raise HTTPException(status_code=404, detail="Commentaire not found")
        self.db.delete(commentaire)
        self.db.commit()
        return {"message": "Commentaire deleted"}

    def get_all_commentaires(self):
        commentaires = self.db.query(Commentaire).all()
        return commentaires