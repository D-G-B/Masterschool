import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_info(data):
    for animal in data:
        output_info = {}

        characteristics = animal.get("characteristics", {})

        # Check and add each field if it exists
        if name := animal.get("name"):
            output_info["Name"] = name

        if diet := characteristics.get("diet"):
            output_info["Diet"] = diet

        if location := animal.get("locations", [None])[0]:
            output_info["Location"] = location

        if ani_type := characteristics.get("type"):
            output_info["Type"] = ani_type

        if output_info:
            for key, value in output_info.items():
                print(f"{key}: {value}")
            print()


def main():
    animals_data = load_data('animals_data.json')
    print_info(animals_data)


if __name__ == "__main__":
    main()