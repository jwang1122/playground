from rx import Observable,of

source = of("Alpha", "Beta", "Gamma", None, "Delta", "Epsilon")

source.subscribe(
    on_next = lambda i: print("Received {0}".format(i)),
)