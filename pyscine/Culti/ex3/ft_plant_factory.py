class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def status(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

    def growth(self, days):
        self.age += days
        self.height += days*2
        self.status()
        if (days == 6):
            print(f"Growth this week: +{days*2}cm\n")
        else:
            print(f"Growth on {days} days: +{days*2}cm\n")


""" if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    liste = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 15, 120),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
        ]
    for plant in liste:
        plant.status()
    print(f"\nTotal plants created: {len(liste)}") """
