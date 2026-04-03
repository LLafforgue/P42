from ex0 import CreatureCard, CardError
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck, DeckError

if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    new_Deck = Deck()
    try:
        cards = [
            CreatureCard("Fire Dragon", 5, 'rare', 12, 30),
            CreatureCard("Goblin Warrior", 2, 'common', 3, 5),
            CreatureCard("Goblin Warrior", 2, 'common', 3, 5),
            CreatureCard("Elven Archer", 3, 'common', 4, 6),
            CreatureCard("Elven Archer", 3, 'common', 4, 6),
            ArtifactCard("Helmet of Valor", 1, 'rare', 5, "+5 health"),
            ArtifactCard("Sword of Flames", 3, 'legendary', 3, "+3 attack"),
            SpellCard("Fireball", 4, 'common', "Deal 3 damage to target"),
            SpellCard("Fireball", 4, 'common', "Deal 3 damage to target"),
            SpellCard("Fireball", 4, 'common', "Deal 3 damage to target"),
            SpellCard("Healing Light", 2, 'epic', "heal"),
            SpellCard("Strength Buff", 3, 'common', "buff"),
        ]
    except (CardError, Exception) as e:
        print(e)

    for card in cards:
        try:
            new_Deck.add_card(card)
        except Exception as e:
            print(e)

    print('\033[1mDeck stats:\033[0m')
    for k, v in new_Deck.get_deck_stats().items():
        print(k.capitalize(), ':')
        print('-', v)

    new_Deck.shuffle()

    print("Drawing and playing cards:\n")
    for _ in range(3):
        try:
            drew = new_Deck.draw_card()
            print("\nDrew:", drew.get_name(), f"({drew.get_type()})")
            print('Play result:', drew.play({'mana_used': drew.get_cost()}))
        except (Exception, DeckError) as e:
            print(e)

    print("\nPolymorphism in action:"
          + " Same interface, different card behaviors!")
