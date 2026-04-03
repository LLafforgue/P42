from ex0 import Card
from .EliteCard import EliteCard
from .Magical import Magical
from .Combatable import Combatable

if __name__ == "__main__":
    print('=== DataDeck Ability System ===')
    print('EliteCard capabailities:')
    # print all methods of Card class
    print(f'- Card: {[method for method in dir(Card)
                      if not method.startswith("__")][1:]}')
    print(f'- Combatable: {[methid for methid in dir(Combatable)
                            if not methid.startswith("__")][1:]}')
    print(f'- Magical: {[method for method in dir(Magical)
                         if not method.startswith("__")][1:]}')

print('\nPLaying Arcane Warrior (EliteCard):')
arcane_warrior = EliteCard('Arcane Warrior', 4, 'epic', 4, 8, 'melee')
print('\nCombat phase:')
result = arcane_warrior.play({
    'mana_used': 4,
    'target': 'Enemy Minion'
})
if result.get('attack', None) and result.get('defend'):
    print('Attack result:', {r: o for r, o in result['attack'].items()
                             if r != 'combat_resolved'})
    print('Defend result:', result['defend'])

print('\nMagic phase:')
result = arcane_warrior.play({
    'mana_used': 4,
    'targets': ['Enemy1', 'Enemy2'],
    'spell': 'FireBall'
})
if result.get('spell', None):
    print('Spell cast:', result['spell'])
arcane_warrior.play({
    'mana_used': 4,
    'targets': ['Enemy1', 'Enemy2'],
    'spell': 'FireBall'
})
channel = arcane_warrior.channel_mana(3)
print("Mana channel:", {r: o for r, o in channel.items()
                        if r != 'channel_successful'})

print("\nMultiple interface implementation successful!")
