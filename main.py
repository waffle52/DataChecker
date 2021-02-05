#!/usr/bin/env python3
# This script checks every cell in a passed excel file for any Errors
# GNU GPLv3
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl import utils
from correction_funcs import *
from funcs import *
from datatypes import *
from File_class import *
import sys


def main():
    """
    Main code to check parameters exist and check if failures exist
    within the file.
    """

    # check argument length to make sure file is passed
    if (len(sys.argv) != 2):
        print("USAGE: Python3 main.py PATH")
        sys.exit(1)
    file_name = get_file_name(sys.argv[1])

    # check if the file passed is an excel file
    try:
        wb = load_workbook(filename=sys.argv[1])
    except (FileNotFoundError, utils.exceptions.InvalidFileException):
        print("Cannot open. Program only designed for excel files")
        sys.exit(1)

    # variables
    ws = wb.worksheets[0]
    func_num = 0
    first_try = 0
    track = 1
    row_max = ws.max_row + 1
    column_max = ws.max_column + 1
    column_name = ws.cell(1, 1).value
    prev = column_name
    test = False
    stop = findBlank(ws, column_max, row_max) - 1

    # create Results.txt file to report any errors
    f = open("Results.txt", "w")
    f.write("WESTCAL CHECKER ERRORS:\n")
    f.close()
    f = open("Results.txt", "a")
    info = File(0, 0, f, 0)
    begin_prompt(info)

    # loop through length of data present in the excel file passed
    for column_x in range(1, column_max):
        info.set_info('x', column_x)
        info.set_info("name", ws.cell(1, column_x).value)
        for row_y in range(2, row_max):
            info.set_info('y', row_y)
            column_name = ws.cell(1, column_x).value
            if (track == stop):
                track = 1
                break
            if (column_name != prev):
                prev = column_name
                func_num += 1
            if (func_list[func_num](ws.cell(row_y, column_x).value, info) is False):
                mark(column_name, column_x, row_y, f)
            track += 1
    print("Done!")
    f.close()


def mark(column_name, x, y, f):
    """
    mark in notes file location of error
    """
    f.write("\tError with {} value: Column: {} - Row: {}\n"
            .format(column_name, x, y))


main()
