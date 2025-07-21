from fastapi import FastAPI
from app.database import articles_collection
from app.routes.article_routes import router as article_router
from app.routes.comment_route import route as comment_router
app = FastAPI()

@app.get("/")
def test_connection():
    count = articles_collection.count_documents({})
    return {"status": "Connected to MongoDB Atlas", "articles": count}


app.include_router(article_router)
app.include_router(comment_router)