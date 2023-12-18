"""
    Project 1.2
    Author: Natalio Gomes
    Class: COMP390
    Section: 002
    Date: December 18th, 2023

    File Handler File
    This module provides utility functions for file handling, including file opening modes, 
    file name validation, and user prompts.
"""
import os
from meteorite_console_display import *


def output_text_file_name(current_datetime: object, extension=".txt") -> str:
    """
    This method generates a formatted date string for use in creating output text file names.

    Returns:
        str: Formatted date string.
    """
    
    replacements = [',', ':', " ", "."]
    formatted_date_string = str(current_datetime)
    for replacement in replacements:
        formatted_date_string = formatted_date_string.replace(replacement, "_")
    return f"{formatted_date_string}{extension}"


def check_if_file_exists(file_name: str) -> bool or None:
    """
    Check if the specified file exists.

    Args:
        file_name (str): The name of the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    if os.path.exists(file_name): 
        print(TerminalColors.GREEN + f"\nTarget file: {file_name}\n" + TerminalColors.RESET)
        return True
    else:
        print(TerminalColors.RED + f"\nERROR: TARGET FILE NAME: '{file_name}' IS NOT VALID!\n" + TerminalColors.RESET)
    

def prompt_for_valid_file_name_input() -> str or SystemExit:
    """
    Prompt the user for a valid file name input.

    Returns:
        str: Valid file name.
    """
    print("Enter a valid file name (ex. 'file_name.txt') with its file extension (if applicable) |or| Enter '>q' or "
          "'>Q' to quit: ", end="")
    file_name = input(TerminalColors.GREEN)
    if file_name == ">q" or file_name == ">Q":
        terminate_the_program()
    elif check_if_file_exists(file_name):
        return file_name


def get_valid_file_name_loop() -> str:
    """
    Get a valid file name in a loop until a valid one is provided.

    Returns:
        str: Valid file name.
    """
    file_name = None
    while not file_name:
        file_name = prompt_for_valid_file_name_input()
    return file_name


def prompt_for_file_name() -> str:
    """
    Prompt the user for a file name.

    Returns:
        str: File name.
    """
    result = get_valid_file_name_loop()
    return result 


def check_valid_mode(user_mode_input) -> str or SystemExit:
    """
    Check if the specified file mode input is valid.

    Args:
        user_mode_input (str): User-provided file mode input.

    Returns:
        str: Valid file mode.
    """
    if user_mode_input.lower() == '>q':
        terminate_the_program()
    return user_mode_input.lower() if user_mode_input.lower() in ['r','w','a','x'] else None


def get_file_mode_input() -> str:
    """
    Get valid file mode input from the user.

    Returns:
        str: Valid file mode.
    """
    input_mode = None
    while not input_mode:
        try:
            print_file_opening_modes()
            user_mode_input = input("Mode -> ")
            input_mode = check_valid_mode(user_mode_input)
            print(TerminalColors.RED + f"\nINVALID MODE!\n" + TerminalColors.RESET) if not input_mode else print(TerminalColors.GREEN + f" \nFile Mode: {input_mode}\n " + TerminalColors.RESET)
        except KeyboardInterrupt:
            print(TerminalColors.CYAN + "\n\nMust exit this program successfully!\n" + TerminalColors.RESET)
    return input_mode


def open_file_in_read_mode(file_name: str) -> object:
    """
    Open a file in read mode.

    Args:
        file_name (str): Name of the file.

    Returns:
        file: File object.
    """
    file_obj = open(file_name)
    return file_obj


def open_file_in_write_mode(file_name: str) -> object:
    """
    Open a file in write mode.

    Args:
        file_name (str): Name of the file.

    Returns:
        file: File object.
    """
    file_obj = open(file_name,'w')
    return file_obj


def open_file_in_append_mode(file_name: str) -> object:
    """
    Open a file in append mode.

    Args:
        file_name (str): Name of the file.

    Returns:
        file: File object.
    """

    file_obj = open(file_name,'a')
    return file_obj

        
def open_file_in_exclusive_mode(file_name: str) -> object or SystemExit:
    """
    Open a file in exclusive mode.

    Args:
        file_name (str): Name of the file.

    Returns:
        file: File object.
    """
    try:
        file_obj = open(file_name, 'x')
        return file_obj
    except FileExistsError:
        print(TerminalColors.RED + f"\nERROR: File '{file_name}' already exists!\n" + TerminalColors.RESET)
        terminate_the_program()


def open_file_with_user_mode(file_name: str) -> object:
    """
    Open a file based on user-provided mode.

    Args:
        file_name (str): Name of the file.

    Returns:
        file: File object.
    """
    mode = get_file_mode_input()

    if mode == 'r':
        return open_file_in_read_mode(file_name)
    elif mode == 'a':
        return open_file_in_append_mode(file_name)
    elif mode == 'w':
        return open_file_in_write_mode(file_name)
    else:
        return open_file_in_exclusive_mode(file_name)



