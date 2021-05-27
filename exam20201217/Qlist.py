class Queue:
    """ Represents a set of object as a linked list """

    class Qnode:
        """ Represents a single item within the linked list."""

        def __init__(self, data, nxt=None):
            self.data = data
            self.next = nxt

        def __str__(self):
            s = f"{self.data}"
            return s

    def __init__(self, node=None):
        self.first = node
        self.last = node

    def __str__(self):
        """ Returns a string representation of the key """
        s = "["
        x = self.first
        while x:
            s += str(x)
            x = x.next
            if x:
                s += ", "
        return s + "]"

    """***************
       *** TASK A3 ***
       ***************"""

    def enqueue(self, data):
        """Add item to the list"""

        pass  # Remove the pass statement and enter your code here

    """***************
       *** TASK A4 ***
       ***************"""

    def dequeue(self):
        """Remove item from the list and return it"""

        pass  # Remove the pass statement and enter your code here

    """***************
       *** TASK A5 ***
       ***************"""

    # Remove this and implement the operator overload (+)

    """***"""


if __name__ == '__main__':
    # Add tests for this specific file here

    pass
