from menu import Menu

class MenuOption:


        def __init__(self, label: str, action: function):
            self.label = label
            self.action = action

        def __init__(self, label: str, action: Menu):
             self.label = label
             self.action = action


        def activate(self, *args):
            Menu.clear()

            if self.action.isinstance(Menu):
                 self.action.display()

            if args is not None:
                self.action(*args)
            else:
                self.action()


        def set_label(self, label):
            self.label = label