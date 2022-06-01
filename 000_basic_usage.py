from bson import ObjectId
from pymongo import MongoClient

def openClose():
    client = MongoClient('mongodb://localhost:37000/')

    db = client["does-not-exist"]
    print(db)

    db = client.mflix
    print(db)

    db = client["mflix"]
    print(db)

    comments = db.comments
    print(comments)

    comments = db["comments"]
    print(comments)

    client.close()

def insert():
    client = MongoClient('mongodb://localhost:37000/')

    db = client["mflix"]
    print(db)

    coll = db["tickets"]
    print(coll)

    ticket = {
        "code": "qweQWE123",
        "possible_dates" : ["220425", "220523"]
    }
    x = coll.insert_one(ticket)
    print(f"objectid ${x.inserted_id}")

    print(x.acknowledged)

    document = coll.find_one({'_id': x.inserted_id})
    print(document)
    document = coll.find_one({'_id': ObjectId("626a4a45799739942a888695")})

    print(document)

    client.close()

def find():
    client = MongoClient('mongodb://localhost:37000/')

    query = {
        "year": 2000
    }
    projection = {
        "year": 1,
        "title": 1,
        "_id": 0
    }
    for post in client.mflix.movies.find(
            filter=query,
            projection=projection,
            limit=4):
        print(post)

    query = {
        "year": {"$eq": 2010}
    }
    projection = {
        "year": 1,
        "title": 1,
        "_id": 0
    }
    for post in client.mflix.movies.find(filter=query, projection=projection, limit=4):
        print(post)

    client.close()

if __name__ == '__main__':
    openClose()
    insert()
    find()