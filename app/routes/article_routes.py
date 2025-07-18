from fastapi import APIRouter,HTTPException
from fastapi.encoders import jsonable_encoder
from app.database import articles_collection
from app.model.article_model import article
from bson import ObjectId

router = APIRouter()

# fonction pour convetir data de mongodb en un objet pour le frontend 
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

#Route pour GET articles
@router.get("/articles")
async def get_articles():
    articles = articles_collection.find()
    return [article_serializer(article) for article in articles]


#Route pour GET articles BY id
@router.get("/articles/{id}")
async def get_article_by_id(id: str):
    try:
        obj_id = ObjectId(id)
    except:
        raise HTTPException(status_code=400, detail="ID invalide")

    article = articles_collection.find_one({"_id": obj_id})
    if article:
        return article_serializer(article)
    raise HTTPException(status_code=404, detail="Article non trouvé")


#Route pour GET articles BY category
@router.get("/articles/category/{categorie}")
async def get_articles_by_categorie(categorie: str):
    articles = articles_collection.find({"categorie": categorie})
    return [article_serializer(article) for article in articles]



#Royute pour POST article
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

