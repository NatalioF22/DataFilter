
from File_Handler import *
from meteorite_console_display import *
from meteor_data_class import MeteorDataEntry
import datetime


@value_error_handler
def get_valid_user_input_choice():
    
    print_filter_menu_options()
    user_input = int(input(">>"))
    if user_input not in [1, 2, 3]:
        print(TerminalColors.RED + "INVALID CHOICE" + TerminalColors.RESET)
    else:
        return user_input


@keyboard_interrupt_handler
def get_user_filter_choice():
    while True:
        return get_valid_user_input_choice()

@input_validation_decorator
def get_mass_lower_limit():
    lower_limit = input(f"Enter the LOWER limit (inclusive) for meteor's MASS (g) ('Q' to QUIT): ")
    if lower_limit == "q":
        terminate_the_program()
    else:
        return int(lower_limit)

@input_validation_decorator
def get_mass_upper_limit():
    upper_limit = input( "Enter the UPPER limit (inclusive) for meteor's MASS (g) ('Q' to QUIT): ")
    if upper_limit == "q":
        terminate_the_program()
    else:
        return int(upper_limit)

@input_validation_decorator
def get_year_lower_limit():
    year_lower_limit = input("Enter the LOWER limit (inclusive) for meteor's YEAR ('Q' to QUIT): ")
    if year_lower_limit == "q":
        terminate_the_program()
    else:
        return int(year_lower_limit)

@input_validation_decorator
def get_year_upper_limit():
    year_upper_limit = input("Enter the UPPER limit (inclusive) for meteor's YEAR ('Q' to QUIT): ")
    if year_upper_limit == "q":
        terminate_the_program()
    else:
        return int(year_upper_limit)

def extract_meteor_data_from_file(file_obj: object) -> list:
    meteor_list = []
    header = file_obj.readline()
    
    for line in file_obj:
        values = line.split("\t")
        if len(values) < 11: 
            continue
        meteor_object = create_meteor_object(values)
        meteor_list.append(meteor_object) if meteor_object else None
            
    return meteor_list

def create_meteor_object(values: list):
    try:
        name, meteorite_id, name_type, rec_class, mass_g, fall, year, rec_lat, rec_long, geo_location, states, counties = values
        return MeteorDataEntry(name, meteorite_id, name_type, rec_class, int(mass_g), fall, int(year), rec_lat, rec_long, geo_location, states, counties)
    except ValueError as e:
        return None



def print_filtered_meteor_header():
    name_label, id_label, name_type_label, rec_class_label = 'name', 'id', 'nametype', 'recclass'
    mass_g_label, fall_label, year_label, rec_lat_label, rec_long_label = 'mass_g','fall', 'year', 'reclat', 'reclong'
    geo_location_label, states_label = 'geolocation', 'states'
    spacing = 23
    print("=" * 300)
    print(f"{' ' * 7} {name_label:<{spacing}} {id_label:<{spacing}} {name_type_label:<{spacing}} "
          f"{rec_class_label:<{spacing}} {mass_g_label:<{spacing}} {fall_label:<{spacing}} "
          f"{year_label:<{spacing}} {rec_lat_label:<{spacing}} {rec_long_label:<{spacing}}"
          f" {geo_location_label:<{spacing+4}} {states_label}")



def write_filtered_meteor_header_to_text_file(file):
    name_label, id_label, name_type_label, rec_class_label = 'name', 'id', 'nametype', 'recclass'
    mass_g_label, fall_label, year_label, rec_lat_label, rec_long_label = 'mass_g', 'fall', 'year', 'reclat', 'reclong'
    geo_location_label, states_label = 'geolocation', 'states'
    spacing = 23
    print("=" * 300)
    file.write(f"{' ' * 7} {name_label:<{spacing}} {id_label:<{spacing}} {name_type_label:<{spacing}} "
          f"{rec_class_label:<{spacing}} {mass_g_label:<{spacing}} {fall_label:<{spacing}} "
          f"{year_label:<{spacing}} {rec_lat_label:<{spacing}} {rec_long_label:<{spacing}}"
          f" {geo_location_label:<{spacing + 4}} {states_label}")


def format_meteor_data_for_terminal(count, meteor):
    spacing = 24
    print(f"{count:<8}{meteor.get_name():<{spacing}}{meteor.get_id():<{spacing}}{meteor.get_name_type():<{spacing}}"
          f"{meteor.get_rec_class():<{spacing}}{meteor.get_mass():<{spacing}}{meteor.get_fall():<{spacing}}"
          f"{meteor.get_year():<{spacing}}{meteor.get_rec_lat():<{spacing}}{meteor.get_rec_long():<{spacing}}"
          f"{meteor.get_geo_location():<{spacing}}{meteor.get_states():<{spacing}}")


def format_meteor_data_for_txt_file(meteor_list):
    spacing = 24
    file_name = output_text_file_name()
    file = open(file_name, 'w')
    count = 0
    write_filtered_meteor_header_to_text_file(file)
    for meteor in meteor_list:
        count += 1
        file.write(f"\n{count:<8}{meteor.get_name():<{spacing}}{meteor.get_id():<{spacing}}{meteor.get_name_type():<{spacing}}"
          f"{meteor.get_rec_class():<{spacing}}{meteor.get_mass():<{spacing}}{meteor.get_fall():<{spacing}}"
          f"{meteor.get_year():<{spacing}}{meteor.get_rec_lat():<{spacing}}{meteor.get_rec_long():<{spacing}}"
          f"{meteor.get_geo_location():<{spacing}}{meteor.get_states():<{spacing}}")
def print_filtered_mass_data_to_terminal(meteor_list,limits:list):
    print_filtered_meteor_header()
    count = 0
    for meteor in meteor_list:
        if limits[0] <= meteor.get_mass() <= limits[1]: count += 1; format_meteor_data_for_terminal(count, meteor)

def print_filtered_year_data_to_terminal(meteor_list,limits:list):
    print_filtered_meteor_header()
    count = 0
    for meteor in meteor_list:
        if limits[0] <= meteor.get_year() <= limits[1]: count += 1; format_meteor_data_for_terminal(count, meteor)


def print_the_output_option():
    print("How would you like to output the filter results?")
    print("1. On Screen (in terminal)")
    print("2. To a TEXT file")
    print("3. To an EXCEL file")
    print("4. QUIT")


def output_text_file_name():
    current_datetime = datetime.datetime.now()
    replacements = [',', ':', " ", "."]

    formatted_date_string = str(current_datetime)

    for replacement in replacements:
        formatted_date_string = formatted_date_string.replace(replacement, "_")

    return formatted_date_string



def write_filtered_mass_data_to_txt_file(meteor_list, limits):
    filtered_list = []
    for meteor in meteor_list:
        if limits[0] <= meteor.get_mass() <= limits[1]: filtered_list.append(meteor)
    format_meteor_data_for_txt_file(filtered_list)



def get_valid_integer_input_with_retry(func):
    result = None
    while not isinstance(result, int):
        result = func()
    return result

def get_integer_input():
    try:
        user_input = int(input(">> "))
        return user_input
    except ValueError:
        print("\nPlease enter an integer.")



def handle_filter_option_selection(meteor_list, limits):
    selected_option = get_valid_integer_input_with_retry(get_integer_input)
    if selected_option == 1: print_filtered_mass_data_to_terminal(meteor_list, limits)
    elif selected_option == 2: write_filtered_mass_data_to_txt_file(meteor_list, limits)
    elif selected_option == 3: pass  # Add logic for handling option 3
    elif selected_option == 4: terminate_the_program()
    else: print(TerminalColors.RED + "INVALID CHOICE" + TerminalColors.RESET)




def process_filtered_mass_data(file_name):
    file_obj = open_file_in_read_mode(file_name)
    meteor_list = extract_meteor_data_from_file(file_obj)
    limits = [get_mass_lower_limit(),get_mass_upper_limit() ]
    print_the_output_option()
    handle_filter_option_selection(meteor_list, limits)

    
def process_filtered_year_data(file_name):
    file_obj = open_file_in_read_mode(file_name)
    meteor_list = extract_meteor_data_from_file(file_obj)
    limits = [get_year_lower_limit(),get_year_upper_limit() ]
    print_the_output_option()
    handle_filter_option_selection(meteor_list, limits)


def process_user_choice(user_choice, file_name):
    if user_choice == 1:
        process_filtered_mass_data(file_name)
    elif user_choice == 2:
        process_filtered_year_data(file_name)
    elif user_choice == 3:
        terminate_the_program()


# In the main function, specify the output file name
def main():
    print_welcome_message()
    file_name = get_valid_file_name_loop()
    file_obj = open_file_with_user_mode(file_name)
    lst = extract_meteor_data_from_file(file_obj)
    user_choice = get_user_filter_choice()

    process_user_choice(user_choice, file_name)

if __name__ == "__main__":
    main()
