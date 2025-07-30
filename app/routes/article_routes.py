from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.article_schema import ArticleCreate, ArticleRead
from app.crud import article_crud

router = APIRouter()

# GET all articles
@router.get("/articles", response_model=List[ArticleRead])
async def get_articles():
    return await article_crud.get_all_articles()

# GET article by ID
@router.get("/articles/{id}", response_model=ArticleRead)
async def get_article_by_id(id: int):
    article = await article_crud.get_article_by_id(id)
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    return article

# GET articles by catégorie
@router.get("/articles/category/{categorie}", response_model=List[ArticleRead])
async def get_articles_by_categorie(categorie: str):
    return await article_crud.get_articles_by_category(categorie)

# POST create article
@router.post("/article", response_model=ArticleRead, status_code=status.HTTP_201_CREATED)
async def create_article(article_data: ArticleCreate):
    return await article_crud.create_article(article_data)

# PUT update article
@router.put("/articles/{id}")
async def update_article(id: int, updated_data: ArticleCreate):
    article = await article_crud.get_article_by_id(id)
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    await article_crud.update_article(id, updated_data)
    return {"message": "Article mis à jour"}

# DELETE article
@router.delete("/articles/{id}")
async def delete_article(id: int):
    article = await article_crud.get_article_by_id(id)
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    await article_crud.delete_article(id)
    return {"message": "Article supprimé"}


