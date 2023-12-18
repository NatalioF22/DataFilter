"""
    Project 1.2
    Author: Natalio Gomes
    Class: COMP390
    Section: 002
    Date: December 18th, 2023

    Excel Writer

    This module provides functions for creating and writing meteor data to Excel files.

"""
from xlwt import Workbook
from File_Handler import output_text_file_name
import datetime


def create_excel_workbook() -> object:
    """
    Create a new Excel workbook.

    Returns:
        Workbook: Excel workbook object.
    """
    return Workbook()


def add_worksheet_to_workbook(workbook: object, sheet_name: object) -> object:
    """
    Add a new worksheet to the Excel workbook.

    Args:
        workbook (Workbook): Excel workbook object.
        sheet_name (str): Name of the worksheet.

    Returns:
        Worksheet: Excel worksheet object.
    """
    return workbook.add_sheet(sheet_name)


def write_header_row(worksheet: object, header: object) -> None:
    """
    Write the header row to the Excel worksheet.

    Args:
        worksheet (Worksheet): Excel worksheet object.
        header (list): List of header values.
    """
    for col, value in enumerate(header):
        worksheet.write(0, col, value)


def write_data_rows(worksheet: object, filtered_list: list) -> None:
    """
    Write data rows to the Excel worksheet.

    Args:
        worksheet (Worksheet): Excel worksheet object.
        filtered_list (list): List of meteor objects to be written to the worksheet.
    """
    for row, meteor in enumerate(filtered_list, start=1):
        data_row = [
            meteor.get_name(), meteor.get_id(), meteor.get_name_type(),
            meteor.get_rec_class(), meteor.get_mass(), meteor.get_fall(),
            meteor.get_year(), meteor.get_rec_lat(), meteor.get_rec_long(),
            meteor.get_geo_location(), meteor.get_counties(), meteor.get_states()
        ]
        for col, value in enumerate(data_row):
            worksheet.write(row, col, value)


def save_workbook(workbook: object, file_name: str) -> None:
    """
    Save the Excel workbook to a file.

    Args:
        workbook (Workbook): Excel workbook object.
        file_name (str): Name of the output Excel file.
    """
    workbook.save(f"{file_name}.xls")


def write_filtered_mass_data_to_excel_file(meteor_list: list, limits: list) -> None:
    """
    Write filtered meteor data based on mass to an Excel file.

    Args:
        meteor_list (list): List of meteor objects.
        limits (list): List of mass limits for filtering.
    """
    filtered_list = filter_meteors_by_mass(meteor_list, limits)

    wb = create_excel_workbook()
    ws = add_worksheet_to_workbook(wb, 'Meteor Data')

    header = ['Name', 'ID', 'Name Type', 'Rec Class', 'Mass (g)', 'Fall', 'Year', 'Rec Lat', 'Rec Long', 'Geo Location', 'counties', 'States']
    write_header_row(ws, header)

    write_data_rows(ws, filtered_list)
    current_datetime = datetime.datetime.now()
    file_name = output_text_file_name(current_datetime,'')
    save_workbook(wb, file_name)



def filter_meteors_by_mass(meteor_list: list, limits: list) -> list[object]:
    """
    Filter meteor data by mass within the specified limits.

    Args:
        meteor_list (list): List of meteor objects.
        limits (list): List of mass limits for filtering.

    Returns:
        list: List of filtered meteor objects.
    """
    return [meteor for meteor in meteor_list if limits[0] <= meteor.get_mass() <= limits[1]]


def write_filtered_year_data_to_excel_file(meteor_list: list, limits: list) -> None:
    """
    Write filtered meteor data based on year to an Excel file.

    Args:
        meteor_list (list): List of meteor objects.
        limits (list): List of year limits for filtering.
    """
    filtered_list = filter_meteors_by_year(meteor_list, limits)

    wb = create_excel_workbook()
    ws = add_worksheet_to_workbook(wb, 'Meteor Data')

    header = ['Name', 'ID', 'Name Type', 'Rec Class', 'Mass (g)', 'Fall', 'Year', 'Rec Lat', 'Rec Long', 'Geo Location',
              'counties', 'States']
    write_header_row(ws, header)

    write_data_rows(ws, filtered_list)
    current_datetime = datetime.datetime.now()
    file_name = output_text_file_name(current_datetime, '')
    save_workbook(wb, file_name)


def filter_meteors_by_year(meteor_list: list, limits: list) -> list[object]:
    """
    Filter meteor data by year within the specified limits.

    Args:
        meteor_list (list): List of meteor objects.
        limits (list): List of year limits for filtering.

    Returns:
        list: List of filtered meteor objects.
    """
    return [meteor for meteor in meteor_list if limits[0] <= meteor.get_year() <= limits[1]]
