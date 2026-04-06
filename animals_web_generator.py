import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as json_file:
        return json.load(json_file)


def load_template(file_path):
    """Loads an HTML template file as text"""
    with open(file_path, "r", encoding="utf-8") as html_file:
        return html_file.read()


def write_html_file(file_path, content):
    """Creates and fills an HTML file with text"""
    with open(file_path, "w", encoding="utf-8") as result_html_file:
        result_html_file.write(content)
        return None


def main():
    """Main function"""

    animals_data = load_data("animals_data.json")
    html_template = load_template("animals_template.html")
    result_html_file_path = "animals.html"

    output = ""  # define an empty string
    output += f'<ul class="cards">'

    for animal in animals_data:
        name = animal.get("name", "Unknown")  # name is compulsory
        characteristics = animal.get("characteristics", {})
        locations = animal.get("locations", [])

        output += f'<li class="cards__item">'

        output += f"Name: {name}<br/>"
        if "diet" in characteristics:
            output += f"Diet: {characteristics['diet']}<br/>"
        if "type" in characteristics:
            output += f"Type: {characteristics['type']}<br/>"
        if locations:
            output += f"Location: {locations[0]}<br/>"

        output += f"</li>"
    output += f"</ul>"

    html_result = html_template.replace("__REPLACE_ANIMALS_INFO__", output)
    write_html_file(result_html_file_path, html_result)


if __name__ == "__main__":
    main()
