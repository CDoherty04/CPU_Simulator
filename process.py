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
        main is popped off, ending the process

        Returns False to remove the process from the queue
        Returns True to move the process to the back of the queue"""

        while True:

            # If main is reached end the process entirely
            if self._call_stack.peek().get_name() == "main":
                print(f"\"main\" could not handle the exception")
                print(f"The \"{self._name}\" process has ended")
                return False

            # If it's not main and can't handle exceptions, pop the call and continue
            elif not self._call_stack.peek().can_handle_exceptions():
                print(f"\"{self._call_stack.peek().get_name()}\" could not handle the exception, and has ended")
                self._call_stack.pop()

            # Otherwise it isn't main and can handle exceptions, place at back of queue
            else:
                print(f"\"{self._call_stack.peek().get_name()}\" handled the exception")
                return True

    def get_name(self):
        """Returns the call stack"""

        return self._name

    def get_call_stack(self):
        """Returns the call stack"""

        return self._call_stack
