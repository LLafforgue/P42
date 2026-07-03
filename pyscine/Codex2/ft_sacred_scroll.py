import alchemy


def init_comtrolled(crea_ele: str) -> None:
    """Attempts to access an element creation function."""
    try:
        if crea_ele not in alchemy.__all__:
            raise AttributeError('AttributeError - not exposed')
        else:
            element = getattr(alchemy, crea_ele)
            print(f"alchemy.{crea_ele}():", element())
    except AttributeError as e:
        print(f"alchemy.{crea_ele}():", e)

# def init_comtrolled(crea_ele: str) -> None:
#     try:
#         if crea_ele not in alchemy.__all__:
#             raise AttributeError('AttributeError - not exposed')
#         else:
#             element = alchemy.__dict__[crea_ele]
#             print(f"alchemy.{crea_ele}:", element())
#     except AttributeError as e:
#         print(f"alchemy.{crea_ele}():", e)


if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===")
    print("\nTesting direct module access:")
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", alchemy.elements.create_air())

    print("\nTesting package-level access (controlled by __init__.py):")
    elements = ["create_water", "create_fire", "create_earth", "create_air"]
    for ele in elements:
        init_comtrolled(ele)

    print("\nPackage metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)
