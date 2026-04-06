import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    """Main function"""

    animals_data = load_data("animals_data.json")
    print(animals_data)

    for animal in animals_data:
        name = animal.get("name", "Unknown")

        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet", "Unknown")
        type_of_animal = characteristics.get("type", "Unknown")

        locations = animal.get("locations", [])
        if locations:
            first_location = locations[0]
        else:
            first_location = "Unknown"

        print(
            f"\nName: {name}\nDiet: {diet}\nLocation: {first_location}\nType: {type_of_animal}"
        )


if __name__ == "__main__":
    main()
