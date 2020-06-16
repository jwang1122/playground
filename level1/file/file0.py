"""
create a new file, and write string to it.
"""
file1 = open("hello.txt", "+w")
print("Hello, world! it is a test.", file=file1)
file1.close()
print("Done")