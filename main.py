"""
Author: Charlie Doherty
KUID: 3115329
Date: 2/06/24
Lab: 02
Last modified: 02/06/24
Purpose: Create linked lists to simulate the processes of the cpu
"""
import cpuscheduler
import process
import function


def get_calls():
    """Reads the input file and returns a list of commands"""

    file_name = input("Enter the file name: ")
    with open(file_name, "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    return lines


if __name__ == "__main__":
    """Main function: calls other functions to run the program"""
    scheduler = cpuscheduler.CPUScheduler()
    commands = get_calls()
    for command in commands:
        command = command.split(" ")

        match command[0]:
            case "START":
                """A new process is created and added to the queue. All processes start with a "main" as their first 
                function command. Print a message to the screen indicating which process was added to the queue."""

                app = process.Process(command[1])
                scheduler.add_process(app)
                print(command[1], "was added to the queue")

            case "CALL":
                """The process at the front of the queue gets some CPU time and calls a function. 
                This puts that function on the call stack for that process. 
                After the call is made, that process goes to the back of the line. 
                Print to the screen indicating which process called the function and the name of the function."""

                # Create a function with command[1] being the name and command[2] being exception handling boolean
                if command[2] == "yes":
                    func = function.Function(command[1], True)
                else:
                    func = function.Function(command[1], False)

                print(f"{scheduler.get_process_queue().get_front().get_value().get_name()} called the "
                      f"function \"{command[1]}\"")

                scheduler.give_cpu_time(func)

        # print(scheduler.get_process_queue().get_front().get_value())
        # print(scheduler.get_process_queue().get_back().get_value())
