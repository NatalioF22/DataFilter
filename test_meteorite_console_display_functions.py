import pytest
from meteorite_console_display import *
from ColoredText import TerminalColors

def test_print_welcome_message(capsys):
    print_welcome_message()
    captured = capsys.readouterr()
    assert "Meteorite Filtering Application" in captured.out
    assert "Author: Natalio Gomes" in captured.out
    assert "December 2023" in captured.out

def test_print_file_opening_modes(capsys):
    print_file_opening_modes()
    captured = capsys.readouterr()
    assert "What mode would you like to open the file with?" in captured.out
    assert '"r" - open for reading (default)' in captured.out
    assert '"w" - open for writing, truncating the file first.' in captured.out

def test_print_filter_menu_options(capsys):
    print_filter_menu_options()
    captured = capsys.readouterr()
    assert "What attribute would you like to filter the data on?" in captured.out
    assert "1. Meteor MASS(g)" in captured.out
    assert "2. The YEAR the meteor fell to earth" in captured.out

def test_terminate_the_program(capsys):
    with pytest.raises(SystemExit):
        terminate_the_program()
    captured = capsys.readouterr()
    assert "The program is now exiting... GOODBYE!" in captured.out

def test_print_the_output_option(capsys):
    print_the_output_option()
    captured = capsys.readouterr()
    assert "How would you like to output the filter results?" in captured.out
    assert "1. On Screen (in terminal)" in captured.out
    assert "2. To a TEXT file" in captured.out
    assert "3. To an EXCEL file" in captured.out

# Add more tests as needed for other functions or scenarios
