import stack


class Process:
    """
    A process is in charge of managing its call stack by making additional calls (adding to the call stack),
    having a function return (removing from the call stack), or having a function raise an exception
    """

    def __init__(self, name):
        self.name = name
        self.call_stack = stack.Stack()

    def add_call(self):
        """Add a function to the call stack"""
        pass

    def return_function(self):
        """Returns a function and removes from the call stack"""
        pass

    def raise_exception(self):
        """Pops calls off the process' call stack until either a function that handles the exception is reached or
        main is popped off, ending the process"""
        pass
