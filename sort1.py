def test():
    temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires", 19),("Los Angeles", 26), \
            ("Tokyo", 27), ("New York", 28),("London", 22),("Beijing", 32)]
    byname = lambda data: data[0]

    x = sorted(temps,key=byname)
    print(x)

    x = sorted(temps, key=lambda data:data[1])
    print(x)

    x = sorted(temps)
    print(x)

    print(temps)

