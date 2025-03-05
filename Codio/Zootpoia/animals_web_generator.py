import json


def load_data(file_path):
    """
    Loads a JSON file and returns its contents as a Python object.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict or list: The parsed JSON data.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def make_animals_html(data):
    """
    Generates an HTML list of animal information from the provided data.

    Args:
        data (list of dict): A list of dictionaries, each representing an animal with its attributes.

    Returns:
        str: A string containing HTML markup for the animals.
    """
    output = ""

    for animal in data:
        list_html = '<li class="cards__item">'

        if name := animal.get("name"):
            list_html += f'<div class="card__title">{name}</div>'

        list_html += '<div class="card__text">'
        list_html += '<ul class="card__details">'

        if diet := animal.get("characteristics", {}).get("diet"):
            list_html += f'<li class="card__detail-item"><strong>Diet:</strong> {diet}</li>'

        if location := animal.get("locations", [None])[0]:
            list_html += f'<li class="card__detail-item"><strong>Location:</strong> {location}</li>'

        if ani_type := animal.get("characteristics", {}).get("type"):
            list_html += f'<li class="card__detail-item"><strong>Type:</strong> {ani_type}</li>'

        list_html += '</ul></div></li>'
        output += list_html

    return output


def read_template(html_path):
    """
    Reads an HTML template file and returns its contents as a string.

    Args:
        html_path (str): The path to the HTML template file.

    Returns:
        str: The contents of the HTML file.
    """
    with open(html_path, "r") as file:
        file_data = file.read()
    return file_data


def write_html_file(html_content):
    """
    Writes the generated HTML content to a file.

    Args:
        html_content (str): The HTML content to write into the file.

    Returns:
        None
    """
    with open("animals.html", "w") as file:
        file.write(html_content)


def main():
    """
    Orchestrates the process of loading animal data, generating HTML content,
    and writing the final HTML output to a file.

    Returns:
        None
    """
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
