"""
create a new file, and write string to it.
"""
file1 = open("hello.txt", "+w")
print("Hello, world!", file=file1)
print("Done")