from flask import Flask, jsonify, render_template, redirect, request
from pymongo.mongo_client import MongoClient
from bson.json_util import dumps

import database


uri = "mongodb+srv://chuw7:psGav2DdUOZXuWYE@toilet.mnkp0e1.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

db = client["Toilets"]
coll = db["toilets"]

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

@app.route('/locations')
def locations():
    return dumps(list(coll.find({})))

@app.route('/review_form.html')
def review_form():
    return render_template('review_form.html')

@app.route('/form.html')
def form():
    return render_template('form.html')

@app.route('/action_add', methods=['POST'])
def action_add():
    facilities = [request.form.get("toilets"), request.form.get("urinals"), request.form.get("sink")]
    locat = request.form.get("location")
    qual = request.form.get("quality")
    men = request.form.get("men")
    women = request.form.get("women")
    unisex = request.form.get("uni")

    database.insert_toilet(
        coll,
        locat,
        qual,
        [men, women, unisex],
        facilities,
    )

    if int(facilities[0]) < 0 or int(facilities[1]) < 0:
	    return redirect('/')
    return redirect('/')

@app.route('/action_route', methods=['POST'])
def action_route():
    tid = request.form.get("tid")
    qual = request.form.get("quality")

    database.add_review(coll, tid, qual)
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
        
    #print(database.find_closest_toilet(coll, [40.8, -74]))
    #database.read_locations(coll)

    app.run(debug=True)
