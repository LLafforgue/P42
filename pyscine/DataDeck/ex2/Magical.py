from abc import ABC, abstractmethod


class MagicalError(Exception):
    """For errors related to magical actions."""
    ErrorType = "\033[1mMagicalError: \033[0m"

    def __init__(self, args: str):
        message = self.ErrorType + args
        super().__init__(message)


class Magical(ABC):
    """Template for cards that have magical effects."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast the card's magical effect on a target."""
        if type(spell_name) is not str:
            raise MagicalError("Spell name has to be a string!")
        if type(targets) is not list or not all(type(t) is str
                                                for t in targets):
            raise MagicalError("Targets have to be a list of strings!")
        return {}

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Channel mana to empower the card's effects."""
        if type(amount) is not int:
            raise MagicalError("Amount of mana to channel must be an int!")
        if 0 < amount < 5:
            return {}
        else:
            raise MagicalError("Amount of mana to channel must be"
                               + " between 1 and 4 inclusive!")

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Return magic-related stats of the card."""
        pass
