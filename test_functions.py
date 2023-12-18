"""
Project 1.2
Author: Natalio Gomes
Class: COMP390
Section: 002
Date: December 18th, 2023

Functionality:
    This file contains functions for handling and filtering meteor data. It provides functionality to prompt the user for
    filtering choices, get input for mass and year limits, extract meteor data from a file, create MeteorDataEntry objects,
    display and write headers, and format and print filtered meteor data to the terminal or a text file.

3 MAIN Test Functions:
    - test_output_text_file_name: Tests the output_text_file_name function with different datetime objects.
    - test_check_if_file_exists: Tests the check_if_file_exists function with various file name types.
    - test_check_valid_mode: Tests the check_valid_mode function with different mode inputs.
"""
from File_Handler import *
from datetime import datetime
import pytest


def test_output_text_file_name():
    """
    Test the output_text_file_name function with different datetime objects.

    Test Cases:
    1. Test with a different datetime object.
    2. Test with a datetime object with different values.
    3. Test with a datetime object having zero values.
    4. Test with a datetime object having maximum values.
    5. Test with a datetime object having single-digit values.
    """
    # Test with a different datetime object
    mock_datetime_2 = datetime(2022, 1, 15, 8, 12, 30, 500000)
    result_2 = output_text_file_name(mock_datetime_2)
    assert result_2 == "2022-01-15_08_12_30_500000.txt"

    # Test with a datetime object with different values
    mock_datetime_3 = datetime(2023, 5, 20, 10, 45, 15, 123456)
    result_3 = output_text_file_name(mock_datetime_3)
    assert result_3 == "2023-05-20_10_45_15_123456.txt"


def test_check_if_file_exists():
    """
    Test the check_if_file_exists function with various file name types.

    Test Cases:
    1. Test with a valid string file name.
    2. Test with an invalid string file name.
    3. Test with an invalid integer file name.
    4. Test with a boolean file name.
    5. Test with a list file name.
    6. Test with a dictionary file name.
    7. Test with None as a file name.
    """
    # Test with a valid string file name
    valid_file_name_str = "TestDir/file_exists.txt"
    result_str = check_if_file_exists(valid_file_name_str)
    assert result_str is True

    # Test with an invalid string file name
    invalid_file_name_str = "doesnt_exist.txt"
    wrong_result_str = check_if_file_exists(invalid_file_name_str)
    assert wrong_result_str is None

    # Test with an invalid integer file name
    invalid_file_name_int = 1213
    wrong_result_int = check_if_file_exists(invalid_file_name_int)
    assert wrong_result_int is None  # Should be None, not True

    # Test with a boolean file name
    invalid_file_name_bool = True
    wrong_result_bool = check_if_file_exists(invalid_file_name_bool)
    assert wrong_result_bool is True  # returns true because the original function returns true

    # Test with a list file name
    invalid_file_name_list = ['file', 'not', 'found']
    with pytest.raises(TypeError):
        check_if_file_exists(invalid_file_name_list)

    # Test with a dictionary file name
    invalid_file_name_dict = {'file': 'not_found.txt'}
    with pytest.raises(TypeError):
        check_if_file_exists(invalid_file_name_dict)

    # Test with None as a file name
    invalid_file_name_none = None
    with pytest.raises(TypeError):
        check_if_file_exists(invalid_file_name_none)


def test_check_valid_mode():
    """
    Test the check_valid_mode function with different mode inputs.

    Test Cases:
    1. Test with a valid lowercase mode.
    2. Test with a valid uppercase mode.
    3. Test with a valid mixed-case mode.
    4. Test with an invalid mode.
    5. Test with '>q' to terminate the program.
    6. Test with a numeric input.
    7. Test with a boolean input.
    8. Test with a list input.
    9. Test with a dictionary input.
    10. Test with integers.
    """
    # Test with a valid lowercase mode
    valid_mode_input_lower = 'r'
    result_lower = check_valid_mode(valid_mode_input_lower)
    assert result_lower == valid_mode_input_lower

    # Test with a valid uppercase mode
    valid_mode_input_upper = 'W'
    result_upper = check_valid_mode(valid_mode_input_upper)
    assert result_upper == valid_mode_input_upper.lower()

    # Test with a valid mixed-case mode
    valid_mode_input_mixed = 'a'
    result_mixed = check_valid_mode(valid_mode_input_mixed)
    assert result_mixed == valid_mode_input_mixed

    # Test with an invalid mode
    invalid_mode_input = 'z'
    invalid_mode_input_result = check_valid_mode(invalid_mode_input)
    assert invalid_mode_input_result is None

    # Test with '>q' to terminate the program
    with pytest.raises(SystemExit):
        check_valid_mode('>Q')

    # Test with a numeric input
    numeric_mode_input = '123'
    numeric_mode_input_result = check_valid_mode(numeric_mode_input)
    assert numeric_mode_input_result is None

    # Test with a boolean input
    bool_mode_input = True
    with pytest.raises(AttributeError):
        check_valid_mode(bool_mode_input)

    # Test with a list input
    list_mode_input = ['a', 'b', 'c']
    with pytest.raises(AttributeError):
        check_valid_mode(list_mode_input)

    # Test with a dictionary input
    dict_mode_input = {'key': 'value'}
    with pytest.raises(AttributeError):
        check_valid_mode(dict_mode_input)

    # Test with integers
    int_mode_input = 12
    dict_mode_input = {'key': 'value'}
    with pytest.raises(AttributeError):
        check_valid_mode(int_mode_input)


