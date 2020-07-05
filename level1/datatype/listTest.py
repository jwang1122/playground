# initial empty list
l = []
print(type(l))

l = [1,2,3,4,5]
print(l)

l=list(range(10))
print(l)

l = list(filter(lambda x: x%2==0, range(20)))
print(l)

l1 = [i for i in range(20) if i%2==1]
print(l)

l = [False]*4 # create a default boolean list
print(l)

# modify list
l[4] = "hello"
print(l)
l = l[3:7]
print(l)
l.append(20)
print(l)
l.insert(0, "First")
print(l)
l.append(l1) # list in list
print(l)

