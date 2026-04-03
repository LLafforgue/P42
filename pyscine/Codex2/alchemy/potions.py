from .elements import create_fire, create_water, create_air, create_earth


def healing_potion() -> str:
    """Brews a healing potion using fire and water elements."""
    return (f"Healing potion brewed with \033[1m{create_fire()}\033[0m"
            + f" and \033[1m{create_water()}\033[0m.")


def strength_potion() -> str:
    """Brews a strength potion using earth and fire elements."""
    return (f"Strength potion brewed with \033[1m{create_earth()}\033[0m"
            + f" and \033[1m{create_fire()}\033[0m.")


def invisibility_potion() -> str:
    """Brews an invisibility potion using air and water elements."""
    return (f"Invisibility potion brewed with \033[1m{create_air()}\033[0m"
            + f" and \033[1m{create_water()}\033[0m.")


def wisdom_potion() -> str:
    """Brews a wisdom potion using all four elements."""
    return ("Wisdom potion brewed with all elements:"
            + f" \033[1m{create_air()}\033[0m,"
            + f" \033[1m{create_earth()}\033[0m,"
            + f" \033[1m{create_fire()}\033[0m,"
            + f" \033[1m{create_water()}\033[0m.")
