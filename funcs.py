#!/usr/bin/env python3
# This script holds useful system functions to get info from file passed.

import os


def get_file_name(var):
    """
    return the file name passed to program
    """
    return (os.path.basename(var))


def begin_prompt(info):
    """
    Function to prompt user on applying optional updates in a new version
    of the excel file given.
    """
    """
    print("Enable new file to be created in same directory?")
    print("This will create a new file with _new.xslx")
    answer = input("Enable (Y/N): ")
    if ("Y" in answer or "y" in answer):
        print("Enabled!")
    """

    print ( " _       ____________________________    __       ____  ___  _________       ________  ________________ __ __________ ")
    print ( "| |     / / ____/ ___/_  __/ ____/   |  / /      / __ \/   |/_  __/   |     / ____/ / / / ____/ ____/ //_// ____/ __ \\")
    print ( "| | /| / / __/  \__ \ / / / /   / /| | / /      / / / / /| | / / / /| |    / /   / /_/ / __/ / /   / ,<  / __/ / /_/ /")
    print ( "| |/ |/ / /___ ___/ // / / /___/ ___ |/ /___   / /_/ / ___ |/ / / ___ |   / /___/ __  / /___/ /___/ /| |/ /___/ _, _/ ")
    print ( "|__/|__/_____//____//_/  \____/_/  |_/_____/  /_____/_/  |_/_/ /_/  |_|   \____/_/ /_/_____/\____/_/ |_/_____/_/ |_|  ")
    print ("                                                                                                                      ")

    print("")
    print("Debug info causing errors to program?")
    errno_answer  = input("Enable (Y/N): ")
    if ("Y" in errno_answer or "y" in errno_answer):
        print("Enabled!")
        info.set_info("e", 1)
    print("Creating txt file!")
    return (True)


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
