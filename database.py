import route
import math

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
    toilet = collection.find_one({'_id': tid})
    q = toilet['quality']
    r = toilet['reviews']
    toilet['quality'] = (q * r + quality) / (r + 1)
    toilet['reviews'] += 1
    collection.replace_one({'_id': tid}, toilet)


def find_closest_toilet(collection, location):
    min_length = inf
    min_route = []
    for document in collection:
        coords = {document['location'][0], document['location'][1]}
        r = route.fastest_route({location[0],location[1]}, coords)
        r_length = route.route_length(r)
        print(r_length)
        
        if r_length < min_length:
            min_length = r_length
            min_route = r

    return min_route


