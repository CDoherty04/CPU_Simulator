import cpuscheduler
import process
import function


def get_calls(file_name):
    """Reads the input file and returns a list of commands"""

    with open(file_name, "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    return lines


def starts(scheduler, name):
    """A new process is created and added to the queue. All processes start with a "main" as their first
    function command. Print a message to the screen indicating which process was added to the queue."""

    app = process.Process(name)
    scheduler.add_process(app)
    print(f"\"{name}\" was added to the queue")


def calls(scheduler, name, exception):
    """The process at the front of the queue gets some CPU time and calls a function. This puts that function on the
    call stack for that process. After the call is made, that process goes to the back of the line.
    Print to the screen indicating which process called the function and the name of the function."""

    # Create a function with command[1] being the name and command[2] being exception handling boolean
    if exception == "yes":
        func = function.Function(name, True)
    else:
        func = function.Function(name, False)

    scheduler.give_cpu_time(func)


def returns(scheduler):
    """The process at the front of the queue has the function at the top of its call-stack return.
    If the process has any functions left on the call-stack, put it at the back of the queue.
    Otherwise, if main returns, simply remove it. Display a message indicating the process ending."""

    # Pops the front process' top call
    scheduler.return_next_function()


def raises(scheduler):
    """The process at the front of the queue has the function at the top of its call-stack raise an exception.
    That function must pop off the call stack, which continues to pop off functions, of that process, until either
    (1) you reach a function that handles the exception or
    (2) you pop main off, ending the process.

    When an exception is raised print a message indicating so, and print messages for all functions that
    are popped because they didn't handle the exception. Finally print a message with the end result of the
    raised exception, again either the process ending or it being handled and placed to the back of the queue."""
    pass


class Executive:
    """The class that handles files and function calls"""

    def __init__(self, file_name):
        """Takes the file and creates a list of commands"""
        self.commands = get_calls(file_name)

    def run(self):
        """Acts as the main function"""

        scheduler = cpuscheduler.CPUScheduler()
        for command in self.commands:
            command = command.split(" ")

            match command[0]:
                case "START":
                    starts(scheduler, command[1])

                case "CALL":
                    calls(scheduler, command[1], command[2])

                case "RETURN":
                    returns(scheduler)

                case "RAISE":
                    raises(scheduler)
