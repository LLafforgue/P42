def validate_ingredients(ingredients: str) -> str:
    """Validates the given ingredients for a spell."""
    val_ingr = {"fire", "water", "earth", "air"}
    set_ingr = {ingr for ingr in ingredients.lower().split(" ")}
    return (f"{ingredients} - "
            + f"{"IN" if not set_ingr.intersection(val_ingr) else ""}"
              + "VALID")


if __name__ == "__main__":
    print(validate_ingredients("Fire air chips"))
    print(validate_ingredients("caca"))
