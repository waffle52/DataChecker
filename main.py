#!/usr/bin/env python3
# This script checks every cell in the Westcal Student Excel file for any Errors
# GNU GPLv3
from openpyxl import Workbook
from openpyxl import load_workbook
from check_funcs import *
from correction_funcs import *
from funcs import *
import sys

def main():
    """
    Main code to check parameters exist and check if failed file exists
    """

    # check argument length
    if (len(sys.argv) != 2):
        print ("USAGE: Python3 main.py PATH")
        sys.exit(1)
    file_name = get_file_name(sys.argv[1])
    new_file = ""
    # check if new file is to be created from old one with updated changes
    # new_file = begin_prompt()
    # check if the file passed is an excel file
    try:
        wb = load_workbook(filename=sys.argv[1])
    except:
        print("Cannot open. Program only designed for excel files EX: .xlsx")
        sys.exit(1)

    ws = wb.worksheets[0]
    func_track = 0
    first_try = 0
    track = 1
    list_of_functions = [ ID_CHECK, SALUTION_CHECK, FIRST_NAME_CHECK, MIDDLE_NAME_CHECK, LAST_NAME_CHECK, SUFFIX_CHECK, PARTNER_CHECK, SCHOOL_CHECK, INTERNSHIP_CHECK, INTERNSHIP_TYPE_CHECK, PLACEMENT_CHECK, PLACEMENT_DATE_CHECK, END_DATE_CHECK, NEW_SOURCE_CHECK, STATUS_CHECK, FIRST_GEN_CHECK, INTERNATIONAL_CHECK, GENDER_CHECK, AGE_CHECK, ETHNICITY_CHECK, REENTRY_CHECK, FOSTER_CHECK, OCCUPATION_CHECK, COMPANY_CHECK, EMAIL_CHECK, EMAIL_CHECK, WEBSITE_CHECK, WEBSITE_CHECK, PHONE_NUMBER_CHECK, PHONE_NUMBER_CHECK, PHONE_NUMBER_CHECK, PHONE_NUMBER_CHECK, PHONE_NUMBER_CHECK, PHONE_NUMBER_CHECK, PHONE_NUMBER_CHECK, FIRST_CONTACT_CHECK, BEST_PERSON_CHECK, ADDRESS_CHECK, SUITE_CHECK, CITY_CHECK, STATE_CHECK, ZIP_CHECK, COUNTRY_CHECK, HOMELESS_CHECK, SOURCE_CHECK, VET_CHECK ]

    row_max = ws.max_row + 1
    column_max = ws.max_column + 1
    column_name = ws.cell(1, 1).value
    prev = column_name
    test = False
    stop = findBlank(ws, column_max, row_max) - 1
    f = open("errors.txt", "w")
    f.write("WESTCAL CHECKER ERRORS:\n")
    f.close()
    f = open("errors.txt", "a")

    for column_x in range (1, column_max):
        for row_y in range (2, row_max):
            column_name = ws.cell(1, column_x).value
            if (track == stop):
                track = 1
                break
            if (column_name != prev):
                prev = column_name
                func_track += 1
            if (list_of_functions[func_track](ws.cell(row_y, column_x).value) == False):
                mark(column_name, column_x, row_y, f)
            track += 1
    f.close()

def mark(column_name, x, y, f):
    # mark in notes file location of error
    f.write("\tError with {} value: Column: {} - Row: {}\n".format(column_name, x, y))

def findBlank(ws, column_max, row_max):
    row_end = 1
    for column_x in range (2, 3):
        for row_y in range (1, row_max):
            if (ws.cell(row_y, column_x).value == None and ws.cell(row_y, column_x + 1).value == None and ws.cell(row_y, column_x + 2).value == None):
                return (row_end)
            row_end += 1
    return (row_end)

def begin_prompt():
    # add ask user for end of line for stop variable?
    print("Enable zip code rewrite?")
    print("This will create a new file with _new.xslx at the end in the folder of the file given with each zip code converted to nine-digit based zip if address is present in file")
    answer = input("Enable (Y/N): ")
    if ("Y" in answer or "y" in answer):
        return (True)
    return (False)

main()
