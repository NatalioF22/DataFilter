from ColoredText import TerminalColors
import os
from CustumDecorators import *
from meteorite_console_display import *



def check_if_file_exists(file_name:str) -> bool:
    if os.path.exists(file_name): 
        print(TerminalColors.GREEN + f"\nTarget file: {file_name}\n" + TerminalColors.RESET)
        return True
    else:
        print(TerminalColors.RED + f"\nERROR: TARGET FILE NAME: '{file_name}' IS NOT VALID!\n" + TerminalColors.RESET)
    

@keyboard_interrupt_handler
def prompt_for_valid_file_name_input():
    print("Enter a valid file name (ex. 'file_name.txt') with its file extension (if applicable) |or| Enter '>q' or '>Q' to quit: "  , end="")
    file_name = input(TerminalColors.GREEN)
    if file_name == ">q" or file_name == ">Q":
        terminate_the_program()
    elif check_if_file_exists(file_name):
        return file_name


def get_valid_file_name_loop():
    file_name = None
    while not file_name:
        file_name = prompt_for_valid_file_name_input()
    return file_name


def prompt_for_file_name():
    result = get_valid_file_name_loop()
    return result 


def check_valid_mode(user_mode_input):
    if user_mode_input.lower() == '>q':
        terminate_the_program()
    return user_mode_input if user_mode_input.lower() in ['r','w','a','x'] else None

def get_file_mode_input():
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


def open_file_in_read_mode(file_name):
    file_obj = open(file_name)
    return file_obj

def open_file_in_write_mode(file_name):
    file_obj = open(file_name,'w')
    return file_obj

def open_file_in_append_mode(file_name):
    file_obj = open(file_name,'a')
    return file_obj
    
def open_file_in_exclusive_mode(file_name):
    file_obj = open(file_name,'x')
    return file_obj

def open_file_with_user_mode(file_name):
    mode = get_file_mode_input()

    if mode == 'r':
        return open_file_in_read_mode(file_name)
    elif mode == 'a':
        return open_file_in_append_mode(file_name)
    elif mode == 'w':
        return open_file_in_write_mode(file_name)
    else:
        return open_file_in_exclusive_mode(file_name)



