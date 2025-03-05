import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_info(data):
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
            print("\n".join(output_parts) + "\n")


def main():
    animals_data = load_data('animals_data.json')
    print_info(animals_data)


if __name__ == "__main__":
    main()