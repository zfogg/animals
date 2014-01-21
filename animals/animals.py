import random

from .types import types


def randomSample(xs, n):
    return random.sample(xs, n)

def qAndA(type_, nmin, nmax):
    print("Choose number of {0} ({1} to {2}):".format(
        type_, nmin, nmax))

    n = int(raw_input(), 10)
    n = min(n, nmax)
    n = max(n, nmin)

    print("{0}\n".format(randomSample(types[type_], n)))


