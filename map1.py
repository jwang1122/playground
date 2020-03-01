def test():
    temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26),
            ("Tokyo", 27), ("New York", 28), ("London", 22), ("Beijing", 32)]

    x = map(lambda data: (data[0], round((9 / 5) * data[1] + 32, 2)), temps)

    print("06:", type(x))
    y = next(x)  # get first item
    print("08", y)
    print("09:", list(x))
