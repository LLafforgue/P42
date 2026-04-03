from .CardFactory import CardFactory, CardFactoryError
from ex0 import Card
from ex1 import Deck
import random
from enum import Enum


class FantasyType(Enum):
    """Enum for cards types."""

    CREATURES = {'dragon', 'goblin'}
    SPELLS = {'fireball', 'lightning'}
    ARTIFACTS = {'ring'}


class FantasyCardFactory(CardFactory):
    """Factory for creating fantasy-themed cards."""

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a creature card with the given name or power level."""
        try:
            return super().create_creature(name_or_power)
        except (Exception, CardFactoryError) as e:
            print(e)
            return self.create_creature(random.choice(
                list(FantasyType.CREATURES.value)))

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a spell card with the given name or power level."""
        return super().create_spell(name_or_power)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create an artifact card with the given name or power level."""
        return super().create_artifact(name_or_power)

    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck of the given size."""
        try:
            deck = {'deck': Deck()}
            if type(size) is not int or size <= 0:
                raise CardFactoryError("invalid_deck_size")
            else:
                for _ in range(size):
                    card = random.choice(['creature', 'spell', 'artifact'])
                    if card == 'creature':
                        name = random.choice(
                            list(FantasyType.CREATURES.value))
                        deck['deck'].add_card(self.create_creature(name))
                    elif card == 'spell':
                        deck['deck'].add_card(self.create_spell(
                            random.choice(list(FantasyType.SPELLS.value))
                        ))
                    else:
                        deck['deck'].add_card(self.create_artifact(
                            random.choice(list(FantasyType.ARTIFACTS.value))
                        ))
            return deck
        except (Exception, CardFactoryError) as e:
            print(e)
            return {}

    def get_supported_types(self) -> dict:
        """Return a dictionary of supported card types."""
        return {
            'creature': {x.capitalize() for x in FantasyType.CREATURES.value},
            'spell': {x.capitalize() for x in FantasyType.SPELLS.value},
            'artifact': {x.capitalize() for x in FantasyType.ARTIFACTS.value}
        }


if __name__ == "__main__":

    factory = FantasyCardFactory()
    print("== Fantasy Card Factory ==\n")
    print("Available types:", factory.get_supported_types(), "\n")
    themed_deck = factory.create_themed_deck(100)
    print("Themed deck created with 100 cards:")
    print(f"Deck size: {len(themed_deck['deck'].cards)}")
