from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

router = APIRouter()

# Modèle Article simplifié
class Article(BaseModel):
    titre: str
    contenu: str
    auteur_id: str
    categorie_id: str
    image: Optional[str] = None
    tags: Optional[List[str]] = []

# En attendant la base de données, stockons temporairement les articles dans une liste
fake_articles_db = []

@router.post("/articles")
def ajouter_article(article: Article):
    article_dict = article.dict()
    article_dict["date_publication"] = datetime.utcnow()
    fake_articles_db.append(article_dict)
    return {"message": "Article ajouté", "article": article_dict}

@router.get("/articles")
def get_articles():
    return fake_articles_db
