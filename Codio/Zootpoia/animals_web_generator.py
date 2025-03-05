import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def make_animals_string(data):

    output = ""

    for animal in data:
        output_parts = []

        if name := animal.get("name"):
            output_parts.append(f"Name: {name}")

        if diet := animal.get("characteristics", {}).get("diet"):
            output_parts.append(f"Diet: {diet}")

        if location := animal.get("locations", [None])[0]:
            output_parts.append(f"Location: {location}")

        if ani_type := animal.get("characteristics", {}).get("type"):
            output_parts.append(f"Type: {ani_type}")

        if output_parts:
            output += "\n".join(output_parts) + "\n\n"

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
    animals_string = make_animals_string(animals_data)

    # Replace the placeholder in the template
    output_html = template.replace('__REPLACE_ANIMALS_INFO__', animals_string)

    # Write the new HTML file
    write_html_file(output_html)


if __name__ == "__main__":
    main()