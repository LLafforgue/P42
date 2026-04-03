from abc import ABC, abstractmethod


class RankableError(Exception):
    """For errors related to rankable actions."""

    ErrorType = "\033[1mRankableError: \033[0m"
    MESSAGES = {
        "invalid_rating": "Rating must be a non-negative integer!",
        "invalid_wins_or_losses": ("Wins or losses must"
                                   + " be non-negative integers!")
    }

    def __init__(self, message: str, function: str = '') -> None:
        if message in RankableError.MESSAGES:
            message = (RankableError.ErrorType
                       + (f' ({function}) ' if function != '' else '')
                       + RankableError.MESSAGES[message])
        else:
            message = RankableError.ErrorType + message
        super().__init__(message)


class Rankable(ABC):
    """Interface for objects that can be ranked."""

    def __init__(self) -> None:
        """Initialize the Rankable object with default wins and losses."""
        self.wins: int = 0
        self.losses: int = 0

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return the rating of the object."""
        if self.wins < 0 or self.losses < 0:
            raise RankableError("invalid_wins_or_losses", 'calculate_rating')
        return self.wins - self.losses

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update the number of wins for the object."""
        if not isinstance(wins, int) or wins < 0:
            raise RankableError("invalid_wins_or_losses", 'update_wins')
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update the number of losses for the object."""
        if not isinstance(losses, int) or losses < 0:
            raise RankableError("invalid_wins_or_losses", 'update_losses')

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Return a dictionary containing the rank information."""
        pass
