""" linked_list.py

Student: Hampus
Mail: Hampus.naumanne.94@hotmail.com
Reviewed by: Bruse
Date reviewed: 24/5
"""

class LinkedList:
    
    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ      
        
            
    def __init__(self):
        self.first = None

    
    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ
            
    def __in__(self, x):           # Discussed in the section on operator overloading 
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False 
        return False
        
    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')            
    
    
    # To be implemented
    
    def length(self):             # Optional
        """Method that determines and returns the length of the linked list"""
        list_length = 0
        f = self.first
        while f:                    #if f contains element
            list_length += 1        #increment list lenght
            f = f.succ            #next element in linked list
        return list_length
        
  
  
    def mean(self):               # Optional
        """Method that copmutes the mean of all elements in the linked list and returns the mean"""
        list_sum = 0
        f = self.first
        while f:
            list_sum += f.data             #adding elements
            f = f.succ                     #Next element  
        return list_sum/LinkedList.length(self)
    
    
    def remove_last(self):        # Optional
        """Method that removes the last element of the list and returns that element"""
        temp = None
        if self.first is None:
            return None                       #return None if no element in list
        if self.first.succ is None:
            temp = self.first.data              #storing element to be removed
            self.first = None                   #set pointer to of first node to None if second node doesn't exist
            return temp
        f = self.first
        while f.succ.succ:                       #if third node not None, iterate to last element
            f = f.succ
        temp = f.succ.data                        #store node to be removed
        f.succ = None
        return temp
                
                
    
    
    def remove(self, x):          # Compulsory
        """Method that removes a specific element x and returns true
        if it is removed and returns false if it is not in the list"""
        f = self.first
        
        if f is not None:
            if f.data == x:
                #temp = self.first
                self.first = self.first.succ
                #temp = None
                return True
            
        while f is not None:
            if f.data == x:
                break
            f_prev = f                      #store previous value
            f = f.succ                      #increment node
            
        if f == None:                       #if value can't be find in list
            return False
            
        f_prev.succ = f.succ                #Can't set f.succ = None since it would be the value after the value we wanted
        return True
    
    
    
    def count(self, x):           # Optional
        """Method that counts the number of elements in the linked list"""
        return self._count(x, self.first)
     
    def _count(self, x, f):
        #basecase
        if f is None:
            return 0
        elif f.data == x:
            return 1 + self._count(x, f.succ)
        else:
            return self._count(x, f.succ)
    
    
    def to_list(self):            # Compulsory
        """Method that transform the linked list into a ordinary list"""
        return self._to_list(self.first)
    
    def _to_list(self, f):
        if f is None:
            return []
        else:
            return [f.data] + self._to_list(f.succ)
        
    
    
    def remove_all(self, x):      # Compulsory
        """Method that removes all elements of x and returns the new linked list"""
        self.first = self._remove_all(x, self.first)
    
    def _remove_all(self, x, f):
        if f is None:
            return f
        elif x < f.data:
            return f
        elif f.data == x:
            return self._remove_all(x, f.succ)
        else:
            f.succ = self._remove_all(x, f.succ)        #gå till nästa nod
            return f
            
    
    
    def __str__(self):            # Compulsary
        """String method of the linked list"""
        result = '('
        f = self.first
        if f is not None:
            result += str(f.data)
            f = f.succ
            while f:
                result += ', ' + str(f.data)
                f = f.succ
        result += ')'
        return result
            
    
    
    def merge(self, lst):         # Compulsory
        """Method that merges two linked lists"""
        for node in lst:
            self.insert(node)
    
                
            
    def __getitem__(self, ind):   # Compulsory
        """Method that returns a element of a specific index"""
        if ind > self.length():
            return "Index out of range"
        f = self.first
        for n in range(ind):            #count to number ind
            f = f.succ
        return f.data                       #return data of number ind


class Person:                     # Compulsory to complete
    """Constructor of a person class with personal number and name"""
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr
        
    def __eq__(self, other):
        return self.pnr == other.pnr
    
    def __le__(self, other):
        return self.pnr <= other.pnr
    
    def __ge__(self, other):
        return self.pnr >= other.pnr
    
    def __ne__(self, other):
        return self.pnr != other.pnr
    
        
    def __str__(self):
        return f"{self.name}:{self.pnr}"
    

def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()
    
    while lst.length() > 0:
    
    # Test code:
        print('List length: ', lst.length())
        print('Mean value : ', lst.mean())
        print('Number of elements of 1 : ', lst.count(1))
        print('Number of elements of 2 : ', lst.count(2))
        print('Number of elements of 3 : ', lst.count(3))
        print('Making normal list : ', lst.to_list())
        print('Element removed : ', lst.remove_last())
        lst.print()
        print('--------------------------------')
        
        
    lst2 = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst2.insert(x)
    lst2.print()
        
    print('Testing remove_all method\n')
    print('Remove all instances of number 1 :', lst2.remove_all(1))
    print('Remove all instances of number 7 :', lst2.remove_all(7))
    lst2.print()
    
    lst3 = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst3.insert(x)
    lst3.print()
    
    print('--------------------------------')
    
    print('Testing string method\n')
    print('String method : ', lst3.__str__())
    
    lst4 = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7, 3, 3, 3, 3, 3, 4, 5, 6, 2, 2, 2]:
        lst4.insert(x)
    lst4.print()
    
    lst5 = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7, 1, 4, 7, 5, 3, 7, 5, 4, 3]:
        lst5.insert(x)
    lst5.print()
    
    print('Testing merge method')
    lst4.merge(lst5)
    lst4.print()
    
    print('--------------------------------')
    print('Testing getitem method')
    
    lst6 = LinkedList()
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
        lst6.insert(x)
    lst6.print()
    
    print('Fetching item number 5 :', lst6.__getitem__(20))
    
    print('--------------------------------')
    print('Testing getitem method')
    
    lst7 = LinkedList()
    for x in [1, 2, 6]:
        lst7.insert(x)
    lst7.print()
    
    print('Fetching item number 1 :', lst7.__getitem__(0))
    print('Fetching item number 2 :', lst7.__getitem__(1))
    print('Fetching item number 3 :', lst7.__getitem__(2))
    
    print('--------------------------------')
    print('Testing remove method')
    
    lst8 = LinkedList()
    for x in [3, 1, 2, 6, 1]:
        lst8.insert(x)
    lst8.print()
    
    print('Removing item 0 :', lst8.remove(0))
    lst8.print()
    print('Removing item 6 :', lst8.remove(6))
    lst8.print()
    print('Removing item 1 :', lst8.remove(1))
    lst8.print()
    print('Removing item 2 :', lst8.remove(2))
    lst8.print()
    print('Removing item 3 :', lst8.remove(3))
    lst8.print()
    print('Removing item 1 :', lst8.remove(1))
    lst8.print()
    
    print('--------------------------------')
    print('Testing string method')
    
    lst9 = LinkedList()
    for x in [3, 1, 2, 6, 1]:
        lst9.insert(x)
    lst9.print()
    print()
    print('String method: ', lst9.__str__())
    
    print()
    print()
    
    
    person_1 = Person('Hampus', 9405068777)
    person_2 = Person('Ida', 9703259999)
    person_3 = Person('Kalle', 9001018888)
    
    lst_person = LinkedList()
    lst_person.insert(person_1)
    lst_person.insert(person_2)
    lst_person.insert(person_3)
    
    lst_person.print()
    
    print()
    print()
    print()  


if __name__ == '__main__':
    main()
    


    

