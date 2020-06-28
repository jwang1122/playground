import json
from periodic import *

periodicFile = open("./data/PeriodicTableJSON.json")
data = json.load(periodicFile)
print("06:",type(data))

elements = data.get("elements")
print("09:", type(elements))

elementDict = dict(map(lambda e: (e["name"], Element.from_dict(e)), elements))
# elementDict = dict()
# for e in elements:
#     elementObject = Element.from_dict(e)
#     elementDict[e["name"]]= elementObject

print(elementDict)
element = elementDict.get("Uranium")
print(element.name)
print(element.atomic_mass)
print(element.period)
print(element.shells)