from ex0 import Card, CardError, CardType


class SpellCard(Card):
    """Template for spell cards."""

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        """Initialize spell card."""
        effect_set = {'damage', 'damages', 'heal', 'buff', 'debuff'}
        try:
            if type(effect_type) is not str:
                raise TypeError("\033[1mError:\033[0m"
                                + " An effect_type has to be a string")
            if {*effect_type.split(" ")}.intersection(effect_set):
                super().__init__(name, cost, rarity)
                self.__effect_type = effect_type
                self.set_type(CardType.SPELL.value)
                self.__used = False
            else:
                raise ValueError("\033[1mSpelError:\033[0m effect_type has to "
                                 + "be 'damage', 'heal', 'buff' or 'debuff'.")
        except (Exception, CardError, TypeError) as e:
            print(e.args[0])

    def play(self, game_state: dict) -> dict:
        """Represent playing the spell card in the game."""
        try:
            result: dict = super().play(game_state)
            mana = game_state['mana_used']
            if self.is_playable(mana):
                self.__used = True
                result.update({
                    'card_played': self.get_name(),
                    'mana_used': mana,
                    'effect': self.__effect_type
                    })
                return result
            else:
                return {'Playable': False}
        except (Exception, CardError) as e:
            print(e.args[0])
            return {'Playable': False}

    def resolve_effect(self, targets: list) -> dict:
        """Resolve the spell's effect on the given targets."""
        result: dict = {}
        try:
            if type(targets) is list and all(type(t) is str for t in targets):
                result = {
                    'card': self.get_name(),
                    'effect_type': self.__effect_type,
                    'targets': targets,
                    'effect_resolved': True
                }
            else:
                raise TypeError("\033[1mError:\033[0m targets must be a list "
                                + "of strings")
        except (Exception, TypeError) as e:
            print(e.args[0])
            return {'effect_resolved': False}
        finally:
            return result

    def get_effect_type(self) -> str:
        effect_set = {'damage', 'damages', 'heal', 'buff', 'debuff'}
        return next((w for w in self.__effect_type.split()
                     if w in effect_set), 'None')

    def get_effect(self) -> str:
        """Return the spell's effect type."""
        return self.__effect_type


# if __name__ == "__main__":
#     fire_ball = SpellCard("fire_ball", "2", 'commun', 'debuff')
#     print(fire_ball.get_card_info())
#     ice_spike = SpellCard("ice_spike", 2, 'commun', 'burnt')
#     print(ice_spike.get_card_info())
#     grav = SpellCard("grav", 2, 'commun', 5)
#     print(grav.get_card_info())
