import time
import random
import sys
from typing import Generator

achievments = {
    "monster": {
        "cat": "kill",
        "action": 2
    },
    "ring": {
        "cat": "treasure",
        "action": "inventory"
    },
    "boss": {
        "cat": "kill",
        "action": 5
    },
    "one_level": {
        "cat": "level_up",
        "action": 1
    },
    "sword": {
        "cat": "treasure",
        "action": "inventory"
    }
}

players = {
    "Alice": {
        "level": 5,
        "events": [],
        "inventory": [],
        "score": 28
    },
    "Bob": {
        "level": 1,
        "events": [],
        "inventory": [],
        "score": 2

    },
    "Charlie": {
        "level": 5,
        "events": [],
        "inventory": [],
        "score": 35
    },
    "Sarah": {
        "level": 3,
        "events": [],
        "inventory": [],
        "score": 12
    },
    "Yasmine": {
        "level": 0,
        "events": [],
        "inventory": [],
        "score": 0
    },
    "Will": {
        "level": 9,
        "events": [],
        "inventory": [],
        "score": 68
    }
}

start = time.time()


def x_events_rand(nbr: int, achvts: list[str], plys: list[str]) \
                -> Generator[str]:
    """
    Generates random game events for players.

    Args:
    nbr (int): The number of events to generate.
    achvts (list[str]): The list of possible event types.
    plys (list[str]): The list of existing players.

    Yields:
    str: A description of the generated event.
    """
    i = 1
    while i <= nbr:
        ply = random.choice(plys)
        if ply not in players:
            raise KeyError(f"{ply} is not an existing player")
        player = players[ply]
        ach = random.choice(achvts)
        if ach not in achievments:
            raise KeyError(f"{ach} is not an excpected event")
        (player["events"]).append(achievments[ach]["cat"])
        if achievments[ach]["cat"] == "treasure":
            msg = "found treasure"
            player["inventory"].append(ach)
        if achievments[ach]["cat"] == "level_up":
            msg = "leveled up"
            player["level"] += achievments[ach]["action"]
        if achievments[ach]["cat"] == "kill":
            msg = f"killed a {ach}"
            player["score"] += achievments[ach]["action"]
        event = f"Event {i}: Player {ply} (level {player["level"]}) {msg}"
        i += 1
        yield event


"""
Ce Stream pourrait prendre ausi une valeur de return
qui apparaitrait dans le expect si on depasse le nombre d'appel au yield
(ici nbr)
Cette fonction (generator) se comporte comme une fonctin asynchrone
dont on pourrait suspendre le vol.
"""


def analytics(total: int) -> None:
    """
    Displays statistics on the processed events.

    Args:
    total (int): The total number of events processed.
    """
    print("Total events processed:", total)
    count = {"level_up": 0, "kill": 0, "treasure": 0}
    for ply in players:
        for event in players[ply]["events"]:
            count[event] += 1
    high_level = sum(1 for g in players if players[g]["level"] > 10)
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {count['treasure']}")
    print(f"Level-up events: {count['level_up']}")


def fibonacci(n: int) -> Generator:
    """
    Generates the first 'n' numbers of the Fibonacci sequence.

    Args:
    n (int): The first numbers of the sequence (e.g., n = 3 -> 0, 1, 1)

    Yields:
    int: The Fibonacci numbers.
    """
    a, b = 0, 1
    if n != 0:
        for _ in range(n):
            yield a
            a, b = b, a + b


def prime_numbers(n: int) -> Generator:
    """
    Generates the first 'n' prime numbers.

    Args:
    n (int): The number of prime numbers to generate.

    Yields:
    int: The generated prime numbers.
    """
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
        if is_prime:
            yield num
            count += 1
        num += 1


if __name__ == "__main__":
    try:
        print("=== Game Data Stream Processor ===")
        cnt = 1000
        display = 5
        events = x_events_rand(cnt, [*achievments.keys()],
                               [*players.keys()])
        total = 0
        test_list = []
        for i in range(0, cnt):
            mess = next(events)
            test_list.append(mess)
            if i < display:
                print(mess)
            total += 1
        print("\n=== Stream Analytics ===")
        analytics(total)
        print(f"Memory usage of events: {sys.getsizeof(events)} bytes")
        print(f"Memory usage for a list: {sys.getsizeof(test_list)} bytes")
        events_bis = x_events_rand(10000, [*achievments.keys()],
                                   [*players.keys()])
        if (sys.getsizeof(events) == sys.getsizeof(events_bis)):
            print("After generation of 10000 events, memory usage is constant")
        end = time.time()
        print(f"Processing time: {end - start:.4f} seconds")
    except (Exception, KeyError) as e:
        print("error", e)
    print("\n=== Generator Demonstration ===")
    fibo = ""
    prime = ""
    for fib in fibonacci(10):
        fibo += f"{fib}, "
    print(f"Fibonacci sequence (first 10): {fibo[:-2]}")
    for prm in prime_numbers(5):
        prime += f"{prm}, "
    print("Prime numbers (first 5):", prime[:-2])
