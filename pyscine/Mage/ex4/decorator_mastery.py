from functools import wraps, partial
from typing import Callable, Any
from timeit import timeit
import random
from operator import add


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Callable:
        print(f"Casting {func.__name__}...")
        timed_func = partial(func, *args, **kwargs)
        duration = timeit(timed_func, number=1) * 1000
        print(f"Spell completed in \033[1m{duration:.3f}\033[0m ms")
        return func(*args, **kwargs)
    return wrapper


def power_validator(min_power: int) -> Callable:
    def validator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str | Callable:
            try:
                if 'power' in kwargs and kwargs['power'] <= min_power:
                    return "Insufficient power for this spell"
                if isinstance(args[0], int | float) and args[0] <= min_power:
                    return "Insufficient power for this spell"
                if isinstance(args[0], int | float) or 'power' in kwargs:
                    return func(*args, **kwargs)
                raise AttributeError("`power` must be the first"
                                     + " argument or use kwargs!")
            except (TypeError, AttributeError) as e:
                return (f"\033[35m{e.args[0]}\033[0m")
        return wrapper
    return validator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Callable | str:

            for a in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"{func.__name__.capitalize()} failed, retryng...",
                          end=' ')
                    print(f"(attempt : {a}/{max_attempts})")

            return f"Spell casting failed {max_attempts} attempts"

        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) > 2 and name.isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return ("\033[32mSuccessfully cast {} with power {}\033[0m"
                .format(spell_name, power))


if __name__ == "__main__":

    print("\n\033[1m=== Test of `spell timer` decorator ===\033[0m")

    @spell_timer
    def spell(x: int) -> int:
        b: int = 0
        for _ in range(1000):
            b = add(x, b)
        return b
    spell(1)

    print("\n\033[1m=== Test of `spell valiator` decorator ===\033[0m")
    mage = MageGuild()
    print(mage.cast_spell('Error', 20))
    print(mage.cast_spell(spell_name='Error', power=5))
    print(mage.cast_spell(spell_name='thunderbolt', power=20))

    print("\n\033[1m=== Test of `retry spell` decorator ===\033[0m")

    @retry_spell(max_attempts=3)
    def unstable_spell(target: str) -> str:
        power = random.random()*10

        @power_validator(5)
        def spell_mage(power: int, target: str = target) -> bool:
            if random.random() < 0.5:
                raise ValueError("Spell fizzled!")
            return True
        result = spell_mage(power)
        if result is True:
            return (f"Spell successfully hits {target} "
                    + f"with {int(power)} damages!")
        else:
            print("\033[1mNot enougth power:", int(power), "\033[0m")
            raise ValueError("Not enougth power")

    print(unstable_spell("dragon"))
