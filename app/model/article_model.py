from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String(255), nullable=False)
    contenu = Column(Text, nullable=False)
    slug = Column(String(255), nullable=True)
    resume = Column(Text, nullable=True)
    image_url = Column(String(500), nullable=False)
    categorie = Column(String(100), nullable=False)
    date_publication = Column(DateTime, default=datetime.utcnow)
    auteur = Column(String(255), nullable=False)




    

