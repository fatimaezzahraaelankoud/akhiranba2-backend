from fastapi import FastAPI
from app.database import articles_collection

app = FastAPI()

@app.get("/")
def test_connection():
    count = articles_collection.count_documents({})
    return {"status": "Connected to MongoDB Atlas", "articles": count}


