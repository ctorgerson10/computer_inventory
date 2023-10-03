import re
import json

from models.menu import Menu
from models.menuoption import MenuOption
from models.computer import Computer
from models.utilities import clear

# regex pattern for IPv4 address
ip_address_pattern = re.compile(r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]["
                                r"0-9]?)){3}")

computers = []

# Menu and function definitions
def load_data(filename):
    with open(filename, 'r+') as data:
        raw: dict = json.load(data)
    return raw

def save_data(obj, filename):
    with open(filename, 'w') as data:
        json.dump(obj, filename)


def add_computer():
    clear()
    print("this will do something eventually")
    input("press enter to return to the menu")
    main_menu.display()


def view_computers():
    if computers is not None:
        print(computers)
    input("press enter to continue")
    main_menu.display()

def edit_computer():
    clear()
    print("this will do something eventually")
    input("press enter to return to the menu")
    main_menu.display()


main_menu = Menu("Main Menu", [
        MenuOption("Add Computer", add_computer),
        MenuOption("View Computers", view_computers),
        MenuOption("Edit a Computer", edit_computer)
    ], add_exit=True)


if __name__ == "__main__":
    computers = load_data("computer_inventory.json")
    main_menu.display()
