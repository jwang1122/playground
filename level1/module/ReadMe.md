# test your python module: myModule.py

In python, module is a file

## Containing in module myModule
* s (a string)
* t (a tuple)
* foo() (a function)
* fooClass (a class)

```
python
import myModule
print(myModule.s)
myModule.foo("this is my test of myModule.")

from myModule import *
print(s)
foo("this is my test of myModule.")

fc = fooClass()
print(fc)
```

## Check path settings

When the interpreter executes the above import statement, it searches for mod.py in a list of directories assembled from the following sources:

The directory from which the input script was run or the current directory if the interpreter is being run interactively
The list of directories contained in the PYTHONPATH environment variable, if it is set. (The format for PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)

An installation-dependent list of directories configured at the time Python is installed

The resulting search path is accessible in the Python variable sys.path, which is obtained from a module named sys:

```
>>> import sys
>>> sys.path
```

* append your path to system path setting
```
>>> sys.path.append(r'/Users/wangqianjiang/workspace/playground')
>>> sys.path
```

## find where my module located
```
>>> import myModule
>>> myModule.__file__
>>> myModule
>>> s
>>> foo('test')
```

compare to 
```
>>> from myModule import *
>>> s
>>> foo("this is a test.")
```

## rename the module
```
>>> from myModule import s as msg
>>> msg
>>> foo("this is a test.")

>>> import myModule as mod
>>> mod.s
```

## import within function
```
>>> def bar(arg):
>>>        from myModule import foo
>>>        foo(arg)

>>> bar("this is a test")
```