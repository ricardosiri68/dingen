import random


def generate(FactoryClass, times, args=[], kwargs={}):

    if isinstance(times, tuple):

        min_range, max_range = times
        times = random.randint(min_range, max_range)

    return (FactoryClass(*args, **kwargs) for i in range(times))
