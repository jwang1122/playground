def my_timer(original):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original(*args, **kwargs)
        t2 = time.time() - t1
        print(f'08: {original.__name__} ran in {t2:.3f} seconds.')
        return result
    return wrapper

def display_info(name, age):
    import time
    time.sleep(2) # simulate long process function
    print(f"16: display_info()... run with arguments: ({name}, {age})")

f = my_timer(display_info)
f("John", 23)

def anotherLongRun(parm1, parm2):
    import time
    time.sleep(3)
    print(f"23: another long run process with arguments({parm1}, {parm2})")

f = my_timer(anotherLongRun)
f("Long", "Run...")