answer="y"
while answer=="y":
    number = input("please enter a number: ")
    if int(number) > 5:
        print("the number", number, "is greater than 5")
    else:
        print("the number", number, "is smaller than or equal to 5")
    answer = input("try again?")
