if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    alice_achievements = {"first_kill", "bulls_eye", "runner",
                          "level_10", "eagle Eye"}
    bob_achievements = {"first_kill", "artist", "level_10"}
    charlie_achievements = {"master_mind", "demolition_expert",
                            "bulls_eye", "level_10"}
    diana_achievements = {"first_kill", "runner",
                          "artist", "demolition_expert", "level_10",
                          "level_100"}
    player_achievements = {
        "Alice": alice_achievements,
        "Bob": bob_achievements,
        "Charlie": charlie_achievements,
        "Diana": diana_achievements
    }
    for player in player_achievements:
        achieved = player_achievements[player]
        print(f"\n{player}'s Achievements:")
        print(achieved)

    all_achievements = set().union(*player_achievements.values())

    print("\n=== Achievement Analytics ===")
    print("All unique achievements:")
    print(all_achievements)
    print(f"Total unique achievements: {len(all_achievements)}")
    print("\nCommon to all players: " +
          str(all_achievements.intersection(*player_achievements.values())))

    '''Recherche de(s) accomplissement unique(s)'''
    rare_achievements = set()
    for achievement in all_achievements:
        count = 0
        for achievements in player_achievements.values():
            if achievement in achievements:
                count += 1
        if count == 1:
            rare_achievements.add(achievement)
    print("Rare achievements (1 player):", rare_achievements)
    print("=== Alice vs Bob ===\nCommon to both:",
          alice_achievements.intersection(bob_achievements))
    print("Alice unique:",
          alice_achievements - bob_achievements)
    print("Bob unique:",
          bob_achievements - alice_achievements)
