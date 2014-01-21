import random

from .types import types


def qAndA(type_, nmin, nmax):
    print("Choose number of {0} ({1} to {2}):".format(
        type_, nmin, nmax))

    # Get a number (in base 10) from the user.
    n = int(raw_input(), 10)
    # Ensure the number is between the min and the max.
    n = min(n, nmax)
    n = max(n, nmin)

    sample = random.sample(types[type_], n)

    print("{0}\n".format(sample))

