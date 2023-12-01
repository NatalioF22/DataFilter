from FileHandler import prompt_for_file_name, file_mode, terminate_the_program
from ColoredText import TerminalColors
from meteor_data_class import MeteorDataEntry
from Messages import list_of_strings


file_name = prompt_for_file_name()
file_obj = file_mode(file_name)


def input_validation_decorator(function_name):
    def decorator_function(*args, **kwargs):
        while True:
            try: return function_name(*args, **kwargs)
            except ValueError: print(TerminalColors.RED + "Invalid limit. Please enter a number." + TerminalColors.RESET)
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                break
    return decorator_function


def filter_menu_option()->int:
    while True:
        print(list_of_strings[1]["filter_menu_options"], end="")
        try:
            user_input_choice = int(input(f">>" + TerminalColors.GREEN))
            if user_input_choice in [x for x in range(1,4)]: return user_input_choice
            else: print(TerminalColors.RESET + TerminalColors.RED + "INVALID CHOICE!" + TerminalColors.RESET)
        except ValueError: print(TerminalColors.RED + "\nINVALID CHOICE" + TerminalColors.RESET)

def main():
    user_filter_choice = filter_menu_option()
    meteor_list_data = extract_meteor_data_from_file(file_obj)
    if user_filter_choice == 1: filter_meteor_by_mass(meteor_list_data)
    elif user_filter_choice == 2: filter_meteor_by_fall_year(meteor_list_data)
    else: terminate_the_program()



@input_validation_decorator
def get_mass_lower_limit():
    lower_limit = int(input(TerminalColors.RESET + f"Enter the LOWER limit (inclusive) for meteor's MASS (g) ('Q' to QUIT): "))
    return lower_limit

@input_validation_decorator
def get_mass_upper_limit():
    upper_limit = int(input(TerminalColors.RESET + "Enter the UPPER limit (inclusive) for meteor's MASS (g) ('Q' to QUIT): "))
    return upper_limit

@input_validation_decorator
def get_year_lower_limit():
    year_lower_limit = int(input(TerminalColors.RESET +"Enter the LOWER limit (inclusive) for meteor's YEAR ('Q' to QUIT): "))
    return year_lower_limit

@input_validation_decorator
def get_year_upper_limit():
    year_upper_limit = int(input(TerminalColors.RESET + "Enter the UPPER limit (inclusive) for meteor's YEAR ('Q' to QUIT): "))
    return year_upper_limit


def display_filtered_data_menu():
    while True:
        try:
            print(list_of_strings[0]['output_data_filter'], end='')
            user_input = int(input(  TerminalColors.RESET + ">>"))
            if user_input not in [x for x in range(1,5)]: print("Invalid Choice")
            else: return user_input
        except ValueError:
            print(TerminalColors.RED + "Invalid input. Please enter a number." + TerminalColors.RESET)
        
    

def extract_meteor_data_from_file(file_obj: object)->list:
    meteor_list = []
    header = file_obj.readline()
    try:
        for line in file_obj:
            values = line.split("\t")
            if len(values) < 11: continue
            name, meteorite_id, name_type, rec_class, mass_g, fall, year, rec_lat, rec_long, geo_location, states, counties = values
            meteorite_object = MeteorDataEntry(name, meteorite_id, name_type, rec_class, int(mass_g), fall, int(year),rec_lat,rec_long, geo_location, states, counties)
            meteor_list.append(meteorite_object)
    except ValueError: pass
    return meteor_list

def print_filtered_data_to_terminal(lst):
    lower_limit = get_mass_lower_limit()
    upper_limit = get_mass_upper_limit()
    try:
        for meteor in lst:
            if lower_limit <= meteor.get_mass() <= upper_limit:
               
                print(f"Name: {meteor}, Mass: {meteor.get_mass()}")
               
    except ValueError: pass

def print_filtered_data_to_txt_file(lst):
    lower_limit = get_mass_lower_limit()
    upper_limit = get_mass_upper_limit()
    try:
        for meteor in lst:
            if lower_limit <= meteor.get_mass() <= upper_limit:
                with open('example.txt', 'a') as file:
                        file.write(f"Name: {meteor}, Mass: {meteor.get_mass()}\n")
    except ValueError: 
        pass
        

def print_filtered_data_to_excel_file(lst):
    pass

def filter_meteor_by_mass(lst:list):
    display_filtered_data_menu_choice = display_filtered_data_menu()
    if display_filtered_data_menu_choice == 1: print_filtered_data_to_terminal(lst)
    elif display_filtered_data_menu_choice == 2: print_filtered_data_to_txt_file(lst)
    else: pass
    

def filter_meteor_by_fall_year(lst:list):
    lower_limit = get_year_lower_limit()
    upper_limit = get_year_upper_limit()
    print(lower_limit)
    print(upper_limit)


main()