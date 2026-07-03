from functools import reduce, partial, lru_cache, singledispatch
from operator import mul, add, le
from typing import Callable, Any
import timeit


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation.lower() == 'add':
        return reduce(add, spells)
    elif operation.lower() == 'multiply':
        return reduce(mul, spells)
    elif operation.lower() == 'max':
        return reduce(lambda a, b: b if le(a, b) else a, spells)
    elif operation.lower() == "min":
        return reduce(lambda a, b: a if le(a, b) else b, spells)
    else:
        return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire_enchant': partial(base_enchantment, **{
            'element': 'fire',
            'power': 50
            }),
        'ice_enchant': partial(base_enchantment, **{
            'element': 'ice',
            'power': 50
            }),
        'lightning_enchant': partial(base_enchantment, **{
            'element': 'lightning',
            'power': 50
            }),
        }


@lru_cache(None)
def memoized_fibonacci(n: int) -> int:
    a, b = 0, 1
    if n > 0:
        for _ in range(n):
            a, b = b, a + b
        return a
    else:
        return 0


@lru_cache(None)
def memoized_fibonacci_rec(n: int) -> int:
    if n > 1:
        return memoized_fibonacci_rec(n - 2) + memoized_fibonacci_rec(n - 1)
    elif n == 1:
        return 1
    else:
        return 0


def spell_dispatcher() -> Callable:
    @singledispatch
    def dispatcher(spell: Any) -> None:
        raise ValueError("Unknown spell type!")

    @dispatcher.register(int)
    def _(spell: int) -> None:
        print(f"Damage spell: {spell} points of damage.")

    @dispatcher.register(str)
    def _(spell: str) -> None:
        print(f"Enchantment cast: {spell}.")

    @dispatcher.register(list)
    def _(spell: list) -> None:
        print("Casting multiple spells:")
        for s in spell:
            print("  - ", end='')
            dispatcher(s)

    return dispatcher


if __name__ == "__main__":
    print("\n\033[1m=== Test of spell reducer ===\033[0m")
    print("Test with", [1, 2, 3, 4])
    print("- Sum:", spell_reducer([1, 2, 3, 4], "add"))
    print("- Product:", spell_reducer([1, 2, 3, 4], "multiply"))
    print("- Max:", spell_reducer([1, 2, 3, 4], "max"))
    print("- Min:", spell_reducer([1, 2, 3, 4], "min"))

    print("\n\033[1m=== Test of partial enchanter ===\033[0m")

    def spells(power: int, element: str, target: str) -> str:
        return "{} spell did {} damages to \033[1m{}\033[0m".format(
            element.capitalize(),
            power,
            target.capitalize())
    targets = ['snowman', 'dracoloss', 'leviator']
    print("\n".join(
        [f(target=t) for f, t in zip(partial_enchanter(spells).values(),
                                     targets)]
    ))

    print("\n\033[1m=== Test of memoized fibonacci ===\033[0m")
    print("Fib(10):", memoized_fibonacci(10))
    print("\033[4mInterest of @lru_cache\033[0m")
    print("- Time for Fib(1000) -> ", end=' ')
    print(f"{timeit.timeit(
        lambda: memoized_fibonacci(1000),
        globals=globals(),
        number=10
        ) * 1000:.3f} ms")
    print("- Time for recalculation of Fib(1000) -> ", end=' ')
    print(f"{timeit.timeit(
        lambda: memoized_fibonacci(1000),
        globals=globals(),
        number=10
        ) * 1000:.3f} ms")
    print("\033[32mCache is efficient\033[0m")
    print("- Time for Fib(1001) -> ", end=' ')
    print(f"{timeit.timeit(
        lambda: memoized_fibonacci(1001),
        globals=globals(),
        number=10
        ) * 1000:.3f} ms")
    print("\033[35mCache could be more efficient with recursion\033[0m")
    print("Time for Fib_rec(1000) ->", end=' ')
    print(f"{timeit.timeit(
        lambda: memoized_fibonacci_rec(1000),
        globals=globals(),
        number=10
        ) * 1000:.3f} ms")
    print(f"Time for Fib_rec(1001) -> {timeit.timeit(
        lambda: memoized_fibonacci_rec(1001),
        globals=globals(),
        number=10
        ) * 1000:.3f} ms!")

    print("\n\033[1m=== Test of spell dispatcher ===\033[0m")
    spell_list: list = [
        'Ice',
        5,
        ['Fire ball', 10, 10.5]
        ]
    dispatch = spell_dispatcher()
    for s in spell_list:
        try:
            dispatch(s)
        except ValueError as e:
            print("\033[30m", end='')
            print(e)
            print("\033[0m")
