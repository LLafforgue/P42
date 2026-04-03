def water_plants(plant_list):
    print("Opening watering system")
    test = "ok"
    try:
        for plant in plant_list:
            if plant:
                print(f"Watering {plant}")
            else:
                message = f"Error: Cannot water {plant}"
                message += " - invalid plant!"
                raise Exception(message)
    except Exception as e:
        print(f"{e}")
        test = "error"
    finally:
        print("Closing watering system (cleanup)")
    if test == "ok":
        print("Watering completed successfully!")


def test_watering_system():
    print("Testing normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("\nTesting with error...")
    plants_with_error = ["tomato", None, "lettuce"]
    water_plants(plants_with_error)


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
