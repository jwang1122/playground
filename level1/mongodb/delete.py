from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['mydb']
bookdb = db.books

_id = '3806a683b8e04ac489dab50b026b4f6a'
result = bookdb.find_one_and_delete({'_id':_id})
print(result)