"""Spellbook module for recording spells."""
'with circular import, this module is not directly usable.'
# from ..grimoire import validate_ingredients


# def record_spell(spell_name: str, ingredients: str) -> str:
#     """Records a spell if the ingredients are valid."""
#     response: str = validate_ingredients(ingredients)
#     if response.count("INVALID"):
#         return (f"Spell rejected: {spell_name} ({response})")
#     else:
#         return (f"Spell recorded: {spell_name} ({response})")


'breaking the circular import with late import.'


def record_spell(spell_name: str, ingredients: str) -> str:
    """Records a spell if the ingredients are valid."""
    from ..grimoire import validate_ingredients
    response: str = validate_ingredients(ingredients)
    if response.count("INVALID"):
        return (f"Spell rejected: {spell_name} ({response})")
    else:
        return (f"Spell recorded: {spell_name} ({response})")


'breaking the circular import with proper import.'
# from .validator import validate_ingredients


# def record_spell(spell_name: str, ingredients: str) -> str:
#     """Records a spell if the ingredients are valid."""
#     response: str = validate_ingredients(ingredients)
#     if response.count("INVALID"):
#         return (f"Spell rejected: {spell_name} ({response})")
#     else:
#         return (f"Spell recorded: {spell_name} ({response})")
