from pymongo import MongoClient
import uuid
import json

client = MongoClient('mongodb://localhost:27017')
db = client['mydb']
bookdb = db.books

_id = '3806a683b8e04ac489dab50b026b4f6a'
result = bookdb.find_one({'_id':_id})
file1 = open("book.json","a")
json.dump(result, file1)
file1.close()
print("the book info is saved to book.json file.")