import route
import math


def insert_blank_toilet(collection, location, genders, facilities):
    new_toilet = {
        'location': location,
        'quality': 0.0,
        'reviews': 0,
        'genders': genders,
        'toilet': facilities[0],
        'urinal': facilities[1],
        'sink': facilities[2],
    }
    collection.insert_one(new_toilet)

def insert_toilet(collection, location, quality, genders, facilities):
    new_toilet = {
        'location': location,
        'quality': quality,
        'reviews': 1,
        'genders': genders,
        'toilet': facilities[0],
        'urinal': facilities[1],
        'sink': facilities[2],
    }
    collection.insert_one(new_toilet)

def edit_location(collection, tid, new_location, genders, facilities):
    collection.update_one({'_id': tid},
        { "$set": { 
            'location': new_location,
            'genders': genders,
            'toilet': facilities[0],
            'urinal': facilities[1],
            'sink': facilities[2],
        } 
    })

    
def add_review(collection, tid, quality):
    toilet = collection.find_one({'toiletId': int(tid)})
    q = toilet['quality']
    r = toilet['reviews']
    toilet['quality'] = (q * r + quality) / (r + 1)
    toilet['reviews'] += 1
    collection.replace_one({'toiletId': tid}, toilet)


def find_closest_toilet(collection, location):
    min_length = math.inf
    min_route = []
    for document in collection.find({}):
        coords = (float(document['location'][0]), float(document['location'][1]))
        r, r_length = route.fastest_route((location[0],location[1]), coords)
        print(r_length)
        
        if r_length < min_length:
            min_length = r_length
            min_route = r

    return min_route

def read_locations(coll):
    f=open("data.txt", "r")
    for line in f:
        l = line[:-1].split(",")
        insert_blank_toilet(
            coll,
            l,
            ['True', 'True', 'null'],
            ['2', '2', 'sink'],
        )

def get_id_from_location(coll, locat):
    t = collection.find_one({'location': locat})
    return t['toiletid']


