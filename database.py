def insert_toilet(collection, location, genders, facilities):
    new_toilet = {
        'location': location,
        'quality': 0.0,
        'reviews': 0,
        'genders': genders,
        'toilet': facilities[0],
        'urinal': facilities[1],
        'sink': facilities[2],
        'soap': facilities[3],
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
            'soap': facilities[3],
        } 
    })

    
def add_review(collection, tid, quality):
    toilet = collection.find_one({'_id': tid})
    q = toilet['quality']
    r = toilet['reviews']
    toilet['quality'] = (q * r + quality) / (r + 1)
    toilet['reviews'] += 1
    collection.replace_one({'_id': tid}, toilet)

