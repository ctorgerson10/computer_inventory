import os
from menuoption import MenuOption

class Menu:

    def __init__(self, heading: str, options: list[MenuOption]):
        self.heading = heading
        self.options = options
        help_option = MenuOption("Help", self.help)
        self.options.append(help_option)


    def clear():
        """clears terminal/cmd window (cross-platform), src: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console"""
        os.system('cls' if os.name=='nt' else 'clear')


    def help():
         """prints help statement which tells the user how to operate the program"""
         Menu.clear()
         print("Enter the number corresponding to the menu option you would like to select and press enter.")
         print("press any key to return to main menu")


    def display(self):
         print(self.heading.title() + "\n")
         for idx, option in enumerate(self.options()):
              print(f"{idx + 1}. {option.label}")


    def accept_input(self):
         self.display()
         accepting = True
         while accepting:
            choice = input("> ")
            if choice != isinstance(int):
                print("invalid input, try again")
            else:
                self.options[choice-1].activate()


if __name__ == "__main__":
    mainmenu = Menu()