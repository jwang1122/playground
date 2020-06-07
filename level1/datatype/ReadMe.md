# Python Data Type

## Basic Data Type
![Python Data Type](../../images/DataType.png)

* Number
    - int
    - float
    - complex
* String
    - str
* Tuple
    - tuple
* List
    - list
* Set
    - set
* Dictionary
    - dic

python, does not like other language, determine the data type at data assignment time.
```
>>> a = 5
>>> type(a)
>>> a = 3.4
>>> type(a)
>>> a = 4 + 5j
>>> type(a)
>>> a = (1,2,3)
>>> type(a)
>>> a = [4,6,5]
>>> type(a)
>>> a = {1,2,3}
>>> type(a)
>>> a = {"k1":"value1","k2":"value2"}
>>> type(a)
```
## get individual item from tuple, list and dict
```
a = (1,2,3,4,5)
a[1]

a = {"k1":"value1","k2":"value2"}
a["k1"]
a.get("k1")
```
## Different data type in Tuple or list
```
a = (1,2,'hello',4,5)
```

## change values in tuple, list, set and dict
```
>>> a = [1,2,3,4]
>>> a.append(5)
>>> a = {1,2,3}
>>> a.add(5)
>>> a.add(3)
```
## Operator on tuple, list, set, ...
* + on tuple
```
a = (1,2,3)
b = (4,5,6)
b + a
```
* + on list
```
a = [1,2,3]
b = [4,5,6]
a + b
```