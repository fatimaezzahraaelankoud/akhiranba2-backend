from databases import Database
import os
from dotenv import load_dotenv

load_dotenv()  # charge les variables d'environnement depuis .env

DATABASE_URL = os.getenv("DATABASE_URL")

database = Database(DATABASE_URL)


