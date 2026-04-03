utils = {
    "sword": {
        "values": 500,
        "types": "weapon",
        "rank": "rare"
    },
    "potion": {
        "values": 50,
        "types": "consumable",
        "rank": "common"
    }
}


alice = {}
bob = {}
players = {"Alice": alice, "Bob": bob}


def add_utils(name: str, values: int, types: str, rank: str) -> None:
    """
    Adds an item to the general inventory 'utils'.

    Args:
    name (str): The name of the item.
    values (int): The value (price) of the item in gold.
    types (str): The type of the item (e.g., 'weapon', 'consumable').
    rank (str): The rarity of the item (e.g., 'common', 'rare').
    """
    utils[name] = {
        "values": values,
        "types": types,
        "rank": rank
    }


def manage_player_inv(player: dict, inventory: dict) -> None:
    """
    Updates the inventory of an existing player.

    Args:
    player (dict): The player's current inventory.
    inventory (dict): A dictionary with item names as keys and quantities as
    values.

    Raises:
    Exception: If the player doesn't exist or the inventory has an invalid
    item.
    """
    try:
        for name, quantity in inventory.items():
            player[name] = dict(utils[name], quantity=quantity)
    except Exception as e:
        print(e)


def display_inv(player: dict) -> None:
    """
    Displays the inventory of a player.

    Args:
    player (dict): The player's inventory to display.

    Raises:
    Exception: If the player doesn't exist or the inventory is empty.
    """
    if not player:
        raise ValueError(f"{player} is not a player")
    else:
        for invent in player:
            a_inv = player[invent]
            print(f"{invent} ({a_inv["types"]}, {a_inv["rank"]}): "
                  + f"{a_inv["quantity"]}x @ {a_inv["values"]} gold each = "
                  + f"{a_inv["quantity"]*a_inv["values"]} gold")


def display_inv_summary(player: dict) -> None:
    """
    Displays a summary of the player's inventory: total cost, item count,
    and categories.

    Args:
    player (dict): The player's inventory to summarize.

    Raises:
    Exception: If the player doesn't exist or the inventory is empty.
    """
    if not player:
        raise ValueError(f"{player} is not a player")
    else:
        summary = dict(cost=0, count=0, categories={})
        for desc in player.values():
            summary["cost"] += desc["values"] * desc["quantity"]
            summary["count"] += desc["quantity"]
            if desc["types"] not in summary["categories"]:
                summary["categories"][desc["types"]] = desc["quantity"]
            else:
                summary["categories"][desc["types"]] += desc["quantity"]
        c = ", ".join([f"{t}({h})" for t, h in summary['categories'].items()])
        print(f"Inventory value: {summary["cost"]} gold\n"
              + f"Item count: {summary['count']} item(s)")
        print(f"Categories: {c}")


def transaction(ply1: dict, ply2: dict, item: str, qtt: int) -> None:
    """
    Handles a transaction where one player gives an item to another.

    Args:
    ply1 (dict): The player giving the item.
    ply2 (dict): The player receiving the item.
    item (str): The name of the item being exchanged.
    qtt (int): The quantity of the item being transferred.

    Raises:
    Exception: If the player doesn't exist, doesn't have the item, or doesn't
    have enough quantity to complete the transaction.
    """
    if not ply1:
        raise ValueError(f"{ply1} don't exist")
    elif item not in ply1:
        raise KeyError(f"The player has no {item}")
    elif ply1[item]["quantity"] < qtt:
        raise ValueError(f"The player hasn't {qtt} {item}s"
                         + f" ({ply1[item]["quantity"]})")
    else:
        ply1[item]["quantity"] -= qtt
        if item not in ply2:
            manage_player_inv(ply2, {item: qtt})
        else:
            ply2[item]["quantity"] += qtt


def v_player() -> str:
    """
    Returns the player with the highest total inventory value.

    Returns:
    str: The name of the player and their total inventory value.
    """
    most_valuable = ""
    highest_value = 0
    for player_name, inventory in players.items():
        total_value = sum(
            desc["values"] * desc["quantity"] for desc in inventory.values())
        if total_value > highest_value:
            highest_value = total_value
            most_valuable = player_name
    return f"{most_valuable} ({highest_value} gold)"


def i_player() -> str:
    """
    Returns the player with the most items in their inventory.

    Returns:
    str: The name of the player and their item count.
    """
    most_armed = ""
    highest_cnt = 0
    for player_name, inventory in players.items():
        total_cnt = sum(
            desc["quantity"] for desc in inventory.values()
        )
        if total_cnt > highest_cnt:
            highest_cnt = total_cnt
            most_armed = player_name
    return f"{most_armed} ({highest_cnt} items)"


def r_items() -> str:
    """
    Returns a list of all rare items in the general inventory.

    Returns:
    str: A comma-separated list of rare item names.
    """
    rare = ", ".join(
        item for item in utils.keys() if utils[item]["rank"] == "rare"
        )
    return rare


if __name__ == "__main__":

    add_utils("shield", 200, "armor", "uncommon")
    add_utils("magic_ring", 1000, "artefact", "rare")
    print("=== Player Inventory System ===\n")
    print("=== Alice's Inventory ===")
    try:
        manage_player_inv(alice, {"sword": 1, "potion": 5, "shield": 1})
        display_inv(alice)
        display_inv_summary(alice)
    except (Exception, ValueError) as e:
        print(e)
    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    try:
        transaction(alice, bob, "potion", 2)
        print("Transaction successful!")
        print("\n=== Updated Inventories ===")
        print(f"Alice potions: {alice["potion"]["quantity"]}")
        print(f"Bob potions: {bob["potion"]["quantity"]}")
    except (Exception, ValueError, KeyError) as e:
        print(e)
    print("\n=== Inventory Analytics ===")
    print(f"Most valuable player: {v_player()}")
    print(f"Most items: {i_player()}")
    print(f"Rarest items: {r_items()}")
