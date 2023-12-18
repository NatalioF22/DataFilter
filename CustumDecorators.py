"""
    Project 1.2
    Author: Natalio Gomes
    Class: COMP390
    Section: 002
    Date: December 18th, 2023
    Functionality: This module provides error handling functionalities, including handling KeyboardInterrupt and ValueError.
"""

from ColoredText import TerminalColors


# Value Error Handler

def print_value_error_message():
    """
    Prints a value error message.
    """
    print(TerminalColors.RED + "\n\nPLEASE ENTER ONLY INTEGERS ACCORDING TO THE INSTRUCTIONS, ANYTHING ELSE WILL BE "
                               "IGNORED\n" + TerminalColors.RESET)


def handle_value_error(function_name):
    """
    Handles a value error by printing an error message and recalling the function.

    Parameters:
    function_name: The function to be recalled.

    Returns:
    The result of the function after handling the value error.
    """
    try:
        return function_name()
    except ValueError:
        print_value_error_message()


def handle_value_error_in_loop(function_name):
    """
    Handles a value error in a loop until a valid input is provided.

    Parameters:
    function_name: The function to be recalled.
    """
    valid = False
    while not valid:
        valid = True if handle_value_error(function_name) else False


def value_error_handler_decorator(function_name):
    """
    Decorator that handles value errors in a loop until a valid input is provided.

    Parameters:
    function_name: The function to be decorated.

    Returns:
    A decorated function.
    """
    return lambda *args, **kwargs: handle_value_error_in_loop(function_name)


def handle_value_error_message():
    """
    Prints a value error message.
    """
    print(TerminalColors.RED + "Please enter a valid integer." + TerminalColors.RESET)


def value_error_handler_inner(function_name, *args, **kwargs):
    """
    Handles a value error by printing an error message and recalling the function in a loop.

    Parameters:
    function_name: The function to be recalled.
    *args: Positional arguments for the function.
    **kwargs: Keyword arguments for the function.

    Returns:
    The result of the function after handling the value error.
    """
    while True:
        try:
            return function_name(*args, **kwargs)
        except ValueError:
            handle_value_error_message()


def value_error_handler(function_name):
    """
    Decorator that handles value errors by recalling the function in a loop.

    Parameters:
    function_name: The function to be decorated.

    Returns:
    A decorated function.
    """
    return lambda *args, **kwargs: value_error_handler_inner(function_name, *args, **kwargs)


def input_validation_decorator(function_name):
    """
    Decorator that handles value errors and keyboard interrupts in a loop until valid input is provided.

    Parameters:
    function_name: The function to be decorated.

    Returns:
    A decorated function.
    """

    def decorator_function(*args, **kwargs):
        while True:
            try:
                return function_name(*args, **kwargs)
            except ValueError:
                print(TerminalColors.RED + "Invalid limit. Please enter a number." + TerminalColors.RESET)
            except KeyboardInterrupt:
                print(
                    TerminalColors.CYAN + "\n\nPlease Enter '>q' or '>Q' to exit the Program\n" + TerminalColors.RESET)

    return decorator_function
