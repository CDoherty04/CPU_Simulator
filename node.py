class Node:
    """Component of the linked data structures"""

    def __init__(self, entry):
        """Holds a value and points to another node"""

        self.value = entry
        self.next = None
