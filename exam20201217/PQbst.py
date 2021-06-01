"""
Implements a priority queue using a binary search tree
"""


class PQbst:
    class Node:
        def __init__(self, prio):
            self.prio = prio
            self.left = None
            self.right = None

        def __str__(self):
            return f' {self.prio}'

    def __init__(self):
        self.root = None

    def __str__(self):
        return '< ' + self._str(self.root) + '>'

    def _str(self, t):
        result = ''
        if t:
            result += self._str(t.left)
            result += str(t.prio) + ' '
            result += self._str(t.right)
        return result

    """***************
       *** TASK A9 ***
       ***************"""

    def enqueue(self, prio):
        """You are allowed to implement a helper
        method called _enqueue if you need it."""

        pass  # Remove the pass statement and enter your code here

    """***************
       *** TASK B3 ***
       ***************"""

    def dequeue(self):

        pass  # Remove the pass statement and enter your code here


if __name__ == '__main__':
    # Add tests for this specific file here

    pass
