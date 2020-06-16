"""
Read existing file and add new line in the same file.
"""
def fileread(filaname):
    file1 = open(filaname)
    text = file1.read()
    file1.close()
    return text

def filewrite(filename, line):
    file1 = open(filename, 'a')
    file1.write(f"\nprint('{line}')")
    file1.close()

if(__name__ == '__main__'):
    print(fileread("circle.py"))
    filewrite("circle.py", "Hello, world.")
