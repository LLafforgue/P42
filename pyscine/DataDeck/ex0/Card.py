from abc import ABC, abstractmethod
from enum import Enum


class CardError(Exception):
    """For errors related to card creation and usage."""
    ErrorType = "\033[1mCardError: \033[0m"

    def __init__(self, args: str):
        message = self.ErrorType + args
        super().__init__(message)


class CardType(Enum):
    """Card types."""
    CREATURE = 'Creature'
    SPELL = 'Spell'
    ARTIFACT = 'Artifact'
    ELITE = 'Elite'
    TOURNAMENT = 'Tournament'
    UNTYPED = 'None'


class Rarity(Enum):
    """Card rarities."""
    COMMON = 'common'
    RARE = 'rare'
    EPIC = 'epic'
    LEGENDARY = 'legendary'


class Card(ABC):
    """Template for all cards."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """""Initialize card."""
        if isinstance(name, str) and isinstance(cost, int) \
           and isinstance(rarity, str):
            self.__name = name
            self.__cost = cost
            self.__type = CardType.UNTYPED.value
            if rarity.upper() in Rarity.__members__:
                self.__rarity = rarity
            else:
                raise CardError(f"{rarity} is not a valid rarity type"
                                + "\n -common\n -rare\n -epic\n -legendary")
        else:
            raise CardError("To create a Card:\n -name: str\n"
                            + " -cost: int\n -rarity: str")

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Represent playing the card in the game."""
        if type(game_state) is not dict:
            raise CardError("game_state has to be a dict")
        if not game_state.get('mana_used', None):
            raise CardError("game_state contain 'mana_used'!")
        if type(game_state['mana_used']) is not int:
            raise CardError("'mana_used' has to be an integer!")
        else:
            return {}

    def get_card_info(self) -> dict:
        """Return card information as a dictionary."""
        return {f'{k.rsplit("__", 1)[-1]}': vars(self)[k] for k in vars(self)}

    def is_playable(self, available_mana: int) -> bool:
        """Check if the card can be played with the given mana."""
        return available_mana >= self.__cost

    def get_name(self) -> str:
        """Return the card's name."""
        return self.__name

    def get_cost(self) -> int:
        """Return the card's mana cost."""
        return self.__cost

    def get_rarity(self) -> str:
        """Return the card's rarity."""
        return self.__rarity

    def get_type(self) -> str:
        """Return the card's type."""
        return self.__type

    def set_type(self, type: str) -> None:
        """Set the card's type."""
        self.__type = type
