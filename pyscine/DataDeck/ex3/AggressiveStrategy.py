from .GameStrategy import GameStrategy, GameStrategyError
from ex0 import Card, CreatureCard
from ex1 import SpellCard


class AggressiveStrategy(GameStrategy):
    """Aggressive strategy prioritizes attacking the opponent's cards."""

    def execute_turn(self, hand: list[Card | SpellCard | CreatureCard],
                     battlefield: list) -> dict:
        """Execute the turn based on the aggressive strategy."""
        turn_actions: dict = {
            'card_played': [],
            'mana_used': 0,
            'targets_attacked': [],
            'damage_dealt': 0
        }
        mana = 6
        card: Card | CreatureCard | SpellCard | None = None
        try:
            super().execute_turn(hand, battlefield)
            targets: list = self.prioritize_targets(battlefield)
            while hand and mana > 0:

                playable = [c for c in hand if c.get_cost() <= mana]

                if not playable:
                    break

                creatures = [c for c in playable
                             if isinstance(c, CreatureCard)]

                if creatures:
                    c: CreatureCard = min(creatures,
                                          key=lambda c:
                                          c.get_cost())
                    turn_actions['damage_dealt'] += c.get_attack()
                    card = c
                else:
                    spells: list[SpellCard] = [
                        c for c in playable if isinstance(c, SpellCard)
                        and c.get_effect_type()[:6] == 'damage'
                    ]
                    if spells:
                        spell: SpellCard = min(spells,
                                               key=lambda c: c.get_cost())
                        damage = [s for s in spell.get_effect().split()
                                  if s.isdigit()]
                        if damage:
                            turn_actions['damage_dealt'] += int(damage[0])
                        card = spell
                    else:
                        card = min(playable, key=lambda c: c.get_cost())
                hand.remove(card)
                mana -= card.get_cost()
                turn_actions['card_played'].append(card)
                turn_actions['mana_used'] += card.get_cost()

                if targets:
                    target = targets.pop(-1)
                    turn_actions['targets_attacked'].append(target)

        except (Exception, GameStrategyError) as e:
            print(e)

        return turn_actions

    def prioritize_targets(self, available_targets: list) -> list:
        """Prioritize targets based on the aggressive strategy."""
        targets: list[Card | str] = []

        try:
            targets = super().prioritize_targets(available_targets)
            creatures = min([t for t in targets
                             if isinstance(t, CreatureCard)],
                            key=lambda x: x.get_health(), default=None)

            if creatures:
                targets.remove(creatures)
                targets.append(creatures.get_name())

            targets = [t for t in targets if not isinstance(t, Card)]

        except (Exception, GameStrategyError) as e:
            print(e)

        return targets

    def get_strategy_name(self) -> str:
        """Get the name of the current strategy."""
        return super().get_strategy_name()


if __name__ == "__main__":
    strategy = AggressiveStrategy('aggressive')
    print(strategy.get_strategy_name().capitalize(), '\n')
    hand = [
        CreatureCard('Goblin', 2, 'common', 2, 1),
        SpellCard('Fireball', 4, 'rare', 'damage 3'),
    ]
    battlefield = [
        CreatureCard('Elf', 2, 'common', 1, 2),
        CreatureCard('Troll', 5, 'epic', 5, 4),
        'Enemy Player'
    ]
    turn_actions = strategy.execute_turn(hand, battlefield)
    print(turn_actions)
