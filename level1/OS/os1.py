import os

print(os.getcwd())
os.chdir('level1')
print(os.getcwd())
#os.system('mkdir test')
print(os.getcwd())

print(dir(os))

import shutil
shutil.copyfile('math1.py','math2.py')
shutil.move('math2.py')