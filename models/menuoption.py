class MenuOption:

    def __init__(self, label: str, action: function):
        self.label = label
        self.action = action

    def activate(self, *args):
        if args is not None:
            self.action(*args)
        else:
            self.action()

    def set_label(self, label: str):
        self.label = label
