class Function:
    """A Function contain only two pieces of data: its name and if it can handle thrown exceptions"""
    def __init__(self, name):
        self.name = name
        self.can_handle_exceptions = False

    def __repr__(self):
        return f"function.Function({self.name})"
