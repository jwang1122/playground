"""
write json object (dict) into json file.
and load the content from the file.
"""
import json

with open("./data/student.json", "+w") as f:
    json.dump({
        'student1':{
            'firstname':'John',
            'lastname':'Wang',
            'id':'12345'
        },
        'student2':{
            'firstname':'Bryan',
            'lastname':'Johnson',
            'id':'34567'
        }
    }, f)

with open("./data/student.json") as f:
    x = json.load(f)
    print(type(x))
    print(x)