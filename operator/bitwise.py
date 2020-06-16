# Bitwise Operator
a = 0b00111100
b = 0b00001101
print(a)
print(b)
print(bin(a))  # print in binary
a = 0x3c
print(hex(a))  
c = a & b     # 0011 1100   AND
print("39:",bin(c)) # 0000 1101
c = a | b     # OR
print("41:",bin(c))
c = a ^ b     # XOR
print("43:",bin(c))