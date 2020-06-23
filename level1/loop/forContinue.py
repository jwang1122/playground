sum = 0
for i in range(10):
    if i > 3 and i < 7:
        sum += i
        continue
    print(i)
print(sum)