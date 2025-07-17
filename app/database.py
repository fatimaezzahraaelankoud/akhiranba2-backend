
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://akhiranbaa_mictechteam1:X35!8gf-sAB7CTy@cluster0.woc5ync.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Database name
db = client["akhir_alanbaa"]

# Articles collection
articles_collection = db["articles"]