import asyncio
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

async def test_connection():
    url = os.getenv("DATABASE_URL")
    print("Testing connection to:", url)
    try:
        conn = await asyncpg.connect(url)
        print("Connected!")
        await conn.close()
    except Exception as e:
        print("Connection failed:", e)

asyncio.run(test_connection())
