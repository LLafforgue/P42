#!/usr/bin/env python3
from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not (callable(spell1) and callable(spell2)):
        raise ValueError("Spells must be callables")

    return lambda *args, **kwargs: ((spell1(*args, **kwargs),
                                     spell2(*args, **kwargs)))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not (callable(base_spell)):
        raise ValueError("base_spell must be callables")

    return_typ = [*base_spell.__annotations__.values()][-1]
    if return_typ != int:
        raise TypeError(f"{base_spell.__name__} should return an integer !")
    return lambda x: base_spell(x) * multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not (callable(condition) and callable(spell)):
        raise ValueError("Spell and Condition must be callables")

    param_2 = [*spell.__annotations__.values()][:-1]
    param_1 = [*condition.__annotations__.values()][:-1]

    if (not param_1 != param_2 or len(param_1) > 1):
        raise TypeError("Callables must take exactly one same parameter.")
    return lambda x: spell(x) if condition(x) else "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    for s in spells:
        if not callable(s):
            raise TypeError("All spells must be callable!")
    return lambda x: [s(x) for s in spells]


if __name__ == "__main__":

    def spell1(x: str) -> str:
        return f'Heat {x}!'

    def spell2(b: str) -> str:
        return f'Heal {b}!'

    def spell3(t: str) -> str:
        return f'Create {t}!'

    def damage(d: int = 10) -> int:
        return d

    def target_condition(target: str) -> bool:
        return target in {'Dragon', 'Mage', 'Wizard'}

    def damage_condition(d: int) -> bool:
        return d > 10

    print("\033[4mTesting spell combiner...\033[0m")
    try:
        combined = spell_combiner(spell1, spell2)
        print(combined('Dragon'))
    except (TypeError, ValueError) as e:
        print(e)

    print("\n\033[4mTesting power amplifier...\033[0m")
    try:
        bad_amplif = power_amplifier(spell3, 3)
    except (TypeError, ValueError) as e:
        print(e)

    try:
        mage_amplif = power_amplifier(damage, 3)
        print(f"Original: 5, Amplified:\033[36m {mage_amplif(5)}\033[0m")

        print("\n\033[4mTesting conditional caster...\033[0m")
        print("List of valid targets: {'Dragon', 'Mage', 'Wizard'}")
        caster = conditional_caster(target_condition, combined)
        print("Target 'Mage':\033[36m", caster('Mage'), "\033[0m")
        print("Target 'Snake':\033[31m", caster('Snake'), "\033[0m")
        print("\n\033[4mTesting spell sequence...\033[0m")
        sequence = spell_sequence([
            caster,
            spell_combiner(spell3, combined),
            target_condition]
        )
        print("-", "\n- ".join([
            f"{fun}: {r}"
            for fun, r in zip(
                ['caster', 'spell_combiner', 'target_condition'],
                sequence('Wizard'))
                ]))
    except (TypeError, ValueError, AttributeError) as e:
        print(e)
