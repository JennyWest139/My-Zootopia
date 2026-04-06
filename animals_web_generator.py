import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    """Main function"""

    animals_data = load_data("animals_data.json")

    for animal in animals_data:
        name = animal.get("name", "Unknown")  # name is compulsory
        characteristics = animal.get("characteristics", {})
        locations = animal.get("locations", [])

        print(f"\nName: {name}")
        if "diet" in characteristics:
            print(f"Diet: {characteristics['diet']}")
        if "type" in characteristics:
            print(f"Type: {characteristics['type']}")
        if locations:
            print(f"Location: {locations[0]}")


if __name__ == "__main__":
    main()
