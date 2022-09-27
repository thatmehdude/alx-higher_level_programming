#!/usr/bin/python3

"""module that contains a function that reads from a file"""


def read_file(filename=""):
    """
    function that reads from a file
    Args:
        filename: filename
    Raises
        Exception: when the file can be opened
    """
    with open(filename, 'r') as f:
        read_data = f.read()
        print(read_data, end='')
