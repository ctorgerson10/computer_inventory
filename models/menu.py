import os
from menuoption import MenuOption
from utilities import clear


class Menu:

    def __init__(self, heading: str, options: list[MenuOption]):
        self.heading = heading
        self.options = options
        help_option = MenuOption("Help", self.help)
        self.options.append(help_option)

    def help(self):
        """prints help statement which tells the user how to operate the program"""
        clear()
        print("Enter the number corresponding to the menu option you would like to select and press enter.")
        input("Press enter to return to previous menu")
        self.display()

    def display(self):
        clear()
        print(self.heading.title() + "\n")
        for idx, option in enumerate(self.options):
            print(f"{idx + 1}. {option.label}")

        self.accept_input()

    def accept_input(self):
        accepting = True
        while accepting:
            choice = input("> ")
            try:
                choice = int(choice)
            except ValueError as e:
                print("invalid input, please enter a number")
                continue
            accepting = False
            self.options[int(choice) - 1].activate()


if __name__ == "__main__":
    def add_computer():
        return

    def view_computers():
        return

    def edit_computer():
        return

    main_menu = Menu("Main Menu", [
        MenuOption("Add Computer", add_computer),
        MenuOption("View Computers", view_computers),
        MenuOption("Edit a Computer", edit_computer)
    ])

    main_menu.display()
