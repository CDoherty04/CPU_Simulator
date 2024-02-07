class Function:
    """A Function contain only two pieces of data: its name and if it can handle thrown exceptions"""
    def __init__(self, name, exception):
        self._name = name
        self._exception = exception

    def get_name(self):
        """Returns the name of the function"""
        return self._name

    def can_handle_exceptions(self):
        """Returns if the function can handle exceptions"""
        return self._exception
