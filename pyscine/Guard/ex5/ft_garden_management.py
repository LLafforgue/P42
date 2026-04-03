class GardenError(Exception):
    """A basic error for garden problems"""


def check_int(value):
    if value is None or not isinstance(value, int):
        raise ValueError("Value must be an integer")


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, name: str):
        try:
            # Verifie si le nom de la plante est valide (non vide)
            if not name or not name.strip():
                raise ValueError("Plant name cannot be empty!")
            else:
                self.plants.append(name.strip())
                print(f"Plant `{name.strip()}` added successfully.")
        except (Exception, ValueError) as e:
            print(f"Error adding plant: {e}")

    def water_plants(self, plant_list):
        print("Opening watering system")
        test = []
        try:
            for plant in plant_list:
                # Verifie si la plante est dans le jardin
                if not plant or plant not in self.plants:
                    raise ValueError(
                        f"Error: Cannot water {plant} - invalid plant!"
                        )
                else:
                    print(f"Watering {plant}")
                    test.append(plant)
        except (Exception, ValueError) as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")
        if test == plant_list:
            print("\033[1mAll plants watered successfully!\033[0m")
        else:
            print("\033[1mWatering completed with some errors.\033[0m")

    def check_plant_health(self, plant_name: str, water_lvl: int, sun_h: int):
        try:
            # Verifie les valeurs d'entrée
            check_int(water_lvl)
            check_int(sun_h)
            # Vérifie si le nom de la plante
            if not plant_name or not plant_name.strip():
                raise ValueError("Plant name cannot be empty!")
            if plant_name not in self.plants:
                raise ValueError(f"Plant `{plant_name}` is not in the garden!")
            # Vérifie si le niveau d'eau est raisonnable (entre 1 et 10)
            if not (1 <= water_lvl <= 10):
                if water_lvl < 1:
                    raise ValueError(
                        f"Water level {water_lvl} is too low (min 1)"
                        )
                else:
                    raise ValueError(
                        f"Water level {water_lvl} is too high (max 10)"
                        )
            # Vérifie le nombre d'heures d'ensoleillement (entre 2 et 12)
            if not (2 <= sun_h <= 12):
                if sun_h > 12:
                    raise ValueError(
                        f"Sunlight hours {sun_h} is too high (max 12)"
                        )
                else:
                    raise ValueError(
                        f"Sunlight hours {sun_h} is too low (min 2)"
                        )
            print(
                f"\033[1m{plant_name.strip()}\033[0m: healthy"
                + f" (water: {water_lvl}, sun: {sun_h})"
                )
        except (ValueError) as e:
            print(f"Error checking {plant_name.strip()}: {e}")

    @staticmethod
    def water_tank(tank: int):
        try:
            # Verifie les valeurs d'entrée
            check_int(tank)
            if 0 <= tank < 15:
                raise GardenError("Not enough water in the tank!")
            elif tank < 0 or None or not int(tank):
                raise ValueError("Tank level must be an integer >= 0")
            else:
                return (
                    f"Water tank level is sufficient: {tank} liters available."
                    )
        except (GardenError, ValueError) as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("System recovered and continuing...")


if __name__ == "__main__":
    garden = GardenManager()
    print("=== Garden Management System ===\n")

    print("Adding plants...")
    garden.add_plant("Rose")
    garden.add_plant("  ")
    garden.add_plant("  Tulip")

    print("\nWatering plants...")
    plant_list = ["Rose", "Tulip", "Daisy"]
    garden.water_plants(plant_list)

    print("\nChecking plant health...")
    garden.check_plant_health("Rose", 5, 8)
    garden.check_plant_health("Tulip", 15, 8)  # error niveau d'eau
    garden.check_plant_health("Daisy", 5, 8)  # plant inconnue
    garden.check_plant_health("Tulip", "f", 15)  # error d'entrée

    print("\nTesting error recovery...")
    GardenManager.water_tank(10)  # error niveau d'eau bas

    print("\nGarden management system test complete!")
