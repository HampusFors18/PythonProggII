""" bst.py        Version 2021-04-30


Student: Hampus Naumanen
Mail:
Reviewed by:
Date reviewed:
"""


from linked_list import LinkedList
import random
import math

class BST:
    
    class Node:     
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right
        
        def __iter__(self):     # Discussed in the text on generators
            if self.left:            
                yield from self.left
            yield self.key             
            if self.right:        
                yield from self.right
        
        
    def __init__(self, root=None):
        self.root = root
        
        
    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root   
   
   
    def insert(self, key):
        self.root = self._insert(self.root, key)
  
  
    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass # Already there
        return r


    def print(self):
        self._print(self.root)
    
    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)


    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None
    
    
    def size(self):
        return self._size(self.root)
    
    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0                            #tree does not have any nodes
    
    def _height(self, cur_node, cur_height):    #cur_height to store the height
        if cur_node == None:
            return cur_height
        else: 
            left_heigth = self._height(cur_node.left, cur_height + 1)       #Incerement height by 1 on left
            right_height = self._height(cur_node.right, cur_height + 1)      #Increment height by 1 on right
            return max(left_heigth, right_height)
        
        

    
    def remove(self, key):                           
        self.root = self._remove(self.root, key)
    
    def _remove(self, r, k):                            # Compulsory
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
            
        elif k > r.key:
            r.right = self._remove(r.right, k)
            
        else:                                           #If k == r.key  
            if r.left is None:     # Easy case
                return r.right
                    #Sends r.right to remove function => self.root = r.right
            elif r.right is None:  # Also easy case  
                return r.left
                    #Sends r.left to remove function => self.root = r.left
                    
            else: # This is the tricky case.
                temp_key = r.right                         #Find the value to the right of node that should be deleted
                min_key = temp_key.key                     #Store its value
                
                while temp_key.left:                        #if there are smaller values in the right subtree of that node
                    temp_key = temp_key.left                #find the smallest of them by looking to the left
                    min_key = temp_key.key                  #store their values in min_key. Loop wont continue if nothing to the left
        
                
                r.key = min_key                             #copy value of the smallest node to the node that is to be replaced
                r.right = self._remove(r.right, min_key)   #remove that node. That node is the smallest of the right subtree but still bigger than the node to be replaced
            
            
                    # Find the smallest key in the right subtree
                     # Put that key in this node
                     # Remove that key from the right subtree
            
            #temp_key = r.right
                #min_key = temp_key.key
                #while temp_key.left:
                    #temp_key = temp_key.left
                    #min_key = temp_key.key
                    
                    #r.right = self._remove(r.right, r.key)
                     
        return r # Remember this! It applies to some of the cases above
    

    
    def __str__(self):                            # Compulsory
        count = 0
        result = '<'
        for node in BST.__iter__(self):
            result += str(node)
            count +=1
            if self.size() > 1 and count != self.size():
                result += ', '
        result += '>'
        
        return result
            
    
    
    def to_list(self):                            # Compulsory
        bst_list = []
        for node in BST.__iter__(self):
            bst_list.append(node)
        return bst_list
    
    
    def to_LinkedList(self):                      # Compulsory
        lst = LinkedList()
        for node in BST.__iter__(self):
            lst.insert(node)
        return lst
        
    
    def ipl(self):                                # Compulsory
        return self._ipl(self.root, 1)
    
    def _ipl(self, r, level):
        if r is None:
            return 0
        else:
            return level + self._ipl(r.left, level + 1) + self._ipl(r.right, level + 1)
        
        #Check if None - return 0
        #increment level 
        #Recursive function
        # level + 1
        #check left / right seperately or at the same 
        # if not None - return level + ipl(r.left, lev +1)
        #for right: retrun level + ipl(r.right, level +1)
        pass
    
    
def random_tree(n):                               # Useful
    rand_tree = BST()
    count = 0
    while count < n:
        rand_tree.insert(random.random())
        count += 1
    return rand_tree


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")
        
    print('Height of tree : ', t.height())
    t.print()
    
    t1 = BST()
    for x in [9, 4, 2, 7, 1, 3, 5, 8, 6, 16, 19, 13, 11, 14, 15, 10, 12]:
        t1.insert(x)
    t1.print()
    print()
    print('size : ', t1.size())
    print('----------------------------')
    print('removing element : 10')
    t1.remove(10)
    print('size : ', t1.size())
    t1.print()
    print()
    print('----------------------------')
    print('removing element : 9')
    t1.remove(9)
    print('size : ', t1.size())
    t1.print()
    print()
    print('----------------------------')
    print(t1.ipl())
    
    
    t2 = BST()
    for x in [9, 4, 2, 7, 1, 3, 5, 8, 6, 16, 19, 13, 11, 14, 15, 10, 12]:
        t2.insert(x)
    t2.print()
    
    print()
    print('Testing stringmethod')
    
    print(t2.__str__())
    
    print()
    print('Testing stringmethod on blank')
    t3 = BST()
    t3.print()
    print()
    print('string print: ', t3.__str__())
    
    
    
    print()
    print('Testing stringmethod on one element')
    t4 = BST()
    for x in [1]:
        t4.insert(x)
    t4.print()
    print()
    print('string print: ', t4.__str__())
    print('Level of tree: ', t4.ipl())
    print('size: ', t4.size())
    
    print()
    print('Testing stringmethod and to list')
    t5 = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t5.insert(x)
    t5.print()
    print()
    print('string print: ', t5.__str__())
    print()
    print(t5.to_list())
    print(t5.to_LinkedList())
    print('Level of tree: ', t5.ipl())
    print('size: ', t5.size())
    
    print('----------------------------')
    print('----------------------------')
    print('----------------------------')
    
    
    n = 10000
    randTree = random_tree(n)
    #randTree.print()
    print()
    print('Random tree size: ', randTree.size())
    print()
    print('Random tree height: ', randTree.height())
    print()
    print('Internal path length:', randTree.ipl())
    print()
    print(1.39*n*math.log(n,2) + n)
    
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    
"""
What is the generator good for?
==============================

1. computing size?
2. computing height?
3. contains?
4. insert?
5. remove?




Results for ipl of random trees
===============================

                IPL:                     Formula:

n = 10             30                           56.1748


n = 100            810                          1023.496


n = 1000           12240                       14852.44


n = 10000          165099                      194699


n = 100000          2140415                   2408740


n = 1000000        25712039                   28704880


n = 10000000       297297971                  333223603

om vi delar resultatet för av nuvarande med föregående värde hamnar IPL
på värdet:
            11,5626 (Högsta genom näst högsta)
            
om vi delar resultatet för av nuvarande med föregående värde hamnar Formula
på värdet:
            11,6086 (Högsta genom näst högsta)



"""
