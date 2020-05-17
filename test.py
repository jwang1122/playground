x = int('10')
print(x)
print(type(x))

x = int('10\n')
print(x)
print(type(x))

x = '\n'
#x = int('\n')
#x = int('')
print(len(x))
print(type(x))
x = x.strip()
print(len(x))

x = '  123 \n'
print("[%s]" % x)

x = x.strip()
print("[%s]" % x)
