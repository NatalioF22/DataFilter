"""
    Project 1.2
    Author: Natalio Gomes
    Class: COMP390
    Section: 002
    Date: December 18th, 2023
"""
from ColoredText import TerminalColors


def print_welcome_message() -> None:
    """
    Print a welcome message for the Meteorite Filtering Application.

    This function prints a welcome message with information about the purpose
    of the application and the required format for the input text file.

    How to use it:
        print_welcome_message()

    Author: Natalio Gomes
    Date: December 2023
    """
    print(f"{'*'*100}")
    print("\n\t\t--- Welcome to the Meteorite Filtering Application --- \n\n"
          "This program allows you to filter NASA Meteorite data stored in a text file.\n\n"
          "To use this application, ensure that the data in the text file is organized in the following format:\n"
          "\t- Each line of the text file should describe a single meteorite.\n"
          "\t- For each meteorite, there must be 12 tab-separated data points.\n\n"
          "Please follow the prompts to filter the data.\n\n"
          "\tAuthor: Natalio Gomes\n"
          "\tDecember 2023\n")
    

def print_file_opening_modes() -> None:
    
    print(
        """
    What mode would you like to open the file with?
    "r" - open for reading (default)
    "w" - open for writing, truncating the file first.
         (WARNING: this mode will delete the contents of an existing file!)
    "x" - open for exclusive creation, failing if the file already exists
    "a" - open for writing, appending to the end of the file if it exists
    Enter ">q" or ">Q" to quit """
    )


def print_filter_menu_options() -> None:
    print("What attribute would you like to filter the data on?")
    print("1. Meteor MASS(g)")
    print("2. The YEAR the meteor fell to earth")
    print("3. QUIT")


def terminate_the_program() -> exit:
    print(TerminalColors.RESET + "\nThe program is now exiting... GOODBYE!\n" + TerminalColors.RESET)
    exit()


def print_the_output_option() -> None:
    print("How would you like to output the filter results?")
    print("1. On Screen (in terminal)")
    print("2. To a TEXT file")
    print("3. To an EXCEL file")
    print("4. QUIT")