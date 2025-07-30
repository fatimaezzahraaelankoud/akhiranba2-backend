from app.database import database
from app.schemas.comment_schema import CommentCreate, CommentRead
from typing import List, Optional
from datetime import datetime

# GET comments by article_id
async def get_comments_by_article(article_id: int) -> List[CommentRead]:
    query = """
    SELECT * FROM comments WHERE article_id = :article_id ORDER BY date_comment DESC
    """
    comments = await database.fetch_all(query, values={"article_id": article_id})
    return comments

# CREATE a comment
async def create_comment(comment_data: CommentCreate) -> CommentRead:
    query = """
    INSERT INTO comments (article_id, nom_complet, email, commentaire, date_comment)
    VALUES (:article_id, :nom_complet, :email, :commentaire, :date_comment)
    RETURNING id, article_id, nom_complet, email, commentaire, date_comment
    """
    comment_dict = comment_data.dict()
    if not comment_dict.get("date_comment"):
        comment_dict["date_comment"] = datetime.utcnow()
    new_comment = await database.fetch_one(query, values=comment_dict)
    return new_comment

# DELETE comment by id
async def delete_comment(comment_id: int) -> None:
    # Check if comment exists before deleting
    query_check = "SELECT id FROM comments WHERE id = :id"
    existing = await database.fetch_one(query_check, values={"id": comment_id})
    if not existing:
        raise Exception("Commentaire non trouvé")

    query_delete = "DELETE FROM comments WHERE id = :id"
    await database.execute(query_delete, values={"id": comment_id})


# UPDATE comment by id
async def update_comment(comment_id: int, updated_data: CommentCreate) -> None:
    # Vérifier si le commentaire existe
    query_check = "SELECT id FROM comments WHERE id = :id"
    existing = await database.fetch_one(query_check, values={"id": comment_id})
    if not existing:
        raise Exception("Commentaire non trouvé")

    query_update = """
    UPDATE comments SET
        article_id = :article_id,
        nom_complet = :nom_complet,
        email = :email,
        commentaire = :commentaire,
        date_comment = :date_comment
    WHERE id = :id
    """
    data_dict = updated_data.dict()
    if not data_dict.get("date_comment"):
        data_dict["date_comment"] = datetime.utcnow()
    data_dict["id"] = comment_id

    await database.execute(query_update, values=data_dict)

