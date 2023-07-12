from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Tags, engine

class TagController():

    def get_tags():
        # Code pour récupérer la liste de tous les tags
        with Session(engine) as session:
            tags = session.query(Tags).all()
            list_tags = [tag.name for tag in tags]
        return list_tags
    
    def create_tags(name, post):
        # Code pour créer des tags
        with Session(engine) as session:
            tags = Tags(name=name, post=post)
            session.add(tags)
            session.commit()

    def update_tags(tag_identifier, new_content, tags_id):
        # Code pour changer des tags en saisissant l'id ou le nom 
        with Session(engine) as session:
            tags = session.query(Tags).get(tags_id)
            if tags:
                tags.name = new_content
                session.commit()
                return True
            else:
                return False
            
    def delete_tags(tag_identifier, tags_id):
        #Code pour supprimer des tags
        with Session(engine) as session:
            tags = session.query(Tags).get(tags_id)
            if tags:
                session.delete(tags)
                session.commit()
                return True
            else:
                return False
            
            #J'ai ajouté un commentaire à la fin nde ce code pour m'assurer
            #Que c'est bien cette branche qui a été prise en compte
            #c'est moi la vraie branche, l'autre n'est qu'une importure >:((