"""
Solutions to exam tasks for module 3.
Name:Hampus Naumanen
Code:AX-0055-ZCW

The file contains the classes:
   1) LinkedList with tasks A5, A6 and A7,
   2) BST with tasks A7, A8 and B3, 
   3) Car (just the class statement) which should be written as task A8
   4) LevelOrder (just the class statement) which should be written as task B3

The main function runs a small test of the methods. Note that main will not
fully function until all tasks are solved
"""
import random
import time
import math


class LinkedList:
    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __str__(self):
        result = ''
        for x in self:
            result += str(x) + ', '
        return '<' + result[:-2] + '>'

    def add(self, x):
        """ A5: Add x at the end of the list """
        #node = LinkedList.Node(x)
        if self.first is None:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ:
                f = f.succ
            f.succ = self.Node(x, f.succ)
            
        
    
    
    

    #####################################
    # A6: Complexity for copy1 and copy2

    def copy1(self):
        result = LinkedList()
        for x in self:
            result.add(x)
        return result

    def reversed(self):
        """ Returns a new list with the elements from this list in reverse order"""
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result

    def copy2(self):
        return self.reversed().reversed()


# Write the anser to A6 in this string
A6 = """Complexity for copy1 and copy2 respectively



    """


class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

        def __iter__(self):
            if self.left:
                yield from self.left
            yield self.data
            if self.right:
                yield from self.right

        def __str__(self):
            return str(self.data)

    def __init__(self, root = None):
        """ A7: Allow a list with data as argument """
        self.root = root

    def __iter__(self):
        if self.root:
            yield from self.root

    def __str__(self):
        result = ''
        for x in self:
            result += str(x) + ' '
        return '<' + result + '>'

    def add(self, x):
        def _add(x, r):
            if r == None:
                return self.Node(x)
            elif x < r.data:
                r.left = _add(x, r.left)
            elif x > r.data:
                r.right = _add(x, r.right)
            return r
        self.root = _add(x, self.root)


class Car:
    """ A8 """
    def __init__(self, reg, brand):
        self.reg = reg
        self.brand = brand
        
        
    def __eq__(self, other):
        return self.reg == other.reg
    
    def __le__(self, other):
        return self.reg <= other.reg
    
    def __ge__(self, other):
        return self.reg >= other.reg
    
    def __lt__(self, other):
        return self.reg < other.reg
    
    def __gt__(self, other):
        return self.reg > other.reg
    
    def __ne__(self, other):
        return self.reg != other.reg
    
    def __str__(self):
        return f"{self.reg}, {self.brand}"
        
        
        
        

class LevelOrder:
    """ B3 """
    pass


def main():
    print('\nm3.py\n=====')

    print('\nTest of A5 (add)')
    lst = LinkedList()
    for x in (1, 2, 3, 4, 3, 4, 7):
        lst.add(x)
    print(lst, 'Expected: <1, 2, 3, 4, 3, 4, 7>')

    print('\nAnswert to A6', A6)

    print('\nTest of A7 (init with argument)')
    bst = BST([5, 8, 1, 3, 7, 2, 6])
    print(bst)
    print('\nTest of A7 (empty tree)')
    bst2 = BST()
    print(bst2)

    print('\nTest of A8 (BST with Car objects)')
    bst = BST()
    bst.add(Car('klm123', 'Saab'))
    bst.add(Car('xyz123', 'Volvo'))
    bst.add(Car('abx123', 'VW'))
    for x in bst:
        print(x)
    
    bst = BST()
    bst.add(2)
    bst.add(1)
    bst.add(3)
    print(bst)

    # print('\nTest of B3 (Level order iterator)')
    # liter = LevelOrder(BST([5, 8, 1, 3, 7, 2, 6, 9]))
    # for x in liter:
    #     print(x, end=' ')
    # print('\t Expected: 5 1 8 3 7 9 2 6')


if __name__ == '__main__':
    main()
