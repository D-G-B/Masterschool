import sys
from load_data import load_data

# Load the data
all_data = load_data()
list_ship_dicts = all_data["data"]


def show_countries(ships_list):
    """
    Prints all the countries of the ships without duplicates, sorted alphabetically.
    """
    unique_countries = {ship["COUNTRY"] for ship in ships_list}
    sorted_unique_countries = sorted(list(unique_countries))
    for country in sorted_unique_countries:
        print(country)


def top_countries(num, ships_list):
    """
    Prints 'num' number of countries with the most ships.
    For each country, prints the country name along with the count of ships.
    """
    if num <= 0:
        print("Error: Number must be positive")
        return

    counts = {}
    for ship in ships_list:
        country = ship["COUNTRY"]
        counts[country] = counts.get(country, 0) + 1

    # Sort the countries by count (descending) and then alphabetically
    sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    # Make sure we don't try to print more countries than exist
    num = min(num, len(sorted_counts))
    for country, count in sorted_counts[:num]:
        print(f"{country}: {count}")


def print_help():
    """
    Prints a list of available commands.
    """
    help_text = """
Available commands:
  help
    >Prints this help message.

  show_countries
    >Prints a list of all the countries of the ships (without duplicates, alphabetically ordered).

  top_countries <num_countries>
    >Prints a list of the top <num_countries> with the most ships.
    Example:
      top_countries 5
        >prints the top 5 countries with the most ships along with their counts.

  exit
    >Exits the program.
"""
    print(help_text.strip())


# Command handler functions
def help_command():
    """Handler for help command"""
    print_help()


def show_countries_command():
    """Handler for show_countries command"""
    show_countries(list_ship_dicts)


def top_countries_command(args):
    """Handler for top_countries command"""
    if len(args) != 1:
        print("Usage: top_countries <num>")
        return
    try:
        num = int(args[0])
        top_countries(num, list_ship_dicts)
    except ValueError:
        print("Error: <num> must be an integer.")


def exit_command():
    """Handler for exit command"""
    print("Exiting the program.")
    sys.exit(0)


# The dispatcher dictionary maps command names to their handler functions
command_dispatcher = {
    "help": help_command,
    "show_countries": show_countries_command,
    "top_countries": top_countries_command,
    "exit": exit_command
}


def process_command(command_line):
    """
    Processes a command using the dispatcher dictionary.
    """
    parts = command_line.strip().split()
    if not parts:
        return

    cmd = parts[0].lower()
    args = parts[1:]

    if cmd in command_dispatcher:
        handler_function = command_dispatcher[cmd]  # Directly get function
        if args:
            handler_function(args) # Call with args
        else:
            handler_function()      # Call without args
    else:
        print(f"Unknown command: '{cmd}'. Type 'help' for available commands.")


def main():
    """
    Main program loop
    """
    print("Welcome to the Ships CLI!")
    print("Type 'help' for available commands or 'exit' to quit.")

    while True:
        try:
            command_line = input(">> ").strip()
            if command_line:
                process_command(command_line)
        except KeyboardInterrupt:
            print("\nExiting..... (: GOODBYE :)")
            break


if __name__ == "__main__":
    main()