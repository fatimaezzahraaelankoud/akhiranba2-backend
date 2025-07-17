from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class article(BaseModel):
    id: Optional[str] = None
    titre: str
    contenu: str 
    slug: Optional[str]  
    resume: Optional[str] 
    image_url: str 
    categorie: str
    date_publication : datetime
    auteur: str 



    

