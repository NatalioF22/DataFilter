"""
    Project 1.2
    Author: Natalio Gomes
    Class: COMP390
    Section: 002
    Date: December 14th, 2023
"""


class TerminalColors:
    """
    A utility class for defining ANSI escape codes for text color and formatting in the terminal.

    Usage:
        print(TerminalColors.PURPLE + "This text is in purple." + TerminalColors.RESET)

    Attributes:
        - PURPLE: ANSI escape code for purple text.
        - BLUE: ANSI escape code for blue text.
        - CYAN: ANSI escape code for cyan text.
        - GREEN: ANSI escape code for green text.
        - WARNING: ANSI escape code for warning text (usually yellow).
        - RED: ANSI escape code for red text.
        - RESET: ANSI escape code to reset text color and formatting.
        - BOLD: ANSI escape code for bold text.
        - UNDERLINE: ANSI escape code for underlined text.
    """

    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
