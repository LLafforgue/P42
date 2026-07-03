from ex0 import CardError, Card, CardType
from .Combatable import Combatable, CombatError
from .Magical import Magical, MagicalError
from enum import Enum


class AttackType(Enum):
    MELEE = 'melee'
    DISTANCE = 'distance'
    SINGLE = 'single'


class EliteError(Exception):
    """For errors related to elite card actions."""
    ErrorType = "\033[1mEliteError: \033[0m"
    MESSAGES = {
        "invalid_init": ("To create an EliteCard:\n -name: str\n"
                         + " -cost: int\n -rarity: str\n -attack: "
                         + "int\n -mana_res: int\n -att_type: str"),
        "invalid_play": ("Needs a target (str) to attack "
                         + "or targets (list[str]) and a spell (str)"),
        "invalid_spell": ("Not Enougth mana in you reserve!\n"
                          + "You have to channel!")
    }

    def __init__(self, args: str):
        message = self.ErrorType + self.MESSAGES.get(args, "Unknown error")
        super().__init__(message)


class EliteCard(Card, Combatable, Magical):
    """Template for elite cards, which are both combatable and magical."""

    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, mana_res: int,
                 attack_type: str) -> None:
        """"""
        super().__init__(name, cost, rarity)
        if type(attack) is int \
           and type(mana_res) is int \
           and type(attack_type) is str:
            self.__attack = attack
            self.__mana_reserv = mana_res
            self.__att_type = attack_type \
                if attack_type in AttackType.__members__ \
                else AttackType.SINGLE.value
            self.__health = 5
            self.__type = CardType.ELITE.value
        else:
            raise EliteError('invalid_init')

    def play(self, game_state: dict) -> dict:
        """Represent playing the elite card in the game."""
        try:
            result: dict = super().play(game_state)
            mana = game_state['mana_used']

            if self.is_playable(mana):

                spell = game_state.get('spell', 'None')
                targets = game_state.get('targets', [])

                if spell != 'None' \
                   and len(targets) and mana == 4:

                    result = {'spell': self.cast_spell(spell, targets)}

                elif game_state.get('target', None) \
                        and type(game_state.get('target')) is str:

                    result = {
                        'attack': self.attack(game_state.get('target', 'None'))
                        }
                    if result['attack']['combat_resolved']:
                        result.update({
                            'defend': self.defend(result['attack']['damage'])
                            })

                else:
                    raise EliteError('invalid_play')

                return result

            else:
                return {'Playable': False}
        except (Exception, CardError, CombatError, MagicalError, EliteError) \
                as e:
            print(e)
            return {'Error': e.args[0], 'Playable': False}

    def attack(self, target: str) -> dict:
        """Attack a target creature or player."""
        result: dict = {}

        try:
            super().attack(target)
            result.update({
                'attacker': self.get_name(),
                'target': target,
                'damage': self.__attack,
                'combat_type': self.__att_type,
                'combat_resolved': True
            })

        except (Exception, CombatError) as e:
            print(e.args[0])
            return {'combat_resolved': False}

        finally:
            return result

    def defend(self, incoming_damage: int) -> dict:
        result: dict = {}
        try:
            super().defend(incoming_damage)
            self.__health -= incoming_damage - 3
            result = {
                'defender': self.get_name(),
                'damage_taken': (f'{(incoming_damage - 3):+}'),
                'damage_blocked': 3,
                'still_alive': self.__health >= 0
            }
        except (Exception, CombatError) as e:
            print(e.args[0])
            return {'still_alive': self.__health >= 0}
        finally:
            return result

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on the given targets."""
        result: dict = {}

        try:
            if self.__mana_reserv > 4:
                super().cast_spell(spell_name, targets)
                self.__mana_reserv -= 4
                result = {
                    'caster': self.get_name(),
                    'spell_cast': spell_name,
                    'targets': targets,
                    'mana_used': 4,
                    'spell_resolved': True
                }
            else:
                raise EliteError('invalid_spell')
        except (Exception, MagicalError, EliteError) as e:
            print(e)
            return {
                'Error': e.args[0],
                'spell_resolved': False
                }
        finally:
            return result

    def channel_mana(self, amount: int) -> dict:
        """Channel mana to empower the card's effects."""
        result: dict = {}
        try:
            super().channel_mana(amount)
            if type(amount) is not int:
                raise EliteError("invalid_channel")
            self.__mana_reserv += amount
            result = {
                'channeled': amount,
                'total_mana': self.__mana_reserv,
                'channel_successful': True
            }
        except (Exception, MagicalError, EliteError) as e:
            print(e.args[0])
            return {'channel_successful': False}
        finally:
            return result

    def get_magic_stats(self) -> dict:
        """Return magic-related stats of the card."""
        result: dict = {}
        try:
            result = {
                'name': self.get_name(),
                'magic_power': self.__mana_reserv
            }
        except Exception as e:
            print(e.args[0])
            return {}
        finally:
            return result

    def get_combat_stats(self) -> dict:
        """Return combat-related stats of the card."""
        result: dict = {}
        try:
            result = {
                'name': self.get_name(),
                'attack': self.__attack,
                'health': self.__health,
                'attack_type': self.__att_type
            }
        except Exception as e:
            print(e.args[0])
            return {}
        finally:
            return result
