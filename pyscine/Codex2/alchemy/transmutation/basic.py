from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Transmutes lead into gold using basic alchemy."""
    return (f"Lead transmuted to gold using \033[1m{create_fire()}\033[0m")


def stone_to_gem() -> str:
    """Transmutes stone into a precious gem."""
    return (f"Stone transmuted to gem using \033[1m{create_earth()}\033[0m")


if __name__ == "__main__":
    lead_to_gold()
    stone_to_gem()
