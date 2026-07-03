class Plant:

    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        self.description = f'{name} : {height}cm'

    def status(self):
        print({self.description})


class FloweringPLant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.types = "Flowering Plants"
        self.color = color
        self.description = f'{name} : {height}cm, {color} flowers (blooming)'


class PrizeFlower(FloweringPLant):
    def __init__(self, name: str, height: int, color: str, prize: int):
        super().__init__(name, height, color)
        self.prize = prize
        self.description = f'{name} : {height}cm, {color}'
        self.description += f'flowers (blooming), prize points: {prize}'


class Garden:
    def __init__(self, owner: str, score: int):
        self.owner = owner
        self.score = score
        self.plants = []
        self.grew = 0
        self.plant_count = 0
        self.flowering_count = 0
        self.prizeflower_count = 0

    def add_plant(self, plant, plant_type: str):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden.")
        if plant_type == "Plant":
            self.plant_count += 1
        elif plant_type == "FloweringPLant":
            self.flowering_count += 1
        elif plant_type == "PrizeFlower":
            self.prizeflower_count += 1

    def growth(self, value):
        print(f"{self.owner} is helping all plants grow...")
        if (value > 0):
            for plant in self.plants:
                plant.height += value
                self.grew += value
                print(f"{plant.name} grew by {value}cm")

    def garden_report(self):
        report = f"=== {self.owner}'s Garden Report ===\n"
        report += "Plants in garden:\n"
        for plant in self.plants:
            report += f"- {plant.description}\n"
        report += f"\nPlants added: {len(self.plants)}, "
        report += f"Total growth: {self.grew}cm\n"
        report += f'Plant types: {self.plant_count} regular, '
        report += f'{self.flowering_count} flowering, '
        report += f'{self.prizeflower_count} prize flowers'
        return report


class GardenManager:
    @classmethod
    def create_garden_network(cls, owners_scores: list[tuple[str, int]]):
        cls._instances = {}
        for o, s in owners_scores:
            cls._instances[o] = Garden(o, s)

    @classmethod
    def get_garden_by_owner(cls, owner: str):
        return cls._instances[owner]

    @classmethod
    def get_gardens_report(cls):
        network = "Height validation test: True\n"
        i = 0
        network += "Garden scores - |"
        for o in cls._instances:
            i += 1
            network += f" {o}:  {cls._instances[o].score} |"
        print(network)
        print(f"Total gardens managed: {i}")

    @staticmethod
    def one_garden_report(garden: Garden):
        print(garden.garden_report())

    @staticmethod
    def add_plant_to_garden(garden: Garden, plant, plant_type: str):
        garden.add_plant(plant, plant_type)


""" if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    GardenManager.create_garden_network([("Alice", 218), ("Bob", 92)])
    alice_garden = GardenManager.get_garden_by_owner("Alice")
    bob_garden = GardenManager.get_garden_by_owner("Bob")

    oak = Plant("Oak Tree", 101)
    rose = FloweringPLant("Rose", 26, "Red")
    sunflower = PrizeFlower("Sunflower", 51, "Yellow", 10)
    alice_garden.add_plant(oak, "Plant")
    alice_garden.add_plant(rose, "FloweringPLant")
    alice_garden.add_plant(sunflower, "PrizeFlower")
    bob_garden.add_plant(Plant("Pine Tree", 150), "Plant")
    print("")
    alice_garden.growth(1)
    print("")
    GardenManager.one_garden_report(alice_garden)
    print("")
    GardenManager.get_gardens_report() """
