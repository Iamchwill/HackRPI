from flask import Flask, jsonify, render_template, redirect, request
from pymongo.mongo_client import MongoClient
from bson.json_util import dumps
import re

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
@app.route('/action_review', methods=['POST'])
def action_review():
    locat = request.form.get("location")
    splicedlocation = locat.split(", ")
    qual = request.form.get("quality")
    if not qual.isnumeric() or int(qual) < 0 or int(qual) > 5:
        return redirect('/')
    if len(splicedlocation) != 2 or re.match(r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$', splicedlocation[0]) == None or re.match(r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$', splicedlocation[1]) == None:
        return redirect('/')
    qual = int(qual)
    database.add_review(coll, splicedlocation, qual)
    return redirect('/')
@app.route('/action_add', methods=['POST'])
def action_add():
    facilities = [request.form.get("toilets"), request.form.get("urinals"), request.form.get("sink")]
    locat = request.form.get("location")
    qual = request.form.get("quality")
    men = request.form.get("men")
    women = request.form.get("women")
    unisex = request.form.get("uni")
    splicedlocation = locat.split(", ")
    if not facilities[0].isnumeric() or not facilities[1].isnumeric() or int(facilities[0]) < 0 or int(facilities[1]) < 0:
	    return redirect('/')
    print(facilities[2])
    if facilities[2] != "True" and facilities[2] != None:
        return redirect('/')
    if not qual.isnumeric() or int(qual) < 0 or int(qual) > 5:
        return redirect('/')
    if men != "True" and men != None:
        return redirect('/')
    if women != "True" and women != None:
        return redirect('/')
    if unisex != "True" and unisex != None:
        return redirect('/')
    if len(splicedlocation) != 2 or re.match(r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$', splicedlocation[0]) == None or re.match(r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$', splicedlocation[1]) == None:
        return redirect('/')
    
    if men == None:
        men = False
    else:
        men = True
    if women == None:
        women = False
    else:
        women = True
    if unisex == None:
        unisex = False
    else:
        unisex = True
    if facilities[2] == None:
        facilities[2] = False
    else:
        facilities[2] = True
    facilities[0] = int(facilities[0])
    facilities[1] = int(facilities[1])
    qual = int(qual)
    database.insert_toilet(
        coll,
        splicedlocation,
        qual,
        [men, women, unisex],
        facilities,
    )

    
    return redirect('/')

@app.route('/action_review', methods=['POST'])
def action_review():
    tid = request.form.get("tid")
    qual = int(request.form.get("quality"))

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
