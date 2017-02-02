# -*- coding: utf-8 -*-

import os

_cache = {}


def collatz(n):
    if n <= 1:
        _cache[n] = 1

    elif n not in _cache:
        if n % 2 == 0:
            _next = n / 2

        else:
            _next = (n * 3) + 1

        _cache[n] = collatz(_next) + 1

    return _cache[n]


def run(max_number):
    _number = 0
    _steps = 0

    for n in xrange(0, max_number):
        steps = collatz(n)
        if steps > _steps:
            _number = n
            _steps = steps

    return _number, _steps, len(_cache)

if __name__ == '__main__':
    _number = int(os.environ.get('NUMBER', None)) + 1
    number, steps, cache = run(_number)

    print('Solution number = {0}, steps = {1}'.format(number, steps))
    print('Amunt of numbers in cache: {}'.format(cache))
