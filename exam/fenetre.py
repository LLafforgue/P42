def fenetre(liste: list, nbr: int) -> list:
    return [
        max(liste[i:i+nbr])
        for i in range(len(liste) - nbr + 1)
    ]


if __name__ == "__main__":
    print(fenetre([1, 5, 3, 4], 2))
