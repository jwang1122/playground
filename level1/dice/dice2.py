import random

"""
Bob rolls 7 for 6-side dice.
What is the probability that the
sum of the numbers on his dice are no more than 10.
"""
min = 1
max = 6
count = 0
tests = 1000000
for i in range(tests):
    sum=0
    dice1 = random.randint(min, max)
    dice2 = random.randint(min, max)
#    dice3 = random.randint(min, max)
#    dice4 = random.randint(min, max)
#    dice5 = random.randint(min, max)
#    dice6 = random.randint(min, max)
#    dice7 = random.randint(min, max)
    sum = dice1+dice2 #+dice3+dice4+dice5+dice6+dice7
    if(sum==9):
        count+=1

print("posibility for 100000",count/float(tests))
print("posibility in fraction",1/9)