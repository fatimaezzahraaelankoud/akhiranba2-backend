from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)
    nom_complet = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    commentaire = Column(String, nullable=False)
    date_comment = Column(DateTime, default=datetime.utcnow)
 
    