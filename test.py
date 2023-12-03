from ColoredText import TerminalColors

def check_valid_mode(user_mode_input):
    
    return user_mode_input if user_mode_input in ['r','w','a','x'] else None
def get_file_mode_input():
    input_mode = None
    while not input_mode:
        user_mode_input = input("Mode -> ")
        input_mode = check_valid_mode(user_mode_input)
    return input_mode


get_file_mode_input()



#_______________________________________________________________________________________________


from File_Handler import *
from meteorite_console_display import *
from meteor_data_class import MeteorDataEntry


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

def extract_meteor_data_from_file(file_obj: object) -> list:
    meteor_list = []
    header = file_obj.readline()
    try:
        for line in file_obj:
            values = line.split("\t")
            if len(values) < 11:
                continue
            try:
                name, meteorite_id, name_type, rec_class, mass_g, fall, year, rec_lat, rec_long, geo_location, states, counties = values
                meteorite_object = MeteorDataEntry(name, meteorite_id, name_type, rec_class, int(mass_g), fall, int(year), rec_lat, rec_long, geo_location, states, counties)
                meteor_list.append(meteorite_object)
            except ValueError as e:
                continue
                #print(f"Debug: Error processing line: {line}")
                #print(f"Debug: Error details: {e}")
    except Exception as e:
        pass
        #print(f"Debug: Error during file processing: {e}")

    #print(f"Debug: Number of entries extracted: {len(meteor_list)}")
    return meteor_list



def print_filtered_data_to_terminal(meteor_list, output_file):
    lower_limit = get_mass_lower_limit()
    upper_limit = get_mass_upper_limit()
    year_label = "YEAR"
    name_label = "NAME"
    count = 0
    print("=" * 45)
    print(f"{' ' * 4}{name_label:<24}{year_label}")
    try:
        with open(output_file, 'w') as f:
            for meteor in meteor_list:
                if lower_limit <= meteor.get_mass() <= upper_limit:
                    try:
                        for j in meteor_list:
                            count += 1
                            print(f"{count:<8}{j.get_name():<28}{j.get_year()}")
                    except TypeError as error:
                        print(error)
    except ValueError as e:
        print(f"Error: {e}")

def write_filtered_data_to_txt_file(meteor_list, output_file):
    lower_limit = get_mass_lower_limit()
    upper_limit = get_mass_upper_limit()
    year_label = "YEAR"
    name_label = "NAME"
    count = 0
    print("=" * 45)
    print(f"{' ' * 4}{name_label:<24}{year_label}")
    try:
        with open(output_file, 'w') as f:
            for meteor in meteor_list:
                if lower_limit <= meteor.get_mass() <= upper_limit:
                    count += 1
                    f.write(f"{count:<8}{meteor.get_name():<28}{meteor.get_year()}\n")
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


def test(user_choice, file_name, output_file):
    if user_choice == 1:
        file_obj = open_file_in_read_mode(file_name)
        meteor_list = extract_meteor_data_from_file(file_obj)
        print_filtered_data_to_terminal(meteor_list, output_file)
    elif user_choice == 2:
        meteor_list = extract_meteor_data_from_file(file_obj)
        write_filtered_data_to_txt_file(meteor_list, output_file)
    elif user_choice == 3:
        terminate_the_program()

# In the main function, specify the output file name
def main():
    print_welcome_message()
    file_name = get_valid_file_name_loop()
    output_file = "filtered_output.txt"
    file_obj = open_file_with_user_mode(file_name)
    lst = extract_meteor_data_from_file(file_obj)
    user_choice = get_user_filter_choice()

    test(user_choice, file_name, output_file)

if __name__ == "__main__":
    main()
