from circle import circle_area

area = circle_area(1)
print("05:",area)

area = circle_area(2.3)
print("08:",area)

try:
    area = circle_area(-2)
    print("11:",area)
except ValueError as err:
    print('13: error: {0}'.format(err))

try:
    area = circle_area(-2+3j)   
    print("17:",area)
except TypeError as err:
    print("19: error: {0}".format(err))


#area = circle_area('hello')
#print("17:",area)

#area = circle_area(None) 
#print("27:",area)
