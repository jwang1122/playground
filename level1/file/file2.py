"""
show difference between open and with open.
with open will close the file automatically.
"""
with open("circle.py") as f:
    for line in f:
        print(line, end='')
    print('\n04:', f.closed)  # ourput：False

print("06:", f.closed)  # output：True

file1 = open("circle.py")
flag = True
while(flag):
    line = file1.readline()
    print(line, end='')
    if len(line) == 0:
        flag = False
        file1.close()
        print('')
