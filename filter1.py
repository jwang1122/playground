"""
Use filter function.
"""
if(__name__ == '__main__'):
    temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires", 19),("Los Angeles", 26), \
            ("Tokyo", 27), ("New York", 28),("London", 22),("Beijing", 32)]
    gt25 = lambda data: data[1]>25

    x = list(filter(gt25, temps))
    print(x)
