from typing import ClassVar
from abc import ABC, abstractmethod
from ex0 import Card, CreatureCard
from ex1 import SpellCard, ArtifactCard, Deck
import random


class CardFactoryError(Exception):
    """For errors related to card factory actions."""

    ErrorType = "\033[1mCardFactoryError: \033[0m"

    MESSAGES = {
        "invalid_name_or_power": ("name_or_power"
                                  + " must be a string or an integer!"),
        "invalid_deck_size": "Deck size must be a positive integer!",
        "no_name_or_power": ("No card found with"
                             + " the given name or power level!")

        }

    def __init__(self, args: str) -> None:
        if args in CardFactoryError.MESSAGES:
            message = (CardFactoryError.ErrorType
                       + CardFactoryError.MESSAGES[args])
        else:
            message = CardFactoryError.ErrorType + "Unknown error"
        super().__init__(message)


class CardFactory(ABC):
    """Template for a card factory that can create different types of cards."""

    CREATURES: ClassVar[list[dict]] = [
        {
            "name": "Goblin Warrior",
            "cost": 2,
            "rarity": "common",
            "attack": 3,
            "health": 2,
        },
        {
            "name": "Elven Archer",
            "cost": 3,
            "rarity": "rare",
            "attack": 2,
            "health": 3,
        },
        {
            "name": "Orc Brute",
            "cost": 4,
            "rarity": "epic",
            "attack": 5,
            "health": 4,
        },
        {
            "name": "Fire Dragon",
            "cost": 7,
            "rarity": "legendary",
            "attack": 8,
            "health": 6,
        },
    ]

    SPELLS: ClassVar[list[dict]] = [
        {'name': 'Fireball', 'cost': 4,
         'rarity': 'common', 'effect_type': 'deal 3 damages'},
        {'name': 'Healing Touch', 'cost': 3, 'rarity': 'rare',
         'effect_type': 'heal +4 health'},
        {'name': 'Lightning Strike', 'cost': 5, 'rarity': 'epic',
         'effect_type': 'buff +2 attack'},
    ]

    ARTIFACTS: ClassVar[list[dict]] = [
        {'name': 'Sword of Valor', 'cost': 3,
         'rarity': 'common', 'durability': 2, 'effect': 'attack_boost'},
        {'name': 'mana ring', 'cost': 2,
         'rarity': 'rare', 'durability': 3, 'effect': 'mana_boost'},
        {'name': 'Amulet of Power', 'cost': 5,
         'rarity': 'epic', 'durability': 4, 'effect': 'attack_boost'},
    ]

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a creature card with the given name or power level."""
        if name_or_power is not None and \
           not isinstance(name_or_power, (str, int)):
            raise CardFactoryError("invalid_name_or_power")
        if type(name_or_power) is str:
            creature_data = [creature for creature in CardFactory.CREATURES
                             if ({*creature['name'].lower().split(' ')}
                                 & {name_or_power})]
        elif type(name_or_power) is int:
            creature_data = [creature for creature in CardFactory.CREATURES
                             if creature['attack'] == name_or_power]
        else:
            r_index = random.randint(0, len(CardFactory.CREATURES) - 1)
            return CreatureCard(**CardFactory.CREATURES[r_index])
        if len(creature_data) == 0:
            raise CardFactoryError("no_name_or_power")
        return CreatureCard(**creature_data[0])

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a spell card with the given name or power level."""
        if name_or_power is not None and \
           not isinstance(name_or_power, (str, int)):
            raise CardFactoryError("invalid_name_or_power")
        if type(name_or_power) is str:
            spell_data = [spell for spell in CardFactory.SPELLS
                          if ({*spell['name'].lower().split(' ')}
                              & {name_or_power})]
        elif type(name_or_power) is int:
            spell_data = [spell for spell in CardFactory.SPELLS
                          if spell['cost'] == name_or_power]
        else:
            r_index = random.randint(0, len(CardFactory.SPELLS) - 1)
            return SpellCard(**CardFactory.SPELLS[r_index])
        if len(spell_data) == 0:
            raise CardFactoryError("no_name_or_power")
        return SpellCard(**spell_data[0])

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create an artifact card with the given name or power level."""
        if name_or_power is not None and \
           not isinstance(name_or_power, (str, int)):
            raise CardFactoryError("invalid_name_or_power")
        if type(name_or_power) is str:
            artifact_data = [artifact for artifact in CardFactory.ARTIFACTS
                             if ({*artifact['name'].lower().split(' ')}
                                 & {name_or_power})]
        elif type(name_or_power) is int:
            artifact_data = [artifact for artifact in CardFactory.ARTIFACTS
                             if artifact['cost'] == name_or_power]
        else:
            r_index = random.randint(0, len(CardFactory.ARTIFACTS) - 1)
            return ArtifactCard(**CardFactory.ARTIFACTS[r_index])

        if len(artifact_data) == 0:
            raise CardFactoryError("no_name_or_power")
        return ArtifactCard(**artifact_data[0])

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck of the given size."""
        deck = {'deck': Deck()}
        if type(size) is not int or size <= 0:
            raise CardFactoryError("invalid_deck_size")
        else:
            for _ in range(size):
                card = random.choice(['creature', 'spell', 'artifact'])
                if card == 'creature':
                    deck['deck'].add_card(self.create_creature())
                elif card == 'spell':
                    deck['deck'].add_card(self.create_spell())
                else:
                    deck['deck'].add_card(self.create_artifact())
        return deck

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Give a dictionary of supported card types."""
        return {
            'creature': [
                creature['name'] for creature in CardFactory.CREATURES
                ],
            'spell': [
                spell['name'] for spell in CardFactory.SPELLS
                ],
            'artifact': [
                artifact['name'] for artifact in CardFactory.ARTIFACTS
                ]
            }
