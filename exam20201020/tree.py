"""
Represent a set of keys in a binary search tree.
"""

from linkedlist import ListSet


class BST:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

        def __str__(self):
            return f' {self.key}'

        def __iter__(self):
            if self.left:
                for x in self.left:
                    yield x
            yield self
            if self.right:
                for x in self.right:
                    yield x

    def __init__(self):
        self.root = None

    def __str__(self):
        result = '<'
        if self.root:
            for n in self.root:
                result += str(n) + ' '
        return result + '>'

    def __iter__(self):
        """ Generates the keys in order """
        if self.root:
            for x in self.root:
                yield x

    def insert(self, key):
        """ Inserts a new key in the tree. If the key is already there, nothing is done """
        self.root = self._insert(key, self.root)

    def _insert(self, key, t):
        """ Help method to insert """
        if t is None:
            return BST.Node(key)
        elif key < t.key:
            t.left = self._insert(key, t.left)
        elif key > t.key:
            t.right = self._insert(key, t.right)
        return t

    def contains(self, key):
        """True if 'key' is in the tree, else False """
        return self._contains(key, self.root)

    def _contains(self, key, n):
        """ Help methods for contains """
        if n is None:
            return False
        elif key < n.key:
            return self._contains(key, n.left)
        elif key > n.key:
            return self._contains(key, n.right)
        else:
            return True

    """***************
       *** TASK A6 ***
       ***************"""

    def size(self):
        """This method should return the number of items
           the tree contains"""

        pass  # Remove the pass statement and enter your code here

    """***************
       *** TASK A7 ***
       ***************"""

    def height(self):
        """Returns the height of the tree as an integer.
           Leave this method as is.
           Modify the helper method (_height)."""
        return self._height(self.root)

    def _height(self, t):
        """This method should calculate the height of the tree."""

        pass  # Remove the pass statement and enter your code here

    """***************
       *** TASK A8 ***
       ***************"""

    """Define the two dunder methods for greater than and less than here.
       Make use of the height method to determine which tree is larger/smaller"""

    """***************
       *** TASK B4 ***
       ***************"""

    def to_list_set(self):
        """This method returns the keys in the tree as
           a linked list. It makes use of the
           _to_list_set helper method that you should
           write.
           Leave this method as is."""
        result = ListSet()
        self._to_list_set(self.root, result)
        return result

    def _to_list_set(self, t, result):
        """Implement this method with a time complexity of
           O(n). In answers.py, motivate the time complexity
           in the list_set_motivation method."""

        pass  # Remove the pass statement and enter your code here


if __name__ == '__main__':
    """Run this file to test your implementations in the terminal. 
       The code below will only run if this is the main file running."""
