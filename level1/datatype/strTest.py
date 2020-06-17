s = "this is a Test."
print("02:", s.capitalize())
print("03:", s.title())
print("04:", s.upper())
print("04:", s.lower())
print(s.center(80))

print(s.endswith("."))
print(s.startswith("this"))
print("10:", s.find("is"))
print("11:", s.index("is"))
print(s.find("is", 3))
print(s.find("john"))

print("14:", "123".zfill(5))

a, b = 11, 31
c = a + b
s = "{0}+{1}={2}"
print(s.format(a, b, c))

s = "2a"
print(s.isalnum())
print(s.isalpha())
s = "12"
print(s.isnumeric())
print(s.isdigit())

print("3.4".isdecimal())
print("1.2".isdigit())

# check if a string is a float number
f = "2.34"
print("32:", f + str(3.5))
f = float(f) if f.replace('.', '', 1).isdigit() else f
print("34:", f + 3.5)
print(type(f))

print(" of ".join(["1", "10", "100"]))

print("   123".lstrip(' '))
print("   123   ".strip())
print("1,2,3,4,5".split(','))
print("1,2,3,4,5".split(',', 2))
print("1,2,3,4,5".rsplit(',', 2))
print("1,2\n3\n4,5".splitlines())

print("1,234".partition(','))

print("1234567".replace("345", "abc", 3))
print("1234567".rfind("89"))
#print("1234567".rindex("89"))

import pandas as pd

Data = {'Product': ['ABC', 'XYZ'], 'Price': ['250', '270']}

df = pd.DataFrame(Data)
df['Price'] = df['Price'].astype(float)

print(df)
print(df.dtypes)
