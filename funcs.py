#!/usr/bin/env python3
# This script holds useful system functions to get info from file passed.

import os


def get_file_name(var):
    """
    return the file name passed to program
    """
    return (os.path.basename(var))


def begin_prompt():
    """
    Function to prompt user on applying optional updates in a new version
    of the excel file given.
    """
    print("Enable new file to be created in same directory?")
    print("This will create a new file with _new.xslx")
    answer = input("Enable (Y/N): ")
    if ("Y" in answer or "y" in answer):
        return (True)
    return (False)


def findBlank(ws, column_max, row_max):
    """
    Determines the last row where there is no first & last name
    present to show where the filled data ends.
    """
    row_end = 1
    for column_x in range(2, 3):
        for row_y in range(1, row_max):
            if (ws.cell(row_y, column_x).value is None):
                if (ws.cell(row_y, column_x + 1).value is None):
                    if (ws.cell(row_y, column_x + 2).value is None):
                        return (row_end)
            row_end += 1
    return (row_end)
