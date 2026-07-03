class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.types = None
        self.char = None

    def status(self):
        print(f"{self.name} ({self.types}): \
            {self.height}cm, {self.age} days, {self.char}")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.types = "Flower"
        self.color = color
        self.char = f"{self.color} bloom"

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.types = "Flower"
        self.trunk_diameter = trunk_diameter
        self.char = f"{self.trunk_diameter} diameter"

    def produce_shade(self):
        print(f"{self.name} provides 78 square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.types = "Vegetables"
        self.harvest_season = harvest_season
        self.char = f"{self.harvest_season} harvest"

    def nutritional_value(self, nut: str):
        print(f"{self.name} is rich en {nut}\n")


""" if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    listf = [
        Flower("Rose", 25, 30, "red"),
        Flower("Iris", 12, 651, "white")
        ]
    for _ in listf:
        _.status()
        _.bloom()
    listt = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pin", 650, 2500, 62)
        ]
    for _ in listt:
        _.status()
        _.produce_shade()
    v = Vegetable("Tomato", 80, 90, "summer")
    v.status()
    v.nutritional_value("vitamine C") """
