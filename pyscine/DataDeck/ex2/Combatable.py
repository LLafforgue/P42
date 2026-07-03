from abc import ABC, abstractmethod
from ex0 import Card


class CombatError(Exception):
    """For errors related to combat actions."""
    ErrorType = "\033[1mCombatError: \033[0m"

    def __init__(self, args: str):
        message = self.ErrorType + args
        super().__init__(message)


class Combatable(ABC):
    """Template for cards that can engage in combat."""

    @abstractmethod
    def attack(self, target: str | Card) -> dict:
        """Attack another combatable card."""
        if not isinstance(target, str | Card):
            raise CombatError("Target has to be a string or a Card!")
        return {}

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend against an incoming attack."""
        if type(incoming_damage) is not int:
            raise CombatError("Incoming damage has to be an integer!")
        return {}

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Return combat-related stats of the card."""
        return {}
