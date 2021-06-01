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

        if self.first is None:
            self.first = self.last = Queue.Qnode(data)
        else:
            self.last.next = self.last = Queue.Qnode(data)

    """***************
       *** TASK A4 ***
       ***************"""

    def dequeue(self):
        """Remove item from the list and return it"""
        if self.first is None:
            return None
        else:
            result = self.first.data
            self.first = self.first.next
        return result

    """***************
       *** TASK A5 ***
       ***************"""

    # Remove this and implement the operator overload (+)

    def __add__(self, other):
        
        q = Queue()
        
        x = self.first
        while x:
            q.enqueue(x)
            x = x.next
            
        y = other.first
        while y:
            q.enqueue(y)
            y = y.next
        
        return q
        


if __name__ == '__main__':
    # Add tests for this specific file here

    pass
