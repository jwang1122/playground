def f(a, b, /, c, d, *, e, f):
    """
    a,b are positional-only, c,d can be positional or keyword
    e and f are required to be keyword.
    / separate the position-only arguments from others
    * separage the keyword-only arguments from others
    """
    print(a, b, c, d, e, f)


if(__name__ == "__main__"):
    f(2, 4, "c", "d", e=5, f=8)
    f(4, 2, c="c", d="d", e=9, f=10)
    f(4, 2, e=9, f=10, c="c", d="d")
    f(5, 6, 4, e=7, d="d", f=10)
#    f(1, 2, 3, 4, 5, f=6) # d cannot be keyword argument
#__add__(self, value, /) # means, no keyword arguments allowed.