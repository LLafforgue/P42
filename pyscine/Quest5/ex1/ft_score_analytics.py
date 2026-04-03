import sys


def scores(args: list[str]) -> None:
    """
    Processes a list of score values and displays statistics.

    Args:
        args (list[str]): A list of strings representing score values.

    Prints:
        - Valid processed scores
        - Number of players
        - Total score
        - Average, high, low scores, and score range (if any valid scores)
        - Error message for invalid score values
    """
    scr = []
    for a in args:
        try:
            scr.append(int(a))
        except ValueError:
            print(f"Oups! '\033[1m{a}\033[0m' is not a good score!!!")
    print(f"Scores processed: {scr}")
    print(f"Total players: {len(scr)}")
    print(f"Total scores: {sum(scr)}")
    if len(scr) > 0:
        print(f"Average score: {sum(scr)/len(scr)}")
        print(f"High score: {max(scr)}")
        print(f"Low score: {min(scr)}")
        print(f"Score range:  {max(scr) - min(scr)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) > 1:
        scores(sys.argv[1:])
    else:
        print("No scores !? No game!\nNo game !?... No game!")
