from flask import Flask
from pymongo.mongo_client import MongoClient

import database


uri = "mongodb+srv://chuw7:psGav2DdUOZXuWYE@toilet.mnkp0e1.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    db = client["Toilets"]
    coll = db["toilets"]

    app.run(debug=True)
