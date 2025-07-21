from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime

class Comment(BaseModel):
    id : Optional[str] = None
    article_id : str 
    nom_complet : str 
    email : EmailStr
    commentaire : str
    date_comment : datetime 
    