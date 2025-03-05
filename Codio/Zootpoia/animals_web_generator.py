import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def make_animals_html(data):
    output = ""

    for animal in data:
        list_html = '<li class="cards__item">'

        if name := animal.get("name"):
            list_html += f'<div class="card__title">{name}</div>'

        list_html += '<p class="card__text">'

        if diet := animal.get("characteristics", {}).get("diet"):
            list_html += f'<strong>Diet:</strong> {diet}<br/>'

        if location := animal.get("locations", [None])[0]:
            list_html += f'<strong>Location:</strong> {location}<br/>'

        if ani_type := animal.get("characteristics", {}).get("type"):
            list_html += f'<strong>Type:</strong> {ani_type}<br/>'

        list_html += '</p></li>'
        output += list_html

    return output


def read_template(html_path):
    with open(html_path, "r") as file:
        file_data = file.read()
    return file_data


def write_html_file(html_content):
    with open("animals.html", "w") as file:
        file.write(html_content)


def main():
    # Load animal data
    animals_data = load_data('animals_data.json')

    # Read the HTML template
    template = read_template('animals_template.html')

    # Generate the string of animal information
    animals_string = make_animals_html(animals_data)

    # Replace the placeholder in the template
    output_html = template.replace('__REPLACE_ANIMALS_INFO__', animals_string)

    # Write the new HTML file
    write_html_file(output_html)


if __name__ == "__main__":
    main()
