class Node:
    """Component of the linked data structures"""

    def __init__(self, entry):
        """Holds a value and points to another node"""

        self._value = entry
        self.next = None

    def get_value(self):
        """Returns the value of the node"""

        return self._value
