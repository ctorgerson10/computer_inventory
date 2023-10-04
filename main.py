import re
import json

from models.menu import Menu
from models.menuoption import MenuOption
from models.computer import Computer
from models.utilities import clear

# some cool variables
ip_address_pattern = re.compile(r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]["
                                r"0-9]?)){3}")
computers: 'list[Computer]' = []
save_file = 'computer_inventory.json'

# function definitions
def load_data(filename: str):
    with open(filename, 'r+') as data:
        raw = json.load(data)

    print(list(raw.values()))
    for i in list(raw.values()):
        tmp = Computer(i)
        computers.append(tmp)


def save_data(filename: str):
    payload = {}
    for idx, computer in enumerate(computers):
        payload[str(idx)] = computer.get_json()

    print(payload)
    with open(filename, 'w+') as data:
        json.dump(payload, data, indent=4)


def save_and_return():
    save_data(save_file)
    main_menu.display()


def save_and_exit():
    save_data(save_file)
    exit()


def add_computer():
    clear()
    print("this will do something eventually")
    input("press enter to return to the menu")
    main_menu.display()


def view_computers():
    clear()
    if computers is not None:
        for i in computers:
            i.display()
        print("\n")
    input("press enter to continue")
    main_menu.display()


def edit_computer():
    clear()
    for idx, computer in enumerate(computers):
        print(f"{idx + 1}. {computer.name}")
    accepting = True
    while accepting:
        choice = input("> ")

        try:
            choice = int(choice)
        except ValueError as e:
            print("invalid input, please enter a number")
            continue

        if choice < 0 or choice > len(computers)+1:
            print("invalid input, out of allowed range")
            continue

        accepting = False

    chosen = computers[choice - 1]

    edit_menu = Menu(f'Editing {chosen.name} (select an option to edit)', [
            MenuOption('ip', chosen.set_ip_input),
            MenuOption('mac_address', chosen.set_mac_address_input),
            MenuOption('os', chosen.set_os_input),
            MenuOption('status', chosen.set_status_input),
            MenuOption('name', chosen.set_name_input),
            MenuOption('stop editing', save_and_return)
        ], add_exit=False)
    
    while True:
        edit_menu.display()


main_menu = Menu("Main Menu", [
        MenuOption("Add Computer", add_computer),
        MenuOption("View Computers", view_computers),
        MenuOption("Edit a Computer", edit_computer),
        MenuOption("Save and Exit", save_and_exit)
    ])


def main():
    computers = load_data(save_file)
    main_menu.display()


if __name__ == "__main__":
    main()
