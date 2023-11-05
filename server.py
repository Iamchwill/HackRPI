from flask import Flask, render_template, redirect, request
from pymongo.mongo_client import MongoClient

import database


uri = "mongodb+srv://chuw7:psGav2DdUOZXuWYE@toilet.mnkp0e1.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

@app.route('/formb')
def formb():
    return render_template('review_form.html')

@app.route('/forma')
def forma():
    return render_template('form.html')
@app.route('/action_add', methods=['POST'])
def action_add():
    facilities = [request.form.get("toilets"), request.form.get("urinals"), request.form.get("sink"), request.form.get("soap")]
    locat = request.form.get("locat")
    qual = request.form.get("qual")
    unisex = request.form.get("uni")
    men = request.form.get("men")
    woman = request.form.get("women")
    if int(facilities[0]) < 0 or int(facilities[1]) < 0:
	    return redirect('/')
    return redirect('/')


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
