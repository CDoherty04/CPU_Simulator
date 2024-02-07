"""
Author: Charlie Doherty
KUID: 3115329
Date: 2/06/24
Lab: 02
Last modified: 02/06/24
Purpose: Create linked lists to simulate the processes of the cpu
"""
import cpuscheduler


def get_calls():
    """Reads the input file and returns a list of calls"""

    file_name = input("Enter the file name: ")
    with open(file_name, "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    return lines


if __name__ == "__main__":
    scheduler = cpuscheduler.CPUScheduler()
    calls = get_calls()
    for call in calls:
        call = call.split(" ")
        match call[0]:
            case "START":
                """A new process is created and added to the queue. All processes start with a "main" as their first 
                function call. Print a message to the screen indicating which process was added to the queue."""

                scheduler.add_process(call[1])
                print(call[1], "was added to the queue")
