"""
write json object into json file.
"""
import json

with open("student.json", "+w") as f:
    json.dump({
        'student':{
            'firstname':'John',
            'lastname':'Wang',
            'id':'12345'
        }
    }, f)

with open("student.json") as f:
    x = json.load(f)
    print(x)