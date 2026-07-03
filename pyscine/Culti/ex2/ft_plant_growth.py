# Growth Simulator

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.days = age

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    def grow(self, height: int):
        if height > 0:
            self.height += height
            self.days += int(height/2)
        else:
            print(f"Error on the height value ({height} < 0)")

    def age(self, day: int):
        self.grow(day*2)
        self.get_info()
        if (day == 6):
            print(f"Growth this week: +{day*2}cm\n")
        else:
            print(f"Growth on {day} days: +{day*2}cm\n")


if __name__ == "__main__":
    print("=== Day 1 ===")
    rose = Plant("Rose", 25, 30)
    rose.get_info()
    sunflower = Plant("Sunflower", 80, 45)
    sunflower.get_info()
    cactus = Plant("Cactus", 15, 120)
    cactus.get_info()
    print("\n=== Day 7 ===")
    rose.age(6)
    sunflower.age(6)
    cactus.age(8)
