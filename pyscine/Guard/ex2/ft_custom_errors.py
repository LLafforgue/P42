class GardenError(Exception):
    """A basic error for garden problems"""
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    """For problems with plants"""


class WaterError(GardenError):
    """For problems with watering"""


def plant_water_delay(name: str, days: int):
    if days > 10:
        raise PlantError(f"The {name} plant is wilting!")
    elif days < 0:
        raise ValueError("Delay must be >= 0")
    else:
        return f"Good delay. Next watering for {name}: {10 - days} days."


def water_tank(tank: int):
    if 0 <= tank < 15:
        raise WaterError("Not enough water in the tank!")
    elif tank < 0:
        raise ValueError("Tank level must be >= 0")
    else:
        return f"Water tank level is sufficient: {tank} liters available."


def test_plantErrors(args: list):
    for i in args:
        try:
            print(plant_water_delay("tomato", i))
        except PlantError as e:
            print(f"Caught PlantError: {e}")
        except ValueError as e:
            print(f"Caught ValueError: {e}")


def test_waterErrors(args: list):
    for i in args:
        try:
            print(water_tank(i))
        except WaterError as e:
            print(f"Caught WaterError: {e}")
        except ValueError as e:
            print(f"Caught ValueError: {e}")


def test_gardenErrors(name: str, args: list):
    for tank, days in args:
        try:
            print(f"\nTesting garden with tank={tank}, days={days}:")
            print(water_tank(tank))
            print(plant_water_delay(name, days))
            print("Garden is healthy and well maintained.")
        except GardenError as e:
            print(f"Caught a garden error: {e}")
        except ValueError as e:
            print(f"Caught ValueError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    test_plantErrors([0, 15, -2])
    print("\nTesting WaterError...")
    test_waterErrors([20, 10, -5])
    print("\nTesting catching all garden errors...")
    test_gardenErrors("cucumber", [(5, 15), (20, -1), (10, 3)])
