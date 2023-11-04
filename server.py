from flask import Flask, render_template
from pymongo.mongo_client import MongoClient

import database


uri = "mongodb+srv://chuw7:psGav2DdUOZXuWYE@toilet.mnkp0e1.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

@app.route('/')
def hello_world():
    return render_template('main.html')

if __name__ == "__main__":
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    db = client["Toilets"]
    coll = db["toilets"]

    app.run(debug=True)
