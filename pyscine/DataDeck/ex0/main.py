from .CreatureCard import CreatureCard


def main() -> None:
    """"""
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:")

    print("\nCreatureCard Info:")
    hulk = CreatureCard("hulk", 5, 'rare', 12, 30)
    print(hulk.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {hulk.is_playable(6)}")
    print(f"Play result: {hulk.play({'mana_used': 6})}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", hulk.attack_target("Gobelin Warrior"))

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {hulk.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
