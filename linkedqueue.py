from node import Node


class LinkedQueue:

    def __init__(self):
        self._front = self._back = None

    def enqueue(self, entry):
        """Add to the back"""

        node = Node(entry)

        if self.is_empty():
            self._front = node
            self._back = node

        elif self._back is self._front:
            self._back = node
            self._front.next = self._back

        else:
            temp = self._back
            self._back = node
            temp.next = self._back

    def dequeue(self):
        """Remove the front"""

        # No items in the queue
        if self.is_empty():
            raise RuntimeError("Queue already empty")

        # One item in queue, make sure to set back to None
        elif self._back is self._front:
            temp = self._front
            self._front = self._back = None
            return temp

        # Multiple items in queue
        else:
            temp = self._front
            self._front = self._front.next
            return temp

    def peek_front(self):
        """Look at the front node"""

        if self._front:
            return self._front.value
        else:
            return None

    def is_empty(self):
        """Checks for any nodes in the queue"""

        if self._front is None:
            return True
        return False
