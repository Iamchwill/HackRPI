import route
import math

def insert_toilet(collection, location, genders, facilities):
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


def find_closest_toilets(collection, location):
    for document in collection:
        coords = {document['location'][0], document['location'][1]}
        r = route.fastest_route({location[0],location[1]}, coords)
        edge_lengths = osmnx.utils_graph.get_route_edge_attributes(G, r, 'length')
        route_length = sum(edge_lengths)
        print(route_length)

def dist(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1]-pt2[1])**2)

