from ex0 import Card, CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
import random


class DeckError(Exception):
    """For errors related to deck management."""
    ErrorType = "\033[1mDeckError: \033[0m"
    MESSAGES = {
        "empty": "No enougth cards in your deck!"
    }

    def __init__(self, args: str):
        if args.lower() in self.MESSAGES.keys():
            message = (self.ErrorType
                       + self.MESSAGES.get(args.lower(), "Unknown error"))
        else:
            message = self.ErrorType + args
        super().__init__(message)


class Deck:
    """Template for a deck of cards."""
    def __init__(self) -> None:
        """""Initialize deck."""
        self.cards: list = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card from the deck by name."""
        i: int = 0
        try:
            while card_name != self.cards[i] and i < len(self.cards):
                i += 1
            if i >= self.cards.__len__():
                raise DeckError("Empty")
            else:
                self.cards.pop(i)
                return True
        except (Exception, DeckError) as e:
            print(e)
            return False

    def shuffle(self) -> None:
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draw a card from the top of the deck."""
        if self.cards.__len__() >= 0:
            return self.cards.pop(0)
        else:
            raise DeckError("empty")

    def get_deck_stats(self) -> dict[str, str | int | dict | set]:
        """Return statistics about the deck."""
        try:
            if self.cards.__len__() >= 0:
                creature_cards = sum(1 for cc in self.cards
                                     if type(cc) is CreatureCard)
                spell_cards = sum(1 for _ in self.cards
                                  if type(_) is SpellCard)
                artifactf_cards = sum(1 for ac in self.cards
                                      if type(ac) is ArtifactCard)
                cards = {n.get_name() for n in self.cards}
                deck_info: dict = {}
                for name in cards:
                    nbr = sum(1 for _ in self.cards
                              if _.get_name() == name)
                    deck_info[name] = nbr
                total_mana = sum(mana.get_cost() for mana in self.cards)

                return {
                    "nbr_cards": len(self.cards),
                    "articfacts": artifactf_cards,
                    "creatures": creature_cards,
                    "spells": spell_cards,
                    "deck": deck_info,
                    "mana": ("total_cost: "
                             + f"{total_mana} mana(s)"
                             + " - avg_cost: "
                             + f"{(total_mana/len(self.cards)):.2f}")
                }
            else:
                raise DeckError("empty")
        except (Exception, DeckError) as e:
            print(e)
            return {}


if __name__ == "__main__":
    deck_ll = Deck()
    try:
        deck_ll.add_card(CreatureCard('dragon', 5, 'rare', 10, 20))
        deck_ll.add_card(ArtifactCard('helmet', 1, 'common', 5, '+5 health'))
        deck_ll.add_card(ArtifactCard('helmet', 1, 'common', 5, '+5 health'))
    except (DeckError) as e:
        print(e)
    print(deck_ll.get_deck_stats())
