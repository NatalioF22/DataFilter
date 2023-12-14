from io import StringIO
from File_Handler import *
from datetime import datetime
from pytest import MonkeyPatch as monckeypatch
import pytest

# TODO GATHER ALL THE TEST FUNCTIONS AND PUT IT IN ONE FILE. WITH THE MOST ASSERT STATEMENT.

def test_output_text_file_name():
    # Create a mock datetime object for testing purposes
    mock_datetime = datetime(2023, 12, 5, 15, 30, 45, 231186)

    # Call the function with the mock datetime object
    result = output_text_file_name(mock_datetime)

    # Check the result
    assert result == "2023-12-05_15_30_45_231186"

def test_check_if_file_exists():
    mock_file = "test_file.txt"
    result = check_if_file_exists(mock_file)
    wrong_result = check_if_file_exists("doesnt_exist.txt")

    assert result == True
    assert wrong_result == None
    
    

def test_prompt_for_valid_file_name_input(capsys, monkeypatch):
    test_input = 'test_file.txt'
    monkeypatch.setattr('builtins.input', lambda _: test_input)
    # Call the function
    result = prompt_for_valid_file_name_input()
    # Capture the output
    captured = capsys.readouterr()
  # Check the result and output
    assert result == 'test_file.txt'
    assert "Enter a valid file name" in captured.out
    assert "Target file: test_file.txt" in captured.out

    wrong_input = 'filedoes_exist.txt'
    monkeypatch.setattr('builtins.input', lambda _: test_input)
    result = prompt_for_valid_file_name_input()
    captured = capsys.readouterr()
    verify_file = check_if_file_exists(wrong_input)
    assert verify_file == None


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

def test_prompt_for_file_name(monkeypatch, capsys):
    test_input = 'test_file.txt'
    monkeypatch.setattr('builtins.input', lambda _: test_input)
    result = get_valid_file_name_loop()
    captured = capsys.readouterr()
    assert result == 'test_file.txt'
    assert "Enter a valid file name" in captured.out
    assert "Target file: test_file.txt" in captured.out



def test_check_valid_mode():
    # Test with a valid mode
    valid_mode_input = 'r'
    result = check_valid_mode(valid_mode_input)
    assert result == valid_mode_input

    # Test with an invalid mode
    invalid_mode_input = 'z'
    invalid_mode_input_result = check_valid_mode(invalid_mode_input)
    assert invalid_mode_input_result == None

    # Test with '>q' to terminate the program
    with pytest.raises(SystemExit):
        check_valid_mode('>q')

    

def test_get_file_mode_input(monkeypatch, capsys):
    # Test with a valid mode
    valid_mode_input = 'r'
    monkeypatch.setattr('builtins.input', lambda _: valid_mode_input)
    result = get_file_mode_input()
    captured = capsys.readouterr()
    assert result == valid_mode_input
    assert "File Mode: r" in captured.out

    """
    # Test with an invalid mode
    invalid_mode_input = 'z'
    monkeypatch.setattr('builtins.input', lambda _: invalid_mode_input)
    result = get_file_mode_input()
    captured = capsys.readouterr()
    assert result is None
    assert "INVALID MODE!" in captured.out"""

def test_open_file_in_read_mode():
    """
    This fucntion teste both functions: open_file_in_read_mode and   open_file_in_write_mode

    """
    # Create a temporary file with some content
    test_file_variable = "test_file.txt"
    test_file = open(test_file_variable,"w")
    test_file.write("Hello, World!")
    test_file.close()

    # Test opening the file in read mode
    test_result = open_file_in_read_mode(test_file_variable)

    # Verify that the result is of the expected type

    # Verify that the file content is as expected
    content = test_result.read()
    print(content)
    assert content == "Hello, World!"

    # Close the file
    test_result.close()


def test_open_file_in_append_mode():
    test_file_variable = "test_file.txt"
    test_file = open(test_file_variable,"a")
    test_file.write("New text added!!!")
    test_file.close()

    read_test_file = open(test_file_variable, "r")
    result  = read_test_file.read()
    assert "New text added!!!" in result
    read_test_file.close()



    


    
    


