# garden data

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print(self):
        print(self.name, ":", self.height, "cm,", self.age, "days old")


""" if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    rose.print()
    sunflower = Plant("Sunflower", 80, 45)
    sunflower.print()
    cactus = Plant("Cactus", 15, 120)
    cactus.print() """
