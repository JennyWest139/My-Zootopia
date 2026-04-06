import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as json_file:
        return json.load(json_file)


def load_template(file_path):
    """Loads an HTML template file as text"""
    with open(file_path, "r", encoding="utf-8") as html_file:
        return html_file.read()


def main():
    """Main function"""

    animals_data = load_data("animals_data.json")

    html_template = load_template("animals_template.html")
    print(html_template)  # nur zum Testen

    output = ""  # define an empty string
    for animal in animals_data:
        name = animal.get("name", "Unknown")  # name is compulsory
        characteristics = animal.get("characteristics", {})
        locations = animal.get("locations", [])

        output += f"\nName: {name}\n"
        if "diet" in characteristics:
            output += f"Diet: {characteristics['diet']}\n"
        if "type" in characteristics:
            output += f"Type: {characteristics['type']}\n"
        if locations:
            output += f"Location: {locations[0]}\n"

    html_result = html_template.replace("__REPLACE_ANIMALS_INFO__", output)
    print(html_result)


if __name__ == "__main__":
    main()
