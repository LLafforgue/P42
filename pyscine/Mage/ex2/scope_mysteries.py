from typing import Callable


def mage_counter() -> Callable:
    n: int = 0

    def count() -> int:
        nonlocal n
        n += 1
        return n
    return count


def spell_accumulator(initial_power: int) -> Callable:
    power: int = 0

    def spell(amount: int = 0) -> int:
        nonlocal power
        if power == 0:
            power += initial_power
        power += amount
        return power
    return spell


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchantment(item_name: str) -> str:
        return (enchantment_type.capitalize()
                + " "
                + item_name.capitalize())

    return enchantment


def memory_vault() -> dict[str, Callable]:
    secret_dict: dict = {}

    def store(key: str, value: str | int) -> None:
        nonlocal secret_dict
        # print('secret de store ->', id(secret_dict))
        secret_dict[key] = value

    def recall(key: str) -> str | int:
        nonlocal secret_dict
        # print('secret de recall ->', id(secret_dict))
        return secret_dict.get(key, '\033[35mMemory not found\033[0m')

    return {'store': store, 'recall': recall}


if __name__ == "__main__":

    print("\033[1m=== Test de mage counter ===\033[0m")
    count_a = mage_counter()
    count_b = mage_counter()

    print('Deux compteurs issus de `mage_counter`:',
          '\n-Compteur A :', count_a.__closure__,
          '\n-Compteur B :', count_b.__closure__)
    print("Appels :")
    print('Compteur A (1):', count_a())
    print('Compteur A (2):', count_a())
    print('Compteur B (1):', count_b())
    print('Compteur A (3):', count_a())

    print("\n\033[1m=== Test de spell accumulator ===\033[0m")
    fire_ball = spell_accumulator(10)
    thunder_bolt = spell_accumulator(20)
    print("Puissance initiale de \033[31mfire ball\033[0m:", fire_ball())
    print('Ajout de `3` de puissance a `fire ball` :', fire_ball(3))
    print('Ajout de `5` de puissance a `fire ball`:', fire_ball(5))
    print("Puissance initiale de \033[33mthunder bolt\033[0m:", thunder_bolt())
    print('Ajout de `5` de puissance a `thunder bolt` :', thunder_bolt(5))

    print("\n\033[1m=== Test de enchantement factory ===\033[0m")
    print('Creation d`enchantements \033[4mdragonesques:\033[0m')
    items = ['spell', 'spikes', 'sword']
    factory_dragon = enchantment_factory('Dragon')
    print("\n".join([factory_dragon(i) for i in items]))
    print('Creation d`enchantements de \033[4mglace\033[0m:')
    factory_ice = enchantment_factory('Ice')
    print("\n".join([factory_ice(i) for i in items]))

    print("\n\033[1m=== Test de memory vault ===\033[0m")
    Gobelin = memory_vault()
    print("Verification que les deux fonctions "
          + "ont recuperé le meme environnement.")
    print("Fonction `store`:", Gobelin['store'].__closure__)
    print("Fonction `recall`:", Gobelin['recall'].__closure__)
    print("\nEnregistrement d'une créature (name: Gobelin)")
    Gobelin['store']('name', 'Gobelin')
    print("Récuperation du nom:", Gobelin['recall']('name'))
    print("Récuperation des dommages:", Gobelin['recall']('damages'))
    Gobelin['store']('damages', 15)
    print("Oups!\nEnregistrement des dommages (damages: 15)")
    print("Récuperation des dommages:", Gobelin['recall']('damages'))
