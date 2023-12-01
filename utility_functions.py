"""
This module assists with converting a string to an int or
float.
Only the convert_string_to_numerical() function is available to outside files
"""


def _string_is_numerical(in_string):
    """ returns True if the incoming parameter can be converted to float (i.e. is a number)
    returns False otherwise - checks for TypeError and ValueError on incoming value """

    try:
        float(in_string)
        return True
    except TypeError:
        return False
    except ValueError:
        return False


def convert_string_to_numerical(in_string):
    """ this function converts a string to a numerical value (to either an int or float)
        'None' is returned if the incoming string is not in the form of an int or float """

    if _string_is_numerical(in_string):
        return float(in_string)
    return None


def _insert_none_data(data_list):
    """ converts empty string '' and '\n' elements in the list to 'None' - returns the modified list """

    index_pointer = 0
    for element in data_list:
        # check to see if there is nothing (empty string) or a '\n' for an element
        if element == '' or element == '\n':
            # if an empty string or '\n' is found, replace that element with 'None'
            data_list[index_pointer] = None
        index_pointer += 1
    return data_list


def clean_data_list(data_str):
    """ this function takes a data string as its single parameter - it cleans the data string - removes the newline
    character and splits the data string on the tab separation - this creates a list. This list is then processed
    by replacing all empty strings and '\n' elements with a None value - the clean list is then returned """

    strip_line = data_str.strip('\n')
    # get a tab separated list from the file line
    tab_sep_line = strip_line.split('\t')
    # convert missing data point to None in the list - this applies to '' and '\n' for the missing Counties data
    clean_data = _insert_none_data(tab_sep_line)
    return clean_data
