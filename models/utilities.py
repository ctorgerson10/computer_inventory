import os


def clear():
    """
    clears terminal/cmd window (cross-platform),
    src: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
    os.system('cls' if os.name == 'nt' else 'clear')