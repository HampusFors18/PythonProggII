"""
   ***************
   *** TASK B1 ***
   ***************

   Add any methods to this file
   that you need to complete task B1
"""


class PQlist:
    """ Represents a set of object as a linked list """

    class Qnode:
        """ Represents a single item within the linked list."""

        def __init__(self, data, nxt=None):

            self.data = data
            self.next = nxt

        def __str__(self):
            s = f"{self.data}"
            return s

        """***************
           *** TASK A6 ***
           ***************"""

        def smallest(self):
            """Make use of this helper method if needed"""

            pass  # Remove the pass statement and enter your code here

        """***"""

    def __init__(self, node=None):
        self.first = node

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

    def enqueue(self, data):
        self.first = PQlist.Qnode(data, self.first)

    def dequeue(self):
        if self.first is None:
            return None
        else:
            s = self.smallest()
            if s == self.first.data:
                self.first = self.first.next
            else:
                n = self.first
                while n.next.data != s:
                    n = n.next
                n.next = n.next.next
            return s

    """***************
       *** TASK A6 ***
       ***************"""

    def smallest(self):
        """Return the smallest value in
           the queue. A helper method is
           defined in the node class, use
           it if you need it."""

        pass  # Remove the pass statement and enter your code here


    """***************
       *** TASK A7 ***
       ***************"""

    def copy(self):
        """ Leave this method as is."""

        return PQlist(self._copy(self.first))

    def _copy(self, f):
        """Return a copy of the list"""

        pass  # Remove the pass statement and enter your code here



if __name__ == '__main__':
    # Add tests for this specific file here

    pass
