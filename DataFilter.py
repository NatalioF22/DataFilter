"""
    Project 1.2
    Author: Natalio Gomes
    Class: COMP390
    Section: 002
    Date: December 18th, 2023
    Functionality: This file contains functions for handling and filtering meteor data. It provides functionality to
               prompt the user for filtering choices, get input for mass and year limits, extract meteor data from
               a file, create MeteorDataEntry objects, display and write headers, and format and print filtered
               meteor data to the terminal or a text file.
"""
import io
from CustumDecorators import *
from meteorite_console_display import *
from meteor_data_class import MeteorDataEntry
from Excel_Writer import *


@value_error_handler
def get_user_filter_choice() -> int:
    """
    Continuously prompts the user for a valid filter choice until one is entered.

    Returns:
    int: User's valid filter choice.
    """
    while True:
        print_filter_menu_options()
        user_input = int(input(">>"))
        if user_input not in [1, 2, 3]:
            print(TerminalColors.RED + "INVALID CHOICE" + TerminalColors.RESET)
        else:
            return user_input


@input_validation_decorator
def get_mass_lower_limit() -> int or SystemExit:
    """
    Gets the lower limit for filtering meteor data based on mass.

    Returns:
    int: Lower limit for meteor mass.
    """
    lower_limit = input(f"Enter the LOWER limit (inclusive) for meteor's MASS (g) ('Q' to QUIT): ")
    if lower_limit == "Q":
        terminate_the_program()
    else:
        return int(lower_limit)


@input_validation_decorator
def get_mass_upper_limit() -> int or SystemExit:
    """
    Gets the upper limit for filtering meteor data based on mass.

    Returns:
    int: Upper limit for meteor mass.
    """
    upper_limit = input("Enter the UPPER limit (inclusive) for meteor's MASS (g) ('Q' to QUIT): ")
    if upper_limit == "Q":
        terminate_the_program()
    else:
        return int(upper_limit)


@input_validation_decorator
def get_year_lower_limit() -> int or SystemExit:
    """
    Gets the lower limit for filtering meteor data based on year.

    Returns:
    int: Lower limit for meteor year.
    """
    year_lower_limit = input("Enter the LOWER limit (inclusive) for meteor's YEAR ('Q' to QUIT): ")
    if year_lower_limit == "Q":
        terminate_the_program()
    else:
        return int(year_lower_limit)


@input_validation_decorator
def get_year_upper_limit() -> int or SystemExit:
    """
    Gets the upper limit for filtering meteor data based on year.

    Returns:
    int: Upper limit for meteor year.
    """

    year_upper_limit = input("Enter the UPPER limit (inclusive) for meteor's YEAR ('Q' to QUIT): ")
    if year_upper_limit == "Q":
        terminate_the_program()
    else:
        return int(year_upper_limit)


def extract_meteor_data_from_file(file_obj: object) -> list[object]:
    """
    Extracts meteor data from a file object and returns a list of MeteorDataEntry objects.

    Parameters:
    file_obj (object): File object containing meteor data.

    Returns:
    list: List of MeteorDataEntry objects.
    """
    try:
        meteor_list = []
        header = file_obj.readline()

        for line in file_obj:
            values = line.split("\t")
            if len(values) < 12: continue
            meteor_object = create_meteor_object(values)
            meteor_list.append(meteor_object) if meteor_object else None
        return meteor_list
    except io.UnsupportedOperation as e:
        print("Error: The selected file is not opened in read mode, and reading is not supported in other modes.")
        print("Please ensure the file is opened in read mode before attempting to extract meteor data.")
        terminate_the_program()


def create_meteor_object(values: list) -> object:
    """
    Creates a MeteorDataEntry object from a list of values.

    Parameters:
    values (list): List of values representing meteor data.

    Returns:
    MeteorDataEntry: MeteorDataEntry object.
    """
    name, meteorite_id, name_type, rec_class, mass_g, fall, year, rec_lat, rec_long, geo_location, states, counties = values
    try:
        return MeteorDataEntry(name, meteorite_id, name_type, rec_class, int(mass_g), fall, int(year), rec_lat,
                               rec_long, geo_location, states, counties)
    except ValueError as e:
        return MeteorDataEntry(name, meteorite_id, name_type, rec_class, -1, fall, -1, rec_lat,
                               rec_long, geo_location, states, counties)


def print_filtered_meteor_header() -> None:
    """
    Prints the header for displaying filtered meteor data.
    """
    name_label, id_label, name_type_label, rec_class_label = 'name', 'id', 'nametype', 'recclass'
    mass_g_label, fall_label, year_label, rec_lat_label, rec_long_label = 'mass_g', 'fall', 'year', 'reclat', 'reclong'
    geo_location_label, states_label, counties_label = 'geolocation', 'states', 'counties'
    spacing = 23
    print(f"{' ' * 7} {name_label:<{spacing}} {id_label:<{spacing}} {name_type_label:<{spacing}} "
          f"{rec_class_label:<{spacing}} {mass_g_label:<{spacing}} {fall_label:<{spacing}} "
          f"{year_label:<{spacing}} {rec_lat_label:<{spacing}} {rec_long_label:<{spacing}}"
          f" {geo_location_label:<{spacing + 8}}{counties_label:<{spacing}}{states_label}")
    print("=" * 300)


def write_filtered_meteor_header_to_text_file(file: object) -> None:
    """
    Writes the header for filtered meteor data to a text file.

    Parameters:
    file: File object for writing.
    """
    name_label, id_label, name_type_label, rec_class_label = 'name', 'id', 'nametype', 'recclass'
    mass_g_label, fall_label, year_label, rec_lat_label, rec_long_label = 'mass_g', 'fall', 'year', 'reclat', 'reclong'
    geo_location_label, states_label, counties_label = 'geolocation', 'states', 'counties'
    spacing = "\t"
    file.write(f"{name_label}{spacing} {id_label}{spacing}{name_type_label}{spacing}"
               f"{rec_class_label}{spacing}{mass_g_label}{spacing}{fall_label}{spacing}"
               f"{year_label}{spacing}{rec_lat_label}{spacing}{rec_long_label}{spacing}"
               f" {geo_location_label}{spacing}{states_label}{spacing}{counties_label}\n")


def format_meteor_data_for_terminal(count: int, meteor: object) -> None:
    """
    Formats meteor data for display in the terminal.

    Parameters:
    count: Count of meteor data.
    meteor: MeteorDataEntry object.
    """
    # TODO - Add counties to print out
    spacing = 24

    counties = meteor.get_counties() if meteor.get_counties() else ""
    states = meteor.get_states() if meteor.get_states() else ""
    print(f"{count:<7}{meteor.get_name():<{spacing}}{meteor.get_id():<{spacing}}{meteor.get_name_type():<{spacing}}"
          f"{meteor.get_rec_class():<{spacing}}{meteor.get_mass():<{spacing}}{meteor.get_fall():<{spacing}}"
          f"{meteor.get_year():<{spacing}}{meteor.get_rec_lat():<{spacing}}{meteor.get_rec_long():<{spacing}}"
          f"{meteor.get_geo_location():<{spacing + 8}}{states:<{spacing}}{counties}", end="")


def format_meteor_data_for_txt_file(meteor_list: list[object]) -> None:
    """
    Formats meteor data for writing to a text file.
    Parameters:
    meteor_list (list): List of MeteorDataEntry objects.
    """
    spacing = "\t"
    current_datetime = datetime.datetime.now()
    file_name = output_text_file_name(current_datetime)
    file = open(file_name, 'a')

    write_filtered_meteor_header_to_text_file(file)
    for meteor in meteor_list:
        file.write(f"{meteor.get_name()}{spacing}{meteor.get_id()}{spacing}{meteor.get_name_type()}{spacing}"
                   f"{meteor.get_rec_class()}{spacing}{meteor.get_mass()}{spacing}{meteor.get_fall()}{spacing}"
                   f"{meteor.get_year()}{spacing}{meteor.get_rec_lat()}{spacing}{meteor.get_rec_long()}{spacing}"
                   f"{meteor.get_geo_location()}{spacing}{meteor.get_states()}{spacing}{meteor.get_counties()}")


def print_filtered_mass_data_to_terminal(meteor_list: list, limits: list) -> None:
    """
    Prints filtered meteor data based on mass to the terminal.

    Parameters:
    meteor_list (list): List of MeteorDataEntry objects.
    limits (list): List containing lower and upper limits for mass filtering.
    """
    print("mass filter")
    print_filtered_meteor_header()
    count = 0
    for meteor in meteor_list:
        if limits[0] <= meteor.get_mass() <= limits[1]: count += 1; format_meteor_data_for_terminal(count, meteor)


def print_filtered_year_data_to_terminal(meteor_list: list, limits: list) -> None:
    """
    Prints filtered meteor data based on year to the terminal.

    Parameters:
    meteor_list (list): List of MeteorDataEntry objects.
    limits (list): List containing lower and upper limits for year filtering.
    """
    print("year filter")
    # TODO - Add counties to print out
    print_filtered_meteor_header()
    count = 0
    for meteor in meteor_list:
        if limits[0] <= meteor.get_year() <= limits[1]:
            count += 1
            format_meteor_data_for_terminal(count, meteor)


def write_filtered_mass_data_to_txt_file(meteor_list: list, limits: list) -> None:
    """
    Writes filtered meteor data based on mass to a text file.

    Parameters:
    meteor_list (list): List of MeteorDataEntry objects.
    limits (list): List containing lower and upper limits for mass filtering.
    """

    filtered_list = []
    for meteor in meteor_list:
        if limits[0] <= meteor.get_mass() <= limits[1]:
            filtered_list.append(meteor)
    format_meteor_data_for_txt_file(filtered_list)


def write_filtered_year_data_to_txt_file(meteor_list: list, limits: list) -> None:
    """
    Writes filtered meteor data based on year to a text file.

    Parameters:
    meteor_list (list): List of MeteorDataEntry objects.
    limits (list): List containing lower and upper limits for year filtering.
    """

    filtered_list = []
    for meteor in meteor_list:
        if limits[0] <= meteor.get_year() <= limits[1]:
            filtered_list.append(meteor)
    format_meteor_data_for_txt_file(filtered_list)
