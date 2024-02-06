"""
Author: Charlie Doherty
KUID: 3115329
Date: 2/06/24
Lab: 02
Last modified: 02/06/24
Purpose: Create linked lists to simulate the processes of the cpu
"""


def get_calls():
    """Reads the input file and returns a list of calls"""

    file_name = input("Enter the file name: ")
    with open(file_name, "r") as file:
        lines = file.readlines()

    lines = [line.strip for line in lines]
    return lines


if __name__ == "__main__":
    calls = get_calls()
