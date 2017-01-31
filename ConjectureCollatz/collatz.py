import os

_cache = {1: 1}


def optimization(function):
    def cache(n, steps=0, cached=True):
        if n in _cache and cached:
            return _cache[n] + 1

        else:
            _steps = function(n, steps=0)
            _cache[n] = _steps
            return _steps + steps

    return cache


@optimization
def collatz(n, steps=0):
    steps += 1

    if n <= 1:
        return steps

    elif n % 2 == 0:
        return collatz(n / 2, steps=steps)

    else:
        return collatz((n * 3) + 1, steps=steps)


def run(number):
    biggest_steps = {"number": 0, "steps": 0}

    for n in range(number):
        steps = collatz(n)
        if steps > biggest_steps['steps']:
            biggest_steps['number'] = n
            biggest_steps['steps'] = steps

    without_cache = {
        "number": biggest_steps['number'],
        "steps": collatz(biggest_steps['number'], cached=False)
    }

    print('Solution with cache: {}'.format(biggest_steps))
    print('Solution without cache: {}'.format(without_cache))
    print('Amunt of numbers in cache: {}'.format(len(_cache)))

if __name__ == '__main__':
    number = int(os.environ.get('NUMBER', None))
    run(number + 1)
