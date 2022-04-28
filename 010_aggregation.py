from pymongo import MongoClient

if __name__ == '__main__':
    # Requires the PyMongo package.
    # https://api.mongodb.com/python/current

    client = MongoClient('mongodb://localhost:37000/')
    result = client['mflix']['comments'].aggregate([
        {
            '$group': {
                '_id': '$email',
                'movieCount': {
                    '$count': {}
                }
            }
        }, {
            '$sort': {
                'movieCount': -1
            }
        }, {
            '$limit': 3
        }
    ])

    for c in result:
        print(c)

    client.close()