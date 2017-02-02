# -*- coding: utf-8 -*-

import os

_cache = {}


def optimization(function):
    def cache(n, cached=True):
        if not cached:
            return function(n, cached=cached)

        if n in _cache and cached:
            return _cache[n]

        else:
            _cache[n] = function(n, cached=cached)
            return _cache[n]

    return cache


@optimization
def collatz(n, **kwargs):
    if n <= 1:
        return 1

    elif n % 2 == 0:
        return collatz(n / 2, **kwargs) + 1

    else:
        return collatz((n * 3) + 1, **kwargs) + 1


def run(max_number):
    _number = 0
    _steps = 0

    for n in range(max_number):
        steps = collatz(n)
        if steps > _steps:
            _number = n
            _steps = steps

    print('Solution with cache: number = {0}, steps = {1}'.format(_number, _steps))
    print('Amunt of numbers in cache: {}'.format(len(_cache)))

    return _number, _steps

if __name__ == '__main__':
    number = int(os.environ.get('NUMBER', None))
    run(number + 1)
