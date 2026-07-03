def garden_operations():
    print("=== Garden Error Types Demo ===\n")
    # Test FileNotFoundError
    print("Testing FileNotFoundError...")
    try:
        f = open("missing.txt", "r")
        print(f.read())
        f.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e.args[1]} `{e.filename}`")

    # Test ZeroDivisionError
    print("Testing ZeroDivisionError...")
    try:
        result = 10 / 0
        print(result)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    # Test ValueError
    print("Testing ValueError...")
    try:
        number = int("abc")
        print(number)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    # Test KeyError
    print("Testing KeyError...")
    try:
        my_dict = {'a': 1, 'b': 2}
        value = my_dict['c']
        print(value)
    except KeyError as e:
        print(f"Caught KeyError: {e}")


def test_error_types():

    # Multiple errors together
    print("=== Testing multiple errors together... ===\n")

    def func1(file_name: str):
        f = open(file_name, "r")
        print(f.read())
        f.close()

    def func2(int_test: int):
        return 10 / int_test

    def func3(str_test: str):
        return int(str_test)

    def func4(key: str):
        my_dict = {'a': 1, 'b': 2}
        return my_dict[key]

    functions = [(func1, "none.txt"), (func2, 0), (func3, "abc"), (func4, 'c')]
    test = 1
    for func, arg in functions:
        print(f"Test {test}:")
        test += 1
        try:
            func(arg)
            print("[OK]")
        except (FileNotFoundError) as e:
            print(f"Caught an Error: {e.args[1]}")
        except (ZeroDivisionError, ValueError) as e:
            print(f"Caught an Error with value: {e}")
        except KeyError as e:
            print(f"Caught an Error: {e}")
        except Exception:
            print("Caught an unexpected error.")
    print("All error types tested successfully!")


if __name__ == "__main__":
    garden_operations()
    print("")
    test_error_types()
