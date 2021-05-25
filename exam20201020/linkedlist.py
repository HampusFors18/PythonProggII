class ListSet:
    """ Represents a set of object as a linked list """

    class Node:
        """ Represents a single item within the linked list."""

        def __init__(self, key, next=None):
            self.key = key
            self.next = next

        def insert(self, key):
            """ Adds a new key to the set """
            if key == self.key:
                return False
            elif self.next is None or key < self.next.key:
                self.next = ListSet.Node(key, self.next)
                return True
            else:
                return self.next.insert(key)

        def contains(self, key):
            """ Returns True if `key` is in the sublist starting with this node."""
            if self.key == key:
                return True
            elif self.next and key >= self.next.key:
                return self.next.contains(key)
            else:
                return False

        def __str__(self):
            s = f"{self.key}"
            return s

        """***************
           *** TASK A5 ***
           ***************"""

        def at_index(self, index):
            """This method is called by the __getitem__ dunder method in
               the main ListSet class. This method should find the value
               at the index number given recursively and return it."""

            pass  # Remove the pass statement and enter your code here

    def __init__(self):
        self.first = None

    def insert(self, key):
        """ Insert a key. Returns 'True' if it aleady was there else 'False' """
        if self.first is None or key < self.first.key:  # A new first?
            self.first = self.Node(key, self.first)
            return True
        else:
            return self.first.insert(key)

    def contains(self, key):
        """ Returns 'True' if 'key' is in the set, else 'False' """
        if self.first is not None:
            return self.first.contains(key)
        else:
            return False

    def __str__(self):
        """ Returns a string representation of the list """
        s = "["
        x = self.first
        while x:
            s += str(x)
            x = x.next
            if x:
                s += ", "
        return s + "]"

    """***************
       *** TASK A4 ***
       ***************"""

    def size(self):
        """This method should return the number of items
           the linked list contains"""

        pass  # Remove the pass statement and enter your code here

    """***************
       *** TASK A5 ***
       ***************"""

    def __getitem__(self, index):
        """Operator overload of the square brackets which makes
           the index callable by using list[n], to get the nth index.
           This is thanks to the __getitem__ dunder method.
           Leave this method as is.
           Modify the at_index method of the Node class."""
        if self.first is None:
            return None
        else:
            return self.first.at_index(index)

    """***************
       *** TASK B3 ***
       ***************"""

    def count_keys_between(self, low, high):
        """The method should find all keys between the
           low and high integers passed to the method and
           return a count the number of keys between these values"""

        pass  # Remove the pass statement and enter your code here


if __name__ == '__main__':
    """Run this file to test your implementations in the terminal. 
       The code below will only run if this is the main file running."""
