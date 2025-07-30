from app.database import database
from app.schemas.article_schema import ArticleCreate, ArticleRead
from datetime import datetime
from typing import List, Optional

# GET all articles
async def get_all_articles() -> List[ArticleRead]:
    query = "SELECT * FROM articles ORDER BY date_publication DESC"
    articles = await database.fetch_all(query)
    return articles

# GET article by id
async def get_article_by_id(article_id: int) -> Optional[ArticleRead]:
    query = "SELECT * FROM articles WHERE id = :id"
    article = await database.fetch_one(query, values={"id": article_id})
    return article

# GET articles by categorie
async def get_articles_by_category(categorie: str) -> List[ArticleRead]:
    query = "SELECT * FROM articles WHERE categorie = :categorie ORDER BY date_publication DESC"
    articles = await database.fetch_all(query, values={"categorie": categorie})
    return articles

# CREATE new article
async def create_article(article_data: ArticleCreate) -> ArticleRead:
    query = """
    INSERT INTO articles (titre, contenu, slug, resume, image_url, categorie, date_publication, auteur)
    VALUES (:titre, :contenu, :slug, :resume, :image_url, :categorie, :date_publication, :auteur)
    RETURNING id, titre, contenu, slug, resume, image_url, categorie, date_publication, auteur
    """
    article_dict = article_data.dict()
    if not article_dict.get("date_publication"):
        article_dict["date_publication"] = datetime.utcnow()
    new_article = await database.fetch_one(query, values=article_dict)
    return new_article

# UPDATE article
async def update_article(article_id: int, updated_data: ArticleCreate) -> None:
    query = """
    UPDATE articles SET
        titre = :titre,
        contenu = :contenu,
        slug = :slug,
        resume = :resume,
        image_url = :image_url,
        categorie = :categorie,
        date_publication = :date_publication,
        auteur = :auteur
    WHERE id = :id
    """
    article_dict = updated_data.dict()
    if not article_dict.get("date_publication"):
        article_dict["date_publication"] = datetime.utcnow()
    article_dict["id"] = article_id
    await database.execute(query, values=article_dict)

# DELETE article
async def delete_article(article_id: int) -> None:
    query = "DELETE FROM articles WHERE id = :id"
    await database.execute(query, values={"id": article_id})
