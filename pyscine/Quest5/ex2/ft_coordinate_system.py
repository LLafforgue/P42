import sys
from math import sqrt


def round(x: int | float, dec: int | float) -> int | float | None:
    """
    Rounds a number to a specified decimal place.

    Args:
    x (int): The number to round.
    dec (int): The number of decimal places to round to.

    Returns:
    int | float: The rounded number, either as an integer (if dec is 0)
    or a float.

    Raises:
    Exception: If the input value is invalid or the rounding process fails.
    """
    try:
        xpend = (x // (0.1**dec) + 0.5) / (10**dec)
        if (x - xpend) > 0:
            xpend = (x // (0.1**dec) + 1) / (10**dec)
        else:
            xpend = (x // (0.1**dec)) / (10**dec)
        if dec == 0:
            return int(xpend)
        return xpend
    except Exception as e:
        print(e)
        return None


def validation(string: str) -> bool:
    """
    Validates the format of a coordinate string.

    Args:
    string (str): The coordinate string to validate.

    Returns:
    bool: True if the format is valid, False otherwise.
    """
    if string.count(",") != 2 or string[-1] == ',':
        return False
    for c in string:
        valide = "0123456789.,"
        if c not in valide:
            return False
    return True


def convert(coord: tuple[str, str, str]) \
            -> tuple[int, int, int] | tuple[float, float, float] | None:
    """
    Converts a tuple of coordinate strings to integers or floats.

    Args:
    coord (tuple[str, str, str]): A tuple of 3 strings representing
    coordinates.

    Returns:
    tuple[int, int, int] | tuple[float, float, float]: The coordinates as
    integers or floats.

    Raises:
    Exception: If the coordinates are invalid or there are not exactly 3
    values.
    """
    try:
        x, y, z = coord
    except Exception:
        print("Error : 3 coordinates needed !")
        return None
    try:
        return (int(x), int(y), int(z))
    except ValueError:
        return (float(x), float(y), float(z))


def parsing(arg: str, ply: int) -> dict:
    """
    Parses the input coordinates from the command line and converts them
    into a dictionary.

    Returns:
    dict: A dictionary with player names as keys and their coordinates
    as values.
    """
    x: str
    y: str
    z: str
    players = {}
    if not validation(arg):
        raise ValueError(f"Invalid input for coordinate args{ply}: ({arg})"
                         + "(exemple: '1,2,3')")
    else:
        x, y, z = arg.split(",")
        new_arg = convert((x, y, z))
        players[f"Player {ply}"] = new_arg
    return players


def distance_calc(loc1: tuple, loc2: tuple) -> None:
    """
    Calculates and prints the Euclidean distance between two locations.

    Args:
    loc1 (tuple): The first location as a tuple of coordinates.
    loc2 (tuple): The second location as a tuple of coordinates.

    Raises:
    Exception: If the coordinates are invalid or the calculation fails.
    """
    try:
        dist = sqrt(
            (loc2[0] - loc1[0]) ** 2 + (loc2[1] - loc1[1]) ** 2 +
            (loc2[2] - loc1[2]) ** 2
        )
        print(
            f"{round(dist, 2)} units."
        )
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    players = []
    ply = 0
    for a in sys.argv[1:]:
        try:
            ply += 1
            players.append(parsing(a, ply))
        except (Exception, ValueError) as e:
            print(e)
            ply -= 1
    if len(players) > 0:
        print("\nDistance between (0, 0, 0) and player 1:")
        distance_calc((0, 0, 0), players[0]['Player 1'])
    if len(players) > 1:
        for p in players[1:]:
            print("\nDistance between player 1 and",
                  f"{[*p.keys()][0].lower()} :")
            distance_calc(players[0]['Player 1'], *p.values())
    print("\nUnpacking demonstration:")
    for p in players:
        x, y, z = p[[*p.keys()][0]]
        print(f"{[*p.keys()][0]} at x= {x}, y= {y}, z= {z}")
