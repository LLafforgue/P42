def check_plant_health(plant_name, water_level, sunlight_hours):
    # Vérifie si le nom de la plante est valide (non vide)
    if plant_name and plant_name.strip():
        pass
    else:
        raise ValueError("Plant name cannot be empty!")
        return
    # Vérifie si le niveau d'eau est raisonnable (entre 1 et 10)
    if 1 <= water_level <= 10:
        pass
    else:
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        else:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        return
    # Vérifie le nombre d'heures d'ensoleillement (entre 2 et 12)
    if 2 <= sunlight_hours <= 12:
        pass
    else:
        if sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
                )
        else:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
                )
        return
    print(f"Plant `{plant_name}` is healthy!")


def test_plant_checks():
    # Un test avec des valeurs correctes (devrait fonctionner normalement)
    print("\nTesting with good values...")
    try:
        check_plant_health("Rose", 5, 8)
    except ValueError as e:
        print(f"Error: {e}")
    # Un test avec un mauvais nom de plante (devrait lancer une ValueError)
    print("\nTesting empty plant name...")
    try:
        check_plant_health("  ", 5, 8)
    except ValueError as e:
        print(f"Error: {e}")
    # Un test avec un mauvais niveau d'eau
    # (devrait lancer une ValueError)
    print("\nTesting bad water level...")
    try:
        check_plant_health("Tulip", 15, 8)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting low water level...")
    try:
        check_plant_health("Tulip", 0, 8)
    except ValueError as e:
        print(f"Error: {e}")
    # Un test avec un mauvais nombre d'heures d'ensoleillement
    # (devrait lancer une ValueError)
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("Daisy", 5, 15)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Plant Health Checker ===")
    test_plant_checks()
    print("\nAll error raising tests completed!")
