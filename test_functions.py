from io import StringIO
from File_Handler import *
from datetime import datetime
import pytest


def test_output_text_file_name():
    # Test with a different datetime object
    mock_datetime_2 = datetime(2022, 1, 15, 8, 12, 30, 500000)
    result_2 = output_text_file_name(mock_datetime_2)
    assert result_2 == "2022-01-15_08_12_30_500000"

    # Test with a datetime object with different values
    mock_datetime_3 = datetime(2023, 5, 20, 10, 45, 15, 123456)
    result_3 = output_text_file_name(mock_datetime_3)
    assert result_3 == "2023-05-20_10_45_15_123456"

    # Test with a datetime object having zero values
    mock_datetime_4 = datetime(2000, 1, 1, 0, 0, 0, 0)
    result_4 = output_text_file_name(mock_datetime_4)
    assert result_4 == "2000-01-01_00_00_00_0"

    # Test with a datetime object having maximum values
    mock_datetime_5 = datetime(9999, 12, 31, 23, 59, 59, 999999)
    result_5 = output_text_file_name(mock_datetime_5)
    assert result_5 == "9999-12-31_23_59_59_999999"

    # Test with a datetime object having single-digit values
    mock_datetime_6 = datetime(2023, 1, 2, 3, 4, 5, 6)
    result_6 = output_text_file_name(mock_datetime_6)
    assert result_6 == "2023-01-02_03_04_05_000006"


def test_check_if_file_exists():
    # Test with a valid string file name
    valid_file_name_str = "test_file.txt"
    result_str = check_if_file_exists(valid_file_name_str)
    assert result_str is True

    # Test with an invalid string file name
    invalid_file_name_str = "doesnt_exist.txt"
    wrong_result_str = check_if_file_exists(invalid_file_name_str)
    assert wrong_result_str is None

    # Test with an invalid integer file name
    invalid_file_name_int = 1213
    wrong_result_int = check_if_file_exists(invalid_file_name_int)
    assert wrong_result_int is None

    # Test with a boolean file name
    invalid_file_name_bool = True
    wrong_result_bool = check_if_file_exists(invalid_file_name_bool)
    assert wrong_result_bool is None

    # Test with a list file name
    invalid_file_name_list = ['file', 'not', 'found']
    wrong_result_list = check_if_file_exists(invalid_file_name_list)
    assert wrong_result_list is None

    # Test with a dictionary file name
    invalid_file_name_dict = {'file': 'not_found.txt'}
    wrong_result_dict = check_if_file_exists(invalid_file_name_dict)
    assert wrong_result_dict is None

    # Test with None as a file name
    invalid_file_name_none = None
    wrong_result_none = check_if_file_exists(invalid_file_name_none)
    assert wrong_result_none is None

    

def test_prompt_for_valid_file_name_input(capsys, monkeypatch):
    # Test with a valid file name
    valid_test_input = 'test_file.txt'
    monkeypatch.setattr('builtins.input', lambda _: valid_test_input)
    result_valid = prompt_for_valid_file_name_input()
    captured_valid = capsys.readouterr()
    assert result_valid == valid_test_input
    assert "Enter a valid file name" in captured_valid.out
    assert "Target file: test_file.txt" in captured_valid.out

    # Test with an invalid file name (filedoes_exist.txt)
    invalid_test_input = 'filedoes_exist.txt'
    monkeypatch.setattr('builtins.input', lambda _: invalid_test_input)
    result_invalid = prompt_for_valid_file_name_input()
    captured_invalid = capsys.readouterr()
    verify_file_invalid = check_if_file_exists(invalid_test_input)
    assert result_invalid is None  # Since the function prompts until a valid name is given
    assert "Enter a valid file name" in captured_invalid.out
    assert "File does not exist" in captured_invalid.out
    assert verify_file_invalid is None

    # Test with another valid file name
    valid_test_input_2 = 'another_test_file.txt'
    monkeypatch.setattr('builtins.input', lambda _: valid_test_input_2)
    result_valid_2 = prompt_for_valid_file_name_input()
    captured_valid_2 = capsys.readouterr()
    assert result_valid_2 == valid_test_input_2
    assert "Enter a valid file name" in captured_valid_2.out
    assert "Target file: another_test_file.txt" in captured_valid_2.out


def test_get_valid_file_name_loop(monkeypatch, capsys):
    # Simulate user input for a correct filename
    test_input = 'test_file.txt'
    monkeypatch.setattr('builtins.input', lambda _: test_input)
    
    # Call the function
    result = get_valid_file_name_loop()
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Check the result and output for the correct filename
    assert result == 'test_file.txt'
    assert "Enter a valid file name" in captured.out
    assert "Target file: test_file.txt" in captured.out


def test_check_valid_mode():
    # Test with a valid lowercase mode
    valid_mode_input_lower = 'r'
    result_lower = check_valid_mode(valid_mode_input_lower)
    assert result_lower == valid_mode_input_lower

    # Test with a valid uppercase mode
    valid_mode_input_upper = 'W'
    result_upper = check_valid_mode(valid_mode_input_upper)
    assert result_upper == valid_mode_input_upper

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
        check_valid_mode('>q')

    # Test with a numeric input
    numeric_mode_input = '123'
    numeric_mode_input_result = check_valid_mode(numeric_mode_input)
    assert numeric_mode_input_result is None

    # Test with a boolean input
    bool_mode_input = True
    bool_mode_input_result = check_valid_mode(bool_mode_input)
    assert bool_mode_input_result is None

    # Test with a list input
    list_mode_input = ['a', 'b', 'c']
    list_mode_input_result = check_valid_mode(list_mode_input)
    assert list_mode_input_result is None

    # Test with a dictionary input
    dict_mode_input = {'key': 'value'}
    dict_mode_input_result = check_valid_mode(dict_mode_input)
    assert dict_mode_input_result is None

    # Test with a integers
    int_mode_input = 12
    dict_mode_input_result = check_valid_mode(int_mode_input)
    assert dict_mode_input_result is None

