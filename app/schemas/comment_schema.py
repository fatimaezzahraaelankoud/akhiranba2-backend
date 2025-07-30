from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class CommentBase(BaseModel):
    article_id: int
    nom_complet: str
    email: EmailStr
    commentaire: str
    date_comment: Optional[datetime] = None

class CommentCreate(CommentBase):
    pass

class CommentRead(CommentBase):
    id: int

    class Config:
        orm_mode = True
