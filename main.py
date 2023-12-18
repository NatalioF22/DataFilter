"""
Project 1.2
Author: Natalio Gomes
Class: COMP390
Section: 002
Date: December 18th, 2023
Functionality: This script serves as the main entry point for Project 1.2, allowing the user to filter and process
               meteor data based on mass or year. It utilizes functions from the DataFilter module to handle
               filtering and output options, providing a user-friendly interface for interacting with the meteor data.
"""

from DataFilter import *
from File_Handler import *


def get_valid_integer_input_with_retry(func):
    """
    Prompts the user for an integer input, and retries until a valid integer is entered.

    Parameters:
    func: The function to get user input.

    Returns:
    int: Valid integer input from the user.
    """
    result = None
    while not isinstance(result, int):
        result = func()
    return result


def get_integer_input() -> int or SystemExit:
    """
    Gets integer input from the user.

    Returns:
    int: User-entered integer.
    """

    try:
        user_input = int(input(">> "))
        return user_input
    except ValueError:
        print(TerminalColors.RED + "Please enter an integer." + TerminalColors.RESET)
        print_the_output_option()


def handle_year_filter_option_selection(meteor_list: list[object], limits: list[int]) -> None:
    """
    Handles the user's selection for year filtering options.

    Parameters:
    meteor_list (list): List of MeteorDataEntry objects.
    limits (list): List containing lower and upper limits for year filtering.
    """
    selected_output_option = get_valid_integer_input_with_retry(get_integer_input)
    if selected_output_option == 1:
        print_filtered_year_data_to_terminal(meteor_list, limits)
    elif selected_output_option == 2:
        write_filtered_year_data_to_txt_file(meteor_list, limits)
    elif selected_output_option == 3:
        write_filtered_year_data_to_excel_file(meteor_list, limits)
    elif selected_output_option == 4:
        terminate_the_program()
    else:
        print(TerminalColors.RED + "INVALID CHOICE" + TerminalColors.RESET)


def handle_mass_filter_option_selection(meteor_list: list[object], limits: list[int]) -> None:
    """
    Handles the user's selection for mass filtering options.

    Parameters:
    meteor_list (list): List of MeteorDataEntry objects.
    limits (list): List containing lower and upper limits for mass filtering.
    """
    selected_output_option = get_valid_integer_input_with_retry(get_integer_input)
    if selected_output_option == 1:
        print_filtered_mass_data_to_terminal(meteor_list, limits)
    elif selected_output_option == 2:
        write_filtered_mass_data_to_txt_file(meteor_list, limits)
    elif selected_output_option == 3:
        write_filtered_mass_data_to_excel_file(meteor_list, limits)  # Add this line
    elif selected_output_option == 4:
        terminate_the_program()
    else:
        print(TerminalColors.RED + "INVALID CHOICE" + TerminalColors.RESET)


def process_filtered_mass_data(file_name: str) -> None:
    """
    Processes and filters meteor data based on mass.

    Parameters:
    file_name (str): Name of the input file.
    """
    file_obj = open_file_in_read_mode(file_name)
    meteor_list = extract_meteor_data_from_file(file_obj)
    limits = [get_mass_lower_limit(), get_mass_upper_limit()]
    print_the_output_option()
    handle_mass_filter_option_selection(meteor_list, limits)


def process_filtered_year_data(file_name: str) -> None:
    """
    Processes and filters meteor data based on year.

    Parameters:
    file_name (str): Name of the input file.
    """
    file_obj = open_file_in_read_mode(file_name)
    meteor_list = extract_meteor_data_from_file(file_obj)
    limits = [get_year_lower_limit(), get_year_upper_limit()]
    print_the_output_option()
    handle_year_filter_option_selection(meteor_list, limits)


def process_user_choice(user_choice: int, file_name: str) -> None or SystemExit:
    """
    Processes the user's choice for filtering meteor data.

    Parameters:
    user_choice (int): User's choice for filtering (1 for mass, 2 for year, 3 to exit).
    file_name (str): Name of the input file.
    """
    if user_choice == 1:
        process_filtered_mass_data(file_name)
    elif user_choice == 2:
        process_filtered_year_data(file_name)
    elif user_choice == 3:
        terminate_the_program()


def main():
    """
    Main function for the script. Displays a welcome message, prompts the user for a file name, and processes
    the user's choice for filtering meteor data.
    """
    print_welcome_message()
    file_name = get_valid_file_name_loop()
    file_obj = open_file_with_user_mode(file_name)
    lst = extract_meteor_data_from_file(file_obj)
    user_choice = get_user_filter_choice()
    process_user_choice(user_choice, file_name)
    print("\nProcess Completed!!!")


if __name__ == "__main__":
    main()
