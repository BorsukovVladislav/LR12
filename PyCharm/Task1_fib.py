#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


def fib_iter(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


def fib_recurse(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recurse(n - 2) + fib_recurse(n - 1)


@lru_cache
def fib_rec_lru(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec_lru(n - 2) + fib_rec_lru(n - 1)


if __name__ == '__main__':
    print("Время, затраченное на итеративную версию")
    print(f'{timeit.timeit(lambda: fib_iter(15), number=10000)},\n')
    print("Время, затраченное на рекурсивную версию")
    print(f'{timeit.timeit(lambda: fib_recurse(15), number=10000)},\n')
    print("Время, затраченное на рекурсивную версию с lru_cache")
    print(timeit.timeit(lambda: fib_rec_lru(15), number=10000))
