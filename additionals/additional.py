"""
This module contains iterator, decorator, generator
and context manager examples
"""
import time
import random


def fib_gen() -> int:
    """
    Generator function  that returns fibonacci numbers
    :returns: int
        elements of fib sequence

    """
    previous = 0
    next_num = 1
    while True:
        yield previous + next_num
        next_num, previous = previous + next_num, next_num


a = fib_gen()
for _ in range(10):
    print(next(a))


def time_check(func):
    """
    Decorator that allows trace time for function running
    """
    def wrapper(param: int):
        start = time.monotonic()
        func(param)
        stop = time.monotonic()
        print(f"time spend: {stop - start}")
    return wrapper


@time_check
def indexed_fib(index: int) -> int:
    """
    Function generates fib number whose index is given as argument
    """

    gen = fib_gen()
    for _ in range(index + 1):
        next(gen)


indexed_fib(70000)


class CatNameIter:
    """
    Class that generates cat name. Only for male cats.
    """
    def __init__(self, count):
        with open("cat_names.txt") as file:
            temp = file.readlines()
            self.cat_names = temp
            file.close()
        self.count = count
        self.names = []
        for _ in range(self.count):
            self.names.append(random.choice(self.cat_names))

    def _get_name(self):
        """
        Method creates generator of cat names, generator returns only specified
        in  self.count amount of names
        :return: str
        """
        if self.count > 0:
            self.count -= 1
            return self.names.pop().strip()
        raise StopIteration

    def __next__(self):
        return self._get_name()

    def __iter__(self):
        return CatNameContainer(self.count)


class CatNameContainer:
    """
    Container for iterator
    """

    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return CatNameIter(self.count)


cat = CatNameContainer(5)
for w in cat:
    print(w)

for z in cat:
    print(z)


class CatNameManager:
    """
    Class realize content manager for cat names
    """

    def __init__(self, mode):
        self.mode = mode
        self.file = None

    def __enter__(self):

        self.file = open("cat_names.txt", self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(exc_type, exc_val, exc_tb, sep="\n")


print("")
with CatNameManager('r') as manager:
    print(manager.readline())
    print(manager.readline())
