"""
Author: Charlie Doherty
KUID: 3115329
Date: 2/06/24
Lab: 02
Last modified: 02/08/24
Purpose: Create linked lists to simulate the processes of the cpu

Run driver to execute the program and modify commands.txt to change the terminal's output
"""
from executive import Executive

if __name__ == "__main__":
    """Run this to run the program"""

    while True:
        try:

            file_name = input("Enter the file name: ")
            my_exec = Executive(file_name)
            my_exec.run()
            break

        except FileNotFoundError:
            print("That file doesn't seem to exist, try again")
