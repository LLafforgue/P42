from .TournamentPlateform import TournamentPlateform, TournamentCard

if __name__ == "__main__":

    print("=== DataDeck Tournament Platform ===\n")
    try:
        data_cards = [
            TournamentCard("Fire dragon", 5, "Legendary",
                           1200, 300, 2000, 100, "dragon_001"),
            TournamentCard("Ice wizard", 3, "Rare",
                           1150, 200, 20, 10, "wizard_001"),
            TournamentCard("Lezard", 1, "Common",
                           200, 10000, 20, 10, "lezard_001"),
            # TournamentCard("Lezard", 1, "Common",
            #                200, 100, 20, 10, "lezard_002"),
        ]

        plateform = TournamentPlateform("Epic Tournament")
        print("Registering Tournament Cards...")
        for card in data_cards:
            plateform.register_card(card)
            print(f"\n{card.get_name()} (ID: {card.id_c.lower()}):")
            for info in card.get_rank_info():
                print(f'- {info}: {card.get_rank_info()[info]}')

        print("\nCreating tournament match...")
        match_result = plateform.create_match("dragon_001", "wizard_001")
        print("Match result:", match_result)
        match_result = plateform.create_match("dragon_001", "lezard_001")
        print("Match result:", match_result)
        # match_result = plateform.create_match("lezard_002", "lezard_001")
        # print("Match result:", match_result)

        leaderboard = plateform.get_leaderboard()
        print("\nLeaderboard:")
        i = 0
        for lead in leaderboard:
            i += 1
            print(f'{i}. {lead}')

        print("\nPlatform Report:")
        print(plateform.generate_tournament_report())

        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except Exception as e:
        print(e)

    # for card in data_cards:
    #     print(card.health)
