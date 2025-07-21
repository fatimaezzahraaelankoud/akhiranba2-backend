from fastapi import APIRouter,HTTPException
from app.model.comment_model import Comment
from app.database import comments_collection
from bson import ObjectId

route = APIRouter()

def comment_serializer(data) -> dict :
     return {
          "id": str(data["_id"]) ,
          "article_id" : data["article_id"] ,
          "nom_complet" : data["nom_complet"] ,
          "email" : data["email"],
          "commentaire" : data["commentaire"],
          "date_comment" : data["date_comment"]
     }


@route.get("/comments/{article_id}")
async def get_comments(article_id : str):
     comments = comments_collection.find({"article_id" : article_id})
     return [
          comment_serializer(comment) for comment in comments
     ]


@route.post("/comment"):

