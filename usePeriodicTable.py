import json
from periodic import *

periodicFile = open("./data/PeriodicTableJSON.json")
data = json.load(periodicFile)
print(type(data))
elements = data.get("elements")

elementDict = dict()
for e in elements:
    elementObject = Element.from_dict(e)
    elementDict[e["name"]]= elementObject

element = elementDict.get("Uranium")
print(element.name)
print(element.atomic_mass)
print(element.period)