import sys
from ex0 import Card, CardError, CardType
from ex2 import Combatable
from .Rankable import Rankable


class TournCardError(Exception):
    """Problems related to TournamentCard actions."""
    ErrorType = "\033[1mTournamentCardError: \033[0m"
    MESSAGES = {
        'init': ("Failed in card initialization:\n"
                 + "-'rate' must be an integer (0 < rate < 2000)\n"
                 + "-'heat', 'health' and 'armor' must be integers"
                 + "-'id' must be a string"),
        'play_01': 'game_state need a target (str) key',
        'play_02': 'gane_state need a '
    }

    def __init__(self, m: str, function: str = '') -> None:
        """Initialize the TournamentCardError with a message."""
        func = f' ({function}) ' if function != '' else ''
        if m in TournCardError.MESSAGES:
            message = (TournCardError.ErrorType
                       + func
                       + TournCardError.MESSAGES[m])
        else:
            message = (TournCardError.ErrorType
                       + func
                       + m)
        super().__init__(message)


class TournamentCard(Card, Combatable, Rankable):
    """Cards played in the tournament plateform."""

    def __init__(self, name: str, cost: int, rarity: str,
                 rate: int, damages: int, health: int,
                 armor: int, id_c: str) -> None:
        """Initialize the tournament card."""
        try:
            super().__init__(name, cost, rarity)
            self.wins = 0
            self.losses = 0
            self.rate = rate
            self.__type = CardType.TOURNAMENT.value
            if (type(rate) is int and 0 < rate < 2000
               and type(damages) is int
               and type(health) is int
               and type(armor) is int
               and type(id_c) is str):
                self.rate = rate
                self.damages = damages
                self.health = health
                self.armor = armor
                self.id_c = id_c.lower().capitalize()
            else:
                raise TournCardError('init')
        except (CardError, TournCardError) as e:
            print(e, file=sys.stderr)

    def attack(self, target: str | Card) -> dict:
        """Simulate an attack on a target and return the result."""
        result: dict = {}
        try:
            result = super().attack(target)
            result['damages'] = self.damages
        except (Exception) as e:
            print(e, file=sys.stderr)
        finally:
            return result

    def defend(self, incoming_damage: int) -> dict:
        """Simulate defending against incoming damage."""
        result: dict = {}
        try:
            result = super().defend(incoming_damage)
            result['damages'] = (0 if incoming_damage - self.armor <= 0
                                 else incoming_damage - self.armor)

        except (Exception) as e:
            print(e)
        finally:
            return result

    def play(self, game_stat: dict) -> dict:
        """Simulate playing the card in a game state."""
        result: dict = {}
        try:
            if not isinstance(game_stat, dict):
                raise CardError('game_state should be a dict')
            if type(game_stat.get('target', None)) is not TournamentCard:
                raise TournCardError('play_01', 'play')
            else:
                target: TournamentCard = game_stat['target']
                if (target.attack(self.get_name())).get('damages', None):
                    damages = target.attack(self.get_name())['damages']
                    if type(damages) is int and damages >= 0:
                        result['damages_get'] = self.defend(damages)['damages']
                        self.health -= (result['damages_get']
                                        if result['damages_get'] <= self.health
                                        else self.health)
            result['health'] = self.health
        except (Exception, CardError, TournCardError) as e:
            print(e, file=sys.stderr)
        finally:
            return result

    def get_card_info(self) -> dict:
        """Return a dictionary containing the card's information."""
        try:
            return super().get_card_info()
        except (Exception) as e:
            print(e, file=sys.stderr)
            return {}

    def get_combat_stats(self) -> dict:
        """Return a dictionary containing the card's combat statistics."""
        try:
            return super().get_combat_stats()
        except (Exception) as e:
            print(e, file=sys.stderr)
            return {}

    def calculate_rating(self) -> int:
        """Calculate the card's rating based on its wins and losses."""
        rate: int = 0
        try:
            rate = super().calculate_rating() * 16
            if rate == 0:
                if self.health == 0:
                    self.rate -= 50
            self.rate += rate
            return rate
        except (Exception) as e:
            print(e, file=sys.stderr)
            return 0

    def update_losses(self, losses: int) -> None:
        """Update the card's losses and adjust the rating accordingly."""
        try:
            super().update_losses(losses)
            self.losses += losses
        except (Exception) as e:
            print(e, file=sys.stderr)

    def update_wins(self, wins: int) -> None:
        """Update the card's wins and adjust the rating accordingly."""
        try:
            super().update_wins(wins)
            self.wins += wins
        except (Exception) as e:
            print(e, file=sys.stderr)

    def get_rank_info(self) -> dict:
        """Return a dictionary containing the card's rank information."""
        infos: dict = {}
        infos['Interfaces'] = [k.__name__ for k in self.__class__.__mro__][1:4]
        infos['Rating'] = self.rate
        infos['Record'] = f'{self.wins} - {self.losses}'
        return infos
