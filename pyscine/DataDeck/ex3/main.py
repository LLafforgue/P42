from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine
from ex0 import CreatureCard


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy\n")
    engine = GameEngine()

    engine.configure_engine(FantasyCardFactory(),
                            AggressiveStrategy('aggressive'))
    print("Available types", engine.factory.get_supported_types())

    print("\nCreating players...")
    engine.create_player('player1', 20)
    engine.create_player('Enemy Player', 20)
    print("\nSimulating aggressive turn...")

    # cree un battlefield with some cards from the enemy player
    creature: list = []
    while not creature and engine.players['Enemy Player']['deck'].cards:
        card = engine.players['Enemy Player']['deck'].draw_card()
        engine.players['Enemy Player']['hand'].append(card)
        if isinstance(card, CreatureCard):
            engine.players['Enemy Player']['battlefield'].append(card)
            engine.players['Enemy Player']['hand'].remove(card)

    engine.handle_hands('player1')
    turn_result = engine.simulate_turn()
    print("Turn execution:")
    print("Strategy used:", engine.strategy.get_strategy_name())
    print(turn_result)
    print("\nGame report:")
    report = engine.get_report()
    print(report)
    print('cards invocated :'
          + f'{[c.get_name() for c in engine.players['player1']['battlefield']
                if isinstance(c, CreatureCard)]
               + [c.get_name()
                   for c in engine.players['Enemy Player']['battlefield']
                   if isinstance(c, CreatureCard)]}'
          )
