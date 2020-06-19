"""
create a new file, and write string to it.
"""
file1 = open("hello.txt", "+w")
print("Hello, world!", file=file1)

name = input("Enter your name please: ")
print(f"Hello {name}.", file=file1)

file1.close()
print("Done")
