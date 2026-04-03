def check_temperature(temp_str: str) -> int:
    temp = 0
    try:
        temp = int(temp_str)
        # Vérifie si la température est raisonnable (entre 0 et 40)
        if temp >= 0 and temp <= 40:
            return temp
        elif temp < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)\n")
    # Gestion des erreurs de conversion
    except Exception:
        print(f"Error: {temp_str} is not a valid number\n")


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")
    Testing = "Testing temperature: "
    for test in ["25", "abc", "100", "-50"]:
        print(Testing + test)
        temp = check_temperature(test)
        if temp:
            print(f"Temperature {temp}°C is perfect for plants!\n")
    print("All tests completed - program didn`t crash!")


if __name__ == "__main__":
    test_temperature_input()
