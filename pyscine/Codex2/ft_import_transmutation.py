import alchemy
from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion as hulk, invisibility_potion
from alchemy.elements import create_earth

if __name__ == "__main__":
    print("\n=== Import Transmutation Mastery ===\n")
    print("Method 1 - Full module import:")
    print("alchemy.elements.create_air():", alchemy.elements.create_fire())

    print("\nMethod 2 - Specific function import:")
    print("create_earth():", create_earth())

    print("\nMethod 3 - Aliased import:")
    print("heal():", heal())

    print("\nMethod 4 - Multiple imports:")
    print("create_water():", alchemy.create_water())
    print("strength_potion():", hulk())
    print("Invisibility potion:", invisibility_potion())
