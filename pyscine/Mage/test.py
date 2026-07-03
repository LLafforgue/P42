from functools import partial
import operator

def trace(fn):
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)
    return wrapped

@trace
def triple(x):
    return 3 * x

x = triple(10)
print(x)

function = lambda y: y + 2
print((lambda x: x * (function)(x))(5))

def log(level, type, item, message):
    print('[{}]<{}>({}): {}'.format(level.upper(), type, item, message))

log('warning', 'foo', 'bar', 'baz')

mul_5 = partial(operator.mul, 5)
print(mul_5(3))
print(mul_5('z'))
warning = partial(log, 'warning')
print(warning('overflow', 100, 'number is too large'))

def plus(x: int, y: int) -> int:
    return x + y


x_sub_5 = partial(plus, y=-5)
print(x_sub_5(3)) # >>8
plus_1 = partial(plus, 1)
print(plus_1(3)) # >>4

from operator import le
from functools import wraps

def mon_decorateur(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Avant")
        return func(*args, **kwargs)
    return wrapper

@mon_decorateur
def ma_fonction(name: str) -> str:
    """Ma docstring"""
    return "Bravo " + name.capitalize()

print(ma_fonction.__name__)  # "ma_fonction"
print(ma_fonction.__wrapped__("ludo"))
print(ma_fonction("ludo"))
print(le(5,6))
