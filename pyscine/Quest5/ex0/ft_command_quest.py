import sys

args = sys.argv[1:]


def clean(string: str, key: str) -> str:
    """
    Extracts the substring after the last occurrence of a given character.
    Used to clean the programme name (without folrders directorie)

    Args:
        string (str): The input string to process.
        key (str): A single character used as a separator.

    Returns:
        str: The substring after the last occurrence of `key`.
             If `key` is longer than one character,
             returns the original string.
    """
    if len(key) > 1:
        return string
    i = 0
    stop = 0
    while i < len(string):
        if string[i] == key:
            stop = i + 1
        i += 1
    return string[(stop):]


def main() -> None:
    """
    Displays program name and command-line arguments.

    Prints:
        - Program name
        - Number of arguments received
        - Each argument with its index
        - Total number of arguments
    """
    if len(args) == 0:
        print("No arguments provided!")
    print(f"Programme name: {clean(sys.argv[0], "/")}")
    print(f"Argument received: {len(args)}")
    i = 0
    while i < len(args):
        print(f"Argument {i + 1}: {args[i]}")
        i += 1
    print(f"Total arguments: {i + 1}\n")


if __name__ == "__main__":
    print("=== Command Quest ===")
    main()
