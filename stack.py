from node import Node


class Stack:
    """Node based implementation of a stack"""

    def __init__(self):
        self._top = None

    def push(self, entry):
        """Add to the top of the stack"""

        new_node = Node(entry)

        if self._top:
            temp = self._top
            self._top = new_node
            self._top.next = temp
        else:
            self._top = new_node

    def peek(self):
        """Looks at, but doesn't interact with, the top"""

        if self._top:
            return self._top.value
        return None

    def pop(self):
        """Removes from the top"""

        if self.is_empty():
            raise RuntimeError("Stack already Empty")
        elif self._top.next is None:
            temp = self._top.value
            self._top = None
            return temp
        else:
            temp = self._top.value
            self._top = self._top.next
            return temp

    def is_empty(self):
        """Returns True if the stack is empty"""

        if self._top:
            return False
        return True
