# Datas
players = [
    {
        'name': 'alice', 'scores': 2300, 'activity': False,
        'achievements': {
            'first_kill',
            'level_10',
            'treasure_hunter',
            'boss_slayer',
            'speed_run'
            }
    },
    {'name': 'bob', 'scores': 1800, 'activity': True,
     'achievements': {
         'level_10',
         'treasure_hunter',
         'puzzle_master'
         }
     },
    {'name': 'charlie', 'scores': 2150, 'activity': False,
     'achievements': {
         'first_kill',
         'level_10',
         'boss_slayer',
         'speed_run',
         'treasure_hunter',
         'puzzle_master',
         'legendary'
         }
     },
    {'name': 'sarah', 'scores': 1100, 'activity': True,
     'achievements': {}
     }
    ]
regions = ['north', 'east', 'north', 'central']


def list_analytics(players: list) -> None:
    """
        Analyzes player data and displays statistics.

    Args:
        players (list): A list of player dictionaries
            with 'name', 'activity', and 'scores' keys.

    Raises:
        TypeError: If `players` is not a list.
        KeyError: If any player dictionary is missing required keys.

    Prints:
        - High scorers (>2000)
        - Doubled scores
        - Active players
    """
    if type(players) is not list:
        raise TypeError("A list of player is needed !")
    for player in players:
        keys = set(player.keys())
        test_keys = {'name', 'activity', 'scores'} - keys
        if test_keys:
            raise KeyError(f"Missed {test_keys} in {player}")
    names, scores = zip(*[(player['name'], player['scores'])
                          for player in players])
    high_scorers = [player for player, score in zip(names, scores)
                    if score > 2000]
    doubled_scores = [score * 2 for score in scores]
    active_players = [player['name'] for player in players
                      if player['activity']]
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {doubled_scores}")
    print(f"Active players: {active_players}")


def dict_comprehension(names: tuple, scores: tuple) -> None:
    """
    Creates a dictionary of player scores and categorizes them.

    Args:
        names (tuple): Player names (str).
        scores (tuple): Player scores (int).

    Raises:
        TypeError: If `names` or `scores` are not tuples.
        ValueError: If `names` and `scores` have different lengths.

    Prints:
        - Player score dictionary
        - Score categories (high, medium, low)
        - Achievement counts
    """
    if type(names) is not tuple or type(scores) is not tuple:
        raise TypeError("Carefull padawan ! Args has to be tuples !")
    if len(names) != len(scores):
        raise ValueError("Each players needs a score and respectively !")
    player_scores = {player: score for player, score in zip(names, scores)}
    score_categories = {}
    score_categories['high'] = sum(1 for score in scores if score > 2000)
    score_categories['medium'] = sum(
        1 for score in scores if 2000 >= score > 1000)
    score_categories['low'] = sum(1 for score in scores if 1000 >= score)
    achievement_counts = {
        player['name']: len(player['achievements']) for player in players}
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    print("\n=== List Comprehension Examples ===")
    try:
        list_analytics(players)
    except (Exception, KeyError, TypeError) as e:
        print(e)

    print("\n=== Dict Comprehension Examples ===")
    names, scores = zip(*[(player['name'], player['scores'])
                        for player in players])
    try:
        dict_comprehension(names, scores)
    except (Exception, TypeError, ValueError) as e:
        print(e)

    print("\n=== Set Comprehension Examples ===")
    unique_players = set(names)
    rare_achievements = set()
    achievements = set().union(*[player['achievements'] for player in players])
    rare_achievements = {
        achievement for achievement in achievements
        if sum(1 for player in players
               if achievement in player['achievements']) == 1
    }
    active_regions = {
        region for player, region in zip(players, regions)
        if player['activity']
    }
    print("Unique players:", unique_players)
    print("Unique achievements:", rare_achievements)
    print("Active regions:", active_regions)

    print("\n=== Combined Analysis ===")
    total_players = sum(1 for _ in players)
    print("Total players:", total_players)
    print("Total achievements:", len(achievements))
    print("Total unique achievements:", len(rare_achievements))
    average_score = sum(player['scores'] for player in players)/total_players
    print("Average score:", average_score)
    top = [player for player in players
           if player['scores'] == max([p['scores'] for p in players])]
    top_name = top[0]['name']
    top_point, ach = top[0]['scores'], len(top[0]['achievements'])
    print("Top performance:", top_name, f'({top_point}, {ach} achievements)')
