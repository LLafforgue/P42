from .GameStrategy import GameStrategy
from .CardFactory import CardFactoryError, CardFactory


class GameEngineError(Exception):
    """For errors related to the game"""
    ErrorType = "\033[1mGameEngineError: \033[0m"
    MESSAGE = {
        'config': "Game engine is not properly configured.",
        }
    METHODES = {
        'configure': "(configure_engine)",
        'create': "(create_player)",
        'simulate': "(simulate_turn)",
        'status': "(get_engine_status)",
        'handle': "(handle_hands)",
        'report': "(get_report)"
        }

    def __init__(self,
                 message: str = 'None',
                 mehtode: str = '',
                 criteria: str = ''):
        """Initialize the GameEngineError."""
        m_methode = GameEngineError.METHODES.get(mehtode, mehtode)
        if GameEngineError.MESSAGE.get(message, 'None') != 'None':
            message = (self.ErrorType
                       + f' ({m_methode}) ' if m_methode != '' else ''
                       + self.MESSAGE[message]
                       + ' ' + criteria)
        else:
            message = (self.ErrorType
                       + f' ({m_methode}) ' if m_methode != '' else ''
                       + message)
        super().__init__(message)


class GameEngine():
    """Game orchestrator that manages the game flow and interactions."""

    def configure_engine(self,
                         factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Configure the game engine with card factory and strategy."""
        try:
            if not isinstance(factory, CardFactory):
                raise CardFactoryError("config", 'configure', 'factory')
            if not isinstance(strategy, GameStrategy):
                raise CardFactoryError("config", 'configure' 'strategy')
            self.factory = factory
            self.strategy = strategy
            self.players: dict = {}
            self.turn_count: int = 0
        except (Exception, GameEngineError) as e:
            print(e)

    def create_player(self, name: str, size_deck: int) -> None:
        """Create a player with the given name."""
        try:
            if name in self.players.keys():
                raise GameEngineError("Player already exists.", 'create')
            self.players[name] = {
                'hand': [],
                'battlefield': [f'{name}']
            }
            self.players[name].update(
                self.factory.create_themed_deck(size_deck))
        except (Exception, GameEngineError) as e:
            print(e)

    def simulate_turn(self) -> dict:
        """Simulate a turn using the configured strategy."""
        try:
            if self.players.__len__() < 1:
                raise GameEngineError(
                    "Not enougth players in the game.",
                    'simulate')
            players = list(self.players.keys())
            player1_hand = self.players[players[0]]['hand']
            enemy_battlefield = self.players[players[1]]['battlefield']
            self.turn_count += 1
            result = self.strategy.execute_turn(player1_hand,
                                                enemy_battlefield)
            self.players[players[0]]['battlefield'].extend(
                result.get('card_played', []))
            result['card_played'] = [card.get_name()
                                     for card in result.get('card_played', [])]
            return result
        except (Exception, GameEngineError) as e:
            print(e)
            return {}

    def get_engine_status(self) -> dict:
        """Get the current status of the game engine."""
        try:
            if not hasattr(self, 'factory') or not hasattr(self, 'strategy'):
                raise GameEngineError(
                    "Game engine is not properly configured.")
            return {
                'factory': self.factory.__class__.__name__,
                'strategy': self.strategy.get_strategy_name(),
            }
        except (Exception, GameEngineError) as e:
            print(e)
            return {}

    def handle_hands(self, player: str) -> None:
        """Handle the player's hand by drawing cards from the factory."""
        try:
            if player not in self.players.keys():
                raise GameEngineError(
                    "Player does not exist.",
                    'handle')
            to_draw: int = 5 - len(self.players[player]['hand'])
            if to_draw > 0:
                for _ in range(to_draw):
                    self.players[player]['hand'].append(
                        self.players[player]['deck'].draw_card())
        except (Exception, GameEngineError) as e:
            print(e)

    def get_report(self) -> dict:
        """Generate a report of the current game state."""
        try:
            if self.players.__len__() < 1:
                raise GameEngineError("Not enougth players in the game.")
            return {
                'turn_count': self.turn_count,
                'strategy': self.strategy.get_strategy_name(),
                'players': [*self.players.keys()],
            }
        except (Exception, GameEngineError) as e:
            print(e)
            return {}
