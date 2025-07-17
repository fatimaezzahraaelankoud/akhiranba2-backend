from fastapi import APIRouter,HTTPException
from fastapi.encoders import jsonable_encoder
from app.database import articles_collection
from app.model.article_model import article
from bson import ObjectId

router = APIRouter()

def article_serializer(data) -> dict:
    return {
        "id": str(data["_id"]),  
        "titre": data["titre"],
        "contenu": data["contenu"],
        "slug": data.get("slug"),
        "resume": data.get("resume"),
        "image_url": data["image_url"],
        "categorie": data["categorie"],
        "date_publication": data["date_publication"],
        "auteur": data["auteur"],
    }

@router.get("/articles")
async def get_articles():
    articles = articles_collection.find()
    return [article_serializer(article) for article in articles]




@router.post("/article")

async def create_article(article_data: article):
    article_dict = jsonable_encoder(article_data)
    # Supprime 'id' ou '_id' si présents pour éviter doublons
    article_dict.pop("id", None)
    article_dict.pop("_id", None)

    result = articles_collection.insert_one(article_dict)

    # Ajoute l'id MongoDB converti en str
    article_dict["id"] = str(result.inserted_id)

    return article_dict

