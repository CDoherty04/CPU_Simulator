import function
import stack


class Process:
    """
    A process is in charge of managing its call stack by making additional calls (adding to the call stack),
    having a function return (removing from the call stack), or having a function raise an exception
    """

    def __init__(self, name):
        """Initializes the name from input and creates a call stack with a main function"""
        self._name = name
        self._call_stack = stack.Stack()
        self.add_call(function.Function("main", False))

    def add_call(self, call):
        """Add a function to the call stack"""
        self._call_stack.push(call)

    def return_function(self):
        """Returns a function by popping from the call stack"""
        name = self._call_stack.peek()
        self._call_stack.pop()
        return name

    def raise_exception(self):
        """Pops calls off the process' call stack until either a function that handles the exception is reached or
        main is popped off, ending the process"""
        pass

    def get_name(self):
        """Returns the call stack"""
        return self._name

    def get_call_stack(self):
        """Returns the call stack"""
        return self._call_stack
