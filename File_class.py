#!/usr/bin/env python3
"""
Contains info on what info to print to the user
Contains values to help debug any errors within the program / file
"""


class File:
    """
    info on file such as current X/Y Axis
    access to the file and what to debug
    """

    def __init__(self, row_y, column_x, f):
        self.y = row_y
        self.x = column_x
        self.f = f

    def get_info(self, des):
        switcher = {
            'x': self.x,
            'y': self.y,
            'f': self.f,
        }
        return (switcher.get(des))

    def set_info(self, des, new_val):
        if (des == "x"):
            self.x = new_val
            return (0)
        if (des == "y"):
            self.y = new_val
            return (0)
        if (des == "f"):
            self.f = new_val
            return (0)
        return (1)
