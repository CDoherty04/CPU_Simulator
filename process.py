class Process:
    """
    A Process contains a call stack, which is a linked stack of function objects

    A process is in charge of managing its call stack by making additional calls (adding to the call stack),
    having a function return (removing from the call stack), or having a function raise an exception

    NOTE: When a function raises an exception, then you must pop calls off that process' call stack until either (1) you reach a function that handles the exception or (2) you pop main off, ending the process
    """

    def __init__(self):
        self.call_stack = None
