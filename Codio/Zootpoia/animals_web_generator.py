import json



def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def main():
    animals_data = load_data('animals_data.json')
    print(animals_data)

if __name__ == "__main__":
    main()