import json
from periodic import *

periodicFile = open("./data/PeriodicTableJSON.json")
data = json.load(periodicFile)
print("06:", type(data))

elements = data.get("elements")
print("09:", type(elements))

elementDict = dict(map(lambda e: (e["symbol"], Element.from_dict(e)), elements))
# elementDict = dict()
# for e in elements:
#     elementDict[e["name"]]= Element.from_dict(e)

#print(elementDict)
print(elementDict.keys())
element = elementDict.get("Ti")
print(element.name, element.symbol, element.number)
print("row:", element.period, end=' ')
print("column:", element.xpos)
print(element.shells)
print(element.electron_configuration)
print("Total electrons:", sum(element.shells))
