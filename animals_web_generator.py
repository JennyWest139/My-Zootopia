import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8-sig") as json_file:
        return json.load(json_file)


def load_template(file_path):
    """Loads an HTML template file as text"""
    with open(file_path, "r", encoding="utf-8") as html_file:
        return html_file.read()


def write_html_file(file_path, content):
    """Creates and fills an HTML file with text"""
    with open(file_path, "w", encoding="utf-8-sig") as result_html_file:
        result_html_file.write(content)
        return None


def main():
    """Main function"""

    animals_data = load_data("animals_data.json")
    html_template = load_template("animals_template.html")
    result_html_file_path = "animals.html"

    output = f'<ul class="cards">\n'

    for animal in animals_data:
        name = animal.get("name", "Unknown")  # name is compulsory
        characteristics = animal.get("characteristics", {})
        locations = animal.get("locations", [])

        output += f'<li class="cards__item">\n'
        output += f'<div class="card__title">{name}</div>\n'
        output += f'<p class="card__text">\n'
        if "diet" in characteristics:
            output += f"<strong>Diet:</strong> {characteristics['diet']}<br/>\n"
        if locations:
            output += f"<strong>Location:</strong> {locations[0]}<br/>\n"
        if "type" in characteristics:
            output += f"<strong>Type:</strong> {characteristics['type']}<br/>\n"
        output += f"</p>\n"
        output += f"</li>\n"
    output += f"</ul>"

    html_result = html_template.replace("__REPLACE_ANIMALS_INFO__", output)
    write_html_file(result_html_file_path, html_result)


if __name__ == "__main__":
    main()
