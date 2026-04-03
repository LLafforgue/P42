from .TournamentCard import TournamentCard, TournCardError
from ex0 import CardError


class TournamentPlateformError(Exception):
    """For errors related to the tournament plateform."""
    ErrorType = "\033[1mPlateformError: \033[0m"

    def __init__(self, m: str) -> None:
        message = TournamentPlateformError.ErrorType + m
        super().__init__(message)


class TournamentPlateform:
    """Class representing the tournament plateform."""
    def __init__(self, name: str):
        """Initialize the tournament plateform."""
        self.name = name
        self.reports: list[dict] = []
        self.cards: list[TournamentCard] = []

    def register_card(self, card: TournamentCard) -> None:
        """Register a card to the tournament plateform."""
        try:
            if type(card) is not TournamentCard:
                raise TournamentPlateformError(
                    "Only TournamentCard instances can be registered!")
            check_id = sum(1 for c in self.cards
                           if c.id_c == card.id_c.lower().capitalize())
            if check_id != 0:
                raise TournamentPlateformError(
                    f"{card.id_c} has already been registered!"
                )
            else:
                self.cards.append(card)

        except (Exception, CardError, TournCardError) as e:
            print(e)

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Simulate a match between two cards and return the result."""
        result: dict = {}
        winner: TournamentCard | None = None
        try:
            if not all(isinstance(id, str) for id in (card1_id, card2_id)):
                raise TournamentPlateformError("Card IDs should be strings!")
            card1 = next((c for c in self.cards
                          if card1_id.lower().capitalize() == c.id_c))
            card2 = next((c for c in self.cards
                          if card2_id.lower().capitalize() == c.id_c))
            if not all(isinstance(c, TournamentCard) for c in (card1, card2)):
                raise TournamentPlateformError(
                    "Cards not found with given IDs!")
            if any(c.health == 0 for c in (card1, card2)):
                raise TournamentPlateformError("No card should be KO !")
            played = (card1.play({'target': card2}),
                      card2.play({'target': card1}))
            if card2.health == 0 or card1.health == 0:
                for c in (card1, card2):
                    if c.health > 0:
                        winner = c
                        c.update_wins(1)
                    else:
                        loser = c
                        c.update_losses(1)
                end = (f'By_KO [{loser.get_name()}]'
                       if isinstance(winner, TournamentCard)
                       else 'Double KO')
            elif played[0]['damages_get'] > played[1]['damages_get']:
                winner = card2
                loser = card1
                card2.update_wins(1)
                card1.update_losses(1)
                end = 'Dammages Comparaison'
            elif played[0]['damages_get'] < played[1]['damages_get']:
                winner = card1
                loser = card2
                card1.update_wins(1)
                card2.update_losses(1)
                end = 'Dammages Comparaison'
            else:
                card1.rate += card2.rate - card1.rate
                card2.rate -= card2.rate - card1.rate
            for c in (card1, card2):
                c.calculate_rating()
            result = {
                'winner': (winner.id_c
                           if isinstance(winner, TournamentCard)
                           else 'No Winner'),
                'loser': loser.id_c,
                'winner_rating': (winner.rate
                                  if isinstance(winner, TournamentCard)
                                  else 0),
                'loser_rating': loser.rate,
                'Resolution': end
            }
            self.reports.append(result)
            return result
        except (Exception) as e:
            print(e)
            return result

    def get_leaderboard(self) -> list:
        """Return a sorted list of cards based on their ratings."""
        board = sorted(self.cards, key=lambda x: x.rate, reverse=True)
        try:
            if self.cards.__len__() <= 1:
                raise TournamentPlateformError(
                    'Not enougth cards on the plateform!')
            return [(f'{c.get_name()} - Rating: {c.rate}'
                    + f' ({c.get_rank_info()['Record']})') for c in board]
        except (Exception, TournamentPlateformError) as e:
            print(e)
            return board

    def generate_tournament_report(self) -> dict:
        """Generate a report of the tournament."""
        report: dict = {}
        try:
            if self.cards.__len__() <= 1:
                raise TournamentPlateformError(
                    'Not enougth cards on the plateform!')
            report['total_cards'] = len(self.cards)
            report['matched_played'] = len(self.reports)
            report['avg_rating'] = (sum(c.rate for c in self.cards)
                                    // len(self.cards))
            report['platform_status'] = ('active'
                                         if sum(
                                             1 for c in self.cards
                                             if c.health != 0) != 0
                                         else 'No more cards active')
            return report

        except (Exception) as e:
            print(e)
            return report
