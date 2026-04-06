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


def serialize_animal(animal_obj):
    output = ""
    name = animal_obj.get("name", "Unknown")  # name is compulsory
    characteristics = animal_obj.get("characteristics", {})
    locations = animal_obj.get("locations", [])
    lifespan = animal_obj.get("lifespan", "Unknown")

    output += f'<li class="cards__item">\n'
    output += f'<div class="card__title">{name.title()}</div>\n'  # .title() here for unity, but built for m -> Mammal
    output += f'<p class="card__text">\n'
    if "diet" in characteristics:
        output += f'<strong>Diet:</strong> {characteristics["diet"].title()}<br/>\n'
    if locations:
        output += f"<strong>Location:</strong> {locations[0].title()}<br/>\n"
    if "type" in characteristics:
        output += f'<strong>Type:</strong> {characteristics["type"].title()}<br/>\n'
    if "lifespan" in characteristics:
        output += f'<strong>Lifespan:</strong> {characteristics["lifespan"]}<br/>\n'  # deliberately no .title()

    output += f"</p>\n"
    output += f"</li>\n"

    return output


def main():
    """Main function"""

    animals_data = load_data("animals_data.json")
    html_template = load_template("animals_template.html")
    result_html_file_path = "animals.html"

    output = f'<ul class="cards">\n'
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    output += f"</ul>"

    html_result = html_template.replace("__REPLACE_ANIMALS_INFO__", output)
    write_html_file(result_html_file_path, html_result)


if __name__ == "__main__":
    main()
