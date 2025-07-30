from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.comment_schema import CommentCreate, CommentRead
from app.crud.comment_crud import get_comments_by_article, create_comment, delete_comment ,update_comment

route = APIRouter()
# get comments by article id
@route.get("/comments/{article_id}", response_model=List[CommentRead])
async def get_comments(article_id: int):
    return await get_comments_by_article(article_id)
# post comment
@route.post("/comments", response_model=CommentRead, status_code=status.HTTP_201_CREATED)
async def post_comment(comment: CommentCreate):
    return await create_comment(comment)
# delete article
@route.delete("/comments/{id}")
async def remove_comment(id: int):
    try:
        await delete_comment(id)
    except Exception:
        raise HTTPException(status_code=404, detail="Commentaire non trouvé")
    return {"message": "Commentaire supprimé"}

# update comment
@route.put("/comments/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_comment_route(id: int, updated_comment: CommentCreate):
    try:
        await update_comment(id, updated_comment)
    except Exception:
        raise HTTPException(status_code=404, detail="Commentaire non trouvé")
    return {"message": "Commentaire mis à jour"}
