from pymongo import MongoClient
import uuid
import json

client = MongoClient('mongodb://localhost:27017')
db = client['mydb']
bookdb = db.books

_id = '3806a683b8e04ac489dab50b026b4f6a'
result = bookdb.find_one_and_delete({'_id':_id})
book = {
    "title": "White Fragility: Why It's So Hard for White People to Talk About Racism",
    "author": "Robin DiAngelo",
    "read": True,
    "price": 21.69,
    "rating": 5
}
book["_id"] = _id
result = bookdb.insert_one(book)
print(result.inserted_id)
