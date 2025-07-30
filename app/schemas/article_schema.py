from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ArticleBase(BaseModel):
    titre: str
    contenu: str
    slug: Optional[str] = None
    resume: Optional[str] = None
    image_url: str
    categorie: str
    date_publication: Optional[datetime] = None
    auteur: str

class ArticleCreate(ArticleBase):
    pass

class ArticleRead(ArticleBase):
    id: int

    class Config:
        orm_mode = True
