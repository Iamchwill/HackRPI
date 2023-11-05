from flask import Flask, render_template, redirect
from pymongo.mongo_client import MongoClient

import database


uri = "mongodb+srv://chuw7:psGav2DdUOZXuWYE@toilet.mnkp0e1.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

@app.route('/action_add', methods=['POST'])
def action_add() {
    facilities = [request.form.get(toilet), request.form.get(urinal), request.form.get(sink), request.form.get(soap)]
    locat = request.form.get(locat)
    if facilities[0] < 0 or facilities[1] < 0:
	return redirect('/')

}

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
