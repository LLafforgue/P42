from ex0 import Card, CardError, CardType


class ArtifactCard(Card):
    """Template for artifact cards."""

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        """Initialize artifact card."""
        try:
            if type(durability) is not int or type(effect) is not str:
                raise TypeError("\033[1mError:\033[0m"
                                + " To create an ArtifactCard:\n"
                                + " -durability: int"
                                + " -effect: str")
            else:
                super().__init__(name, cost, rarity)
                self.__durability = durability
                self.__effect = effect
                self.set_type(CardType.ARTIFACT.value)
        except (TypeError, CardError, Exception) as e:
            print(e.args[0])

    def play(self, game_state: dict) -> dict:
        """Represent playing the artifact card in the game."""
        try:
            result: dict = super().play(game_state)
            mana = game_state['mana_used']
            if self.is_playable(mana):
                result.update({
                    'card_played': self.get_name(),
                    'mana_used': mana,
                    'effect': (f'Permanent: {self.__effect}')
                    })
                return result
            else:
                return {'Playable': False}
        except (Exception, CardError) as e:
            print(e.args[0])
            return {'Playable': False}

    def activate_ability(self) -> dict:
        """Activate the artifact's ability."""
        result: dict = {}
        try:
            result = {
                'name': self.get_name(),
                'ability_effect': self.__effect,
                'ability_activated': True
            }
        except Exception as e:
            print(e.args[0])
            return {'ability_activated': False}
        finally:
            return result
