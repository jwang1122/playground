import random
"""
1. Two six-sided dice are rolled. What is the probability 
that the numbers on the dice are different?
all set are 6*6=36, there are 6 equal, 30/36 are different. 
Answer: 30/36 = 5/6 = 8.3333333

2. Bob rolls 7 for 6-side dice.
What is the probability that the
sum of the numbers on his dice are no more than 10.

"""
min = 1
max = 6
count = 0
tests = 10000
for i in range(tests):
    sum = 0
    dice1 = random.randint(min, max)
    dice2 = random.randint(min, max)
    # dice3 = random.randint(min, max)
    # dice4 = random.randint(min, max)
    # dice5 = random.randint(min, max)
    # dice6 = random.randint(min, max)
    # dice7 = random.randint(min, max)
    # sum = dice1 + dice2 + dice3 + dice4 + dice5 + dice6 + dice7
    # if (sum < 10):
    #     count += 1
    if(dice1 != dice2):
        count+=1

print("posibility for 100000", count / float(tests))
print("Correct answer is ", 5/6.)
#print("posibility in fraction", 1 / 9)
