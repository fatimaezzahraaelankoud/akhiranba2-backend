from fastapi import FastAPI
from app.database import database  # objet Database PostgreSQL async
from app.routes.article_routes import router as article_router
from app.routes.comment_route import route as comment_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def test_connection():
    # Exemple: compter les articles dans PostgreSQL
    query = "SELECT COUNT(*) FROM articles"
    count = await database.fetch_val(query)
    return {"status": "Connected to PostgreSQL", "articles": count}

app.include_router(article_router)
app.include_router(comment_router)


