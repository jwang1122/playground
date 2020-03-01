x = input("Please enter a integer number: ")
x = int(x)
if x < 0:
    x = 0
    print("you enter a negative number, and will be change to 0.")
elif x == 0:
    print("you enter a 0.")
else:
    print("you enter a positive number")

print("x = %d" % x)
