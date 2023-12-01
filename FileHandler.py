"""
    Project 1.2
    Author: Natalio Gomes
    Class: COMP390
    Section: 002
    Date: December 5th, 2023
"""
import os
from meteor_data_class import MeteorDataEntry
from ColoredText import TerminalColors
from Messages import list_of_strings



def check_if_file_exists(file_name:str) -> bool:
    if os.path.exists(file_name): 
        print(TerminalColors.GREEN + f"\nTarget file: {file_name}\n" + TerminalColors.RESET)
        return True
    else:
        print(TerminalColors.RED + f"\nERROR: TARGET FILE NAME: '{file_name}' IS NOT VALID!\n" + TerminalColors.RESET)
    
    
def terminate_the_program() -> exit:
    print(TerminalColors.RESET + "\nThe program is now exiting... GOODBYE!\n")
    exit()
    

def file_handling(file_name:str, choice: str):
    if choice == 'r': return file_read_mode(file_name)
    elif choice == 'w':return file_write_mode(file_name)
    elif choice == 'x':return file_exclusive_creation_mode(file_name)
    else: return file_append_mode(file_name)


def prompt_for_file_name():
    while True:
        print("Enter a valid file name (ex. 'file_name.txt') with its file extension (if applicable) |or| Enter '>q' or '>Q' to quit: "  , end="")
        file_name = input(TerminalColors.GREEN)
    
        if file_name == ">q" or file_name == ">Q": terminate_the_program()
        elif check_if_file_exists(file_name): return file_name
        
    
def file_mode(file_name:str) -> str:
    while True:
        print(list_of_strings[2]['file_mode_options'], end="")
        user_input_choice = input("Mode ->")
        if user_input_choice.lower() in ['r','w','x','a']: 
            print(TerminalColors. GREEN +f"\nFile mode: {user_input_choice}\n"+ TerminalColors.RESET)
            return file_handling(file_name, user_input_choice)
        elif user_input_choice.lower() == '>q': terminate_the_program()


def file_read_mode(file_name:str) -> str:
    file_obj = open(file_name)
    return file_obj


def file_write_mode(file_name):
    while True:
        print(TerminalColors.RED + "ATENTION: IF YOU PROCCEED TO OPEN THIS FILE, YOU WILL ERASE ALL THE CONTENT WITHIN IT." + TerminalColors.RESET)
        user_choice = input(TerminalColors.WARNING + "WOULD YOU LIKE TO PROCEED?(Y(es) or N(o))\nAnswer: " + TerminalColors.RESET)
        if user_choice.lower() == 'y':
            file_obj = open(file_name, 'w')
            print(TerminalColors.GREEN + "READY TO USE")
            return file_obj
        elif user_choice.lower() == 'n': break
        else: print(TerminalColors. RED + "INVALID CHOICE" + TerminalColors.RESET)


def file_exclusive_creation_mode(file_name):
    file_obj = open(file_name, 'x')
    return file_obj


def file_append_mode(file_name):
    file_obj = open(file_name, 'a')
    return file_obj
