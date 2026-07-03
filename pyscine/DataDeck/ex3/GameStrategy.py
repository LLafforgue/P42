from abc import ABC, abstractmethod
from enum import Enum
from ex0 import Card


class Strategies(Enum):
    """Enum for stratgies allowed"""
    AGGRESSIVE = 'aggressive'


class GameStrategyError(Exception):
    """For errors related the strategy game"""
    ErrorType = "\033[1mGameStrategyError: \033[0m"
    MESSAGE = {
        'init': "Invalid strategy provided. Please, choose a valid strategy.",
        'execute': "Hand and battlefield must be lists.",
        'execute_h': "Hand has to contain only cards.",
        'prioritize': "Available targets must be a list of cards or names.",
        }

    def __init__(self, message: str = 'None'):
        """Initialize the GameStrategyError."""
        if GameStrategyError.MESSAGE.get(message, 'None') != 'None':
            message = self.ErrorType + self.MESSAGE[message]
        else:
            message = self.ErrorType + message
        super().__init__(message)


class GameStrategy(ABC):
    """Patern for game strategies and prioritize targets."""

    def __init__(self, strategy: str) -> None:
        """Initialize the GameStrategy with a specific strategy."""
        if strategy.lower() == Strategies.AGGRESSIVE.value:
            self.__strategy = Strategies.AGGRESSIVE.value
        else:
            raise GameStrategyError()

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute the turn based on the strategy, hand, and battlefield."""
        turn_actions: dict = {}
        if type(hand) is not list or type(battlefield) is not list:
            raise GameStrategyError("execute")
        else:
            if any(not isinstance(c, Card) for c in hand) or len(hand) == 0:
                raise GameStrategyError("execute_h")
            return turn_actions

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Get the name of the current strategy."""
        return (self.__strategy).capitalize()

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Handle target prioritization based on the strategy."""
        if type(available_targets) is not list:
            raise GameStrategyError("prioritize")
        else:
            if any(not isinstance(c, Card | str) for c in available_targets):
                raise GameStrategyError("prioritize")
            return available_targets
