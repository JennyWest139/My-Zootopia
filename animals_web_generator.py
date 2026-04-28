import json

import requests

from API_KEYS import API_NINJAS_API_KEY


def load_data_from_api(animal_name):
    """Fetch animal data from API by name"""
    api_url = "https://api.api-ninjas.com/v1/animals"

    headers = {"X-Api-Key": API_NINJAS_API_KEY}

    params = {"name": animal_name}

    response = requests.get(api_url, headers=headers, params=params)
    response.raise_for_status()  # wichtig für sauberes Fehlerhandling

    return response.json()


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

    name = animal_obj.get("name", "Unknown")
    characteristics = animal_obj.get("characteristics", {})

    skin_type = characteristics.get("skin_type")
    extra_class = " unknown-skin" if not skin_type else ""

    locations = animal_obj.get("locations", [])
    lifespan = animal_obj.get("lifespan", "Unknown")

    output += f'<li class="cards__item{extra_class}">\n'
    output += f'  <div class="card__title">{name.title()}</div>\n'
    output += '  <div class="card__text">\n'
    output += '    <ul class="animal__details">\n'

    if "diet" in characteristics:
        output += (
            f"      <li><strong>Diet:</strong> "
            f'{characteristics["diet"].title()}</li>\n'
        )

    if locations:
        output += (
            f"      <li><strong>Location:</strong> " f"{locations[0].title()}</li>\n"
        )

    if "type" in characteristics:
        output += (
            f"      <li><strong>Type:</strong> "
            f'{characteristics["type"].title()}</li>\n'
        )

    if "lifespan" in characteristics:
        output += (
            f"      <li><strong>Lifespan:</strong> "
            f'{characteristics["lifespan"]}</li>\n'
        )  # deliberately no .title()

    if skin_type:
        output += f"      <li><strong>Skin type:</strong> {skin_type.title()}</li>\n"
    else:  # tested by deleting one skin in json
        output += (
            "      <li><strong>Skin type:</strong> "
            '<span class="skin-unknown">Unknown</span></li>\n'
        )

    output += "    </ul>\n"
    output += "  </div>\n"
    output += "</li>\n"

    return output


def get_available_skin_types(animals_data):
    """Return sorted unique skin_type values found in the JSON."""
    skin_types = set()

    for animal in animals_data:
        characteristics = animal.get("characteristics", {})
        skin_type = characteristics.get("skin_type")
        if skin_type:
            skin_types.add(skin_type)

    return sorted(skin_types)


def main():
    """Main function"""

    # animals_data = load_data("animals_data.json")
    animals_data = load_data_from_api("Fox")
    html_template = load_template("animals_template.html")
    result_html_file_path = "animals.html"

    available_skin_types = get_available_skin_types(animals_data)
    available_skin_types_with_all = ["All"] + available_skin_types  # to allow full list

    print("Available skin types:")
    for skin_type in available_skin_types_with_all:
        print(f"- {skin_type}")

    # Case-insensitive Auswahl: mapping lower -> original

    skin_type_lookup = {
        skin_type.lower(): skin_type for skin_type in available_skin_types_with_all
    }

    selected_skin_type = ""
    while selected_skin_type.lower() not in skin_type_lookup:
        selected_skin_type = input(
            "Please enter a skin type from the list above: "
        ).strip()
        if selected_skin_type.lower() not in skin_type_lookup:
            print("Invalid skin type. Please choose one from the list.")

    selected_skin_type = skin_type_lookup[selected_skin_type.lower()]

    filtered_animals = []
    unknown_skin_animals = []

    for animal in animals_data:
        characteristics = animal.get("characteristics", {})
        skin_type = characteristics.get("skin_type")

        if selected_skin_type == "All":
            filtered_animals.append(animal)
        else:
            if not skin_type:
                unknown_skin_animals.append(animal)
            elif skin_type == selected_skin_type:
                filtered_animals.append(animal)

    if selected_skin_type == "All":
        animals_to_render = filtered_animals
    else:
        animals_to_render = filtered_animals + unknown_skin_animals

    output = f'<ul class="cards">\n'
    for animal_obj in animals_to_render:
        output += serialize_animal(animal_obj)

    output += f"</ul>"

    html_result = html_template.replace("__REPLACE_ANIMALS_INFO__", output)
    write_html_file(result_html_file_path, html_result)


if __name__ == "__main__":
    main()
