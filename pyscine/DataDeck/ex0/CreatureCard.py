from .Card import Card, CardError, CardType


class CreatureCard(Card):
    """Template for creature cards."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        """Initialize creature card."""
        try:
            if type(attack) is not int or type(health) is not int:
                raise TypeError("\033[1mError:\033[0m"
                                + " To create a CreatureCard:\n -attack: int\n"
                                + " -health: int")
            else:
                super().__init__(name, cost, rarity)
                self.__attack = attack
                self.__health = health
                self.set_type(CardType.CREATURE.value)
        except (TypeError, CardError, Exception) as e:
            print(e.args[0])

    def play(self, game_state: dict) -> dict:
        """Represent playing the creature card in the game."""
        try:
            result: dict = super().play(game_state)
            mana = game_state['mana_used']
            if self.is_playable(mana):
                result.update({
                    'name': self.get_name(),
                    'mana_used': mana,
                    'effect': 'Creature summoned to battlefield'
                    })
                return result
            else:
                return {'Playable': False}
        except (Exception, CardError) as e:
            print(e.args[0])
            return {'Playable': False}

    def attack_target(self, target: str) -> dict:
        """Attack a target creature or player."""
        result: dict = {}
        try:
            if type(target) is str:
                result = {'target': target}
            else:
                print('target must be a string')
                return {'combat_resolved': False}
            result.update({
                'attacker': self.get_name(),
                'damage_dealt': self.__attack,
                'combat_resolved': True
            })
        except Exception as e:
            print(e)
        finally:
            return result

    def get_attack(self) -> int:
        """Get the attack value of the creature."""
        return self.__attack

    def get_health(self) -> int:
        """Get the health value of the creature."""
        return self.__health
