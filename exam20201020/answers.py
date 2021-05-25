EXAM_ID = ''  # Enter the ID number given when you registered for the exam
EMAIL = ''  # Enter your contact email address


"""***************
   *** TASK A1 ***
   ***************"""


def total_list_sum(l):
    """Recursively calculate the total sum of integers
    in the list given and return the sum."""

    pass  # Remove the pass statement and enter your code here


"""***************
   *** TASK A2 ***
   ***************"""


def largest_tuple(t):
    """Recursively find the largest tuple in a set
    of tuples and return it."""

    pass  # Remove the pass statement and enter your code here


"""***************
   *** TASK A3 ***
   ***************"""


def calculate():
    """Modify calculator.py to handle absolute values.
       Leave this method as is."""
    import calculator as c

    r1 = c.run('| -4 |')  # Expected value: 4.0
    r2 = c.run('| -4 + 1 |')  # Expected value : 3.0
    r3 = c.run('| -4 + | -10 + 2 | |')  # Expected value: 4.0
    r4 = c.run('| 10 - | 2 - 20 | |')  # Expected value: 8.0
    r5 = c.run('| 10 - 2 - 20 |')  # Expected value: 12.0
    r6 = c.run('|-3+2)')  # Expected value: None and printed error: Expected '|'
    return r1, r2, r3, r4, r5, r6


"""***************
   *** TASK A4 ***
   ***************"""


def list_size():
    """Modify linkedlist.py so that the size of the list can be accessed.
       Leave this method as is."""
    from linkedlist import ListSet

    s = ListSet()
    s.insert(25)
    s.insert(12)
    s.insert(49)
    s.insert(2)
    s.insert(10)
    return s.size()  # Expected value: 5


"""***************
   *** TASK A5 ***
   ***************"""


def list_index():
    """Modify linkedlist.py so that value at index n can
       be accessed with s[n]."""
    from linkedlist import ListSet

    s = ListSet()
    s.insert(27)
    s.insert(10)
    s.insert(6)
    s.insert(44)
    s.insert(8)
    return s[3]  # Expected value: 27


"""***************
   *** TASK A6 ***
   ***************"""


def tree_size():
    """Modify tree.py so that the size of the tree can be accessed.
       Leave this method as is."""
    from tree import BST

    b = BST()
    b.insert(9)
    b.insert(1)
    b.insert(25)
    b.insert(6)
    b.insert(13)
    b.insert(19)
    return b.size()  # Expected value: 6


"""***************
   *** TASK A7 ***
   ***************"""


def tree_height():
    """Modify tree.py so that the height of the tree can be accessed.
       Leave this method as is."""
    from tree import BST

    b = BST()
    b.insert(4)
    b.insert(8)
    b.insert(2)
    b.insert(12)
    b.insert(11)
    b.insert(13)
    return b.height()  # Expected value: 4


"""***************
   *** TASK A8 ***
   ***************"""


def operator_overload():
    """Overload the greater than and less than operators (> and <)
       on the binary search tree in tree.py so that it compares
       the height of the two trees to find out which is greater/lesser."""
    from tree import BST

    b1, b2 = BST(), BST()

    b1.insert(10)
    b1.insert(13)
    b1.insert(7)
    b1.insert(9)
    b1.insert(11)

    b2.insert(7)
    b2.insert(9)
    b2.insert(10)
    b2.insert(11)
    b2.insert(13)

    try:
        r = b2 > b1
    except TypeError:
        r = None

    return r  # Should return True


"""***************
   *** TASK A9 ***
   ***************"""


def infinite_tens():
    """Make this method a generator that generates multiples of 10
       ad infinitum. When invoking the Python next() method on it,
       the first number should be 1, then 10, then 100 etc."""

    pass  # Remove the pass statement and enter your code here


"""****************
   *** TASK A10 ***
   ****************"""


def get_age(index):
    """This method opens the peeps.json file and
    returns the age of the person of the index given.
    Leave this method as is."""
    import json

    with open('peeps.json') as f:
        data = json.load(f)
        return data[index]['age']


def get_average_age(indexes):
    """Run the get_age in parallel (concurrently) for each of the indexes given.
    Then return the average age of the given results from get_age."""

    pass  # Remove the pass statement and enter your code here


"""***************
   *** TASK B1 ***
   ***************"""


def multi_argument_calculator():
    """Update calculator.py to handle functions with multiple arguments"""
    import calculator as c

    r1 = c.run('sum(1,2,3,4,5,6,7,8,9)')  # Expected value: 45.0
    r2 = c.run('max(1 - 2, min(10, 20))')  # Expected value: 10.0
    r3 = c.run('mean(1, -4, sum(1, 2, 3), | -8 |)')  # Expected value: 2.75
    r4 = c.run('max(2,3|]')  # Expected error: Missing ending ')' in argument list
    r5 = c.run('min()')  # Expected error: Expected number, word, '-' or '('
    return r1, r2, r3, r4, r5


"""***************
   *** TASK B2 ***
   ***************"""


def intersection_answer():
    """Write your answer to the question in Task B2 in
       in the string being returned."""
    return ''


"""***************
   *** TASK B3 ***
   ***************"""


def count_keys():
    """Update the count_keys_between in linkedlist.py.
       The method should count how many keys are between
       the values low and high arguments passed to the method"""
    from linkedlist import ListSet

    s = ListSet()
    s.insert(9)
    s.insert(27)
    s.insert(13)
    s.insert(2)
    s.insert(3)
    s.insert(55)

    r1 = s.count_keys_between(1, 9)  # Expected value: 3
    r2 = s.count_keys_between(20, 100)  # Expected value: 2
    r3 = s.count_keys_between(60, 70)  # Expected value: 0
    return r1, r2, r3


"""***************
   *** TASK B4 ***
   ***************"""


def convert_to_list():
    """Write the _to_list_set helper method in tree.py.
       It should help the to_list_set method return a linked list
       with all values in the binary search tree."""
    from tree import BST

    b = BST()
    b.insert(4)
    b.insert(83)
    b.insert(23)
    b.insert(3)
    b.insert(19)
    return b.to_list_set()  # Expected value: [3, 4, 19, 23, 83]


def list_set_motivation():
    """Write your motivation to the solution of Task B2 in
       in the string being returned."""
    return ''


"""***************
   *** TASK B5 ***
   ***************"""


def get_peeps():
    """This method opens the peeps.json file and
    returns all records as a List of Dictionaries.
    One record is a dictionary. Here is an
    excerpt of one of the records:
    {
        "_id": "5f85a7e08f3a33f3b318be4b",
        "index": 111,
        "balance": "$3,445.93",
        "age": 39,
        "eyeColor": "brown",
        "name": "Hartman Hayden",
        "email": "hartmanhayden@rooforia.com",
        "phone": "+1 (874) 496-3579",
        "address": "843 Miller Avenue, Blende, Louisiana, 2740",
        "latitude": 51.112454,
        "longitude": -10.076946,
    }
    Leave this method as is.
    """
    import json

    with open('peeps.json') as f:
        return json.load(f)


def calculate_distance_to_hq(coordinates):
    """This method takes a set of coordinates as a tuple (latitude, longitude)
       and calculates the distance to the headquarter coordinates, which is
       then returned as a distance in km.
       Leave this method as is."""
    import math

    hq_lat, hq_long = (39.771401, -86.161340)
    R = 6_378_137  # Earth's radius in metres

    c_lat, c_long = coordinates

    p1 = hq_lat * math.pi / 180
    p2 = c_lat * math.pi / 180
    dp = (c_lat - hq_lat) * math.pi / 180
    dl = (c_long - hq_long) * math.pi / 180

    a = (math.sin(dp / 2) ** 2) + math.cos(p1) * math.cos(p2) * (math.sin(dl / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance / 1000


def worker(records):
    """This is a worker method that should be employed
       by the calculate_average_distance_to_hq method.
       It takes a set of peeps records to be used
       to calculate the distance between the customers
       in the set and the bank head quarters, using the
       latitude, longitude attributes in the record."""

    pass  # Remove the pass statement and enter your code here


def calculate_average_distance_to_hq():
    """This method should employ 8 concurrent workers to calculate distances
       between a customer and the bank head quarters. There are currently
       112 customers defined in peeps.json. The average distance between all
       customers and HQ should be returned in km with two decimal points.
       Use the get_peeps method to fetch all customer records as a list of
       dictionaries."""

    pass  # Remove the pass statement and enter your code here


"""************************************
   *** Run and test your code below ***
   ************************************"""

if __name__ == '__main__':
    # ** TASK A1 **
    nums = [96, 45, 100, 27, 77]
    # The method total_list_sum should take a list of integers as an argument
    # and return the sum of all the integers
    print(f'A1: Executing total_list_sum. Expected value: 345.')
    print(f'Returned value: {total_list_sum(nums)} \n')
    # **************

    # ** TASK A2 **
    t = [(1, 5, 12), (7, 9, 14, 13), (8, 7, 2, 10, 14), (2, 10, 5)]
    # The method largest_tuple should take a list of tuples with integers
    # and return the tuple with the larges sum of its integers
    print(f'A2: Executing largest_tuple. Expected value: (7, 9, 14, 13).')
    print(f'Returned value: {largest_tuple(t)} \n')
    # **************

    # ** TASK A3 **
    print(f"A3: Executing calculator with absolute value. Expected values: (4.0, 3.0, 4.0, 8.0, 12.0, 'Error').")
    r = calculate()
    print(f'Returned values: {r} \n')
    # **************

    # ** TASK A4 **
    r = list_size()
    print(f'A4: Executing linked list size method. Expected value: 5.')
    print(f'Returned value: {r} \n')
    # **************

    # ** TASK A5 **
    r = list_index()
    print(f'A5: Executing linked list Node at_index method. Expected value: 27.')
    print(f'Returned value: {r} \n')
    # **************

    # ** TASK A6 **
    r = tree_size()
    print(f'A6: Executing binary search tree size method. Expected value: 6.')
    print(f'Returned value: {r} \n')
    # **************

    # ** TASK A7 **
    r = tree_height()
    print(f'A7: Executing binary search tree height method. Expected value: 4.')
    print(f'Returned value: {r} \n')
    # **************

    # ** TASK A8 **
    r = operator_overload()
    print(f'A8: Executing binary search tree greater than method. Expected value: True.')
    print(f'Returned value: {r} \n')
    # **************

    # ** TASK A9 **
    g = infinite_tens()
    # The method infinite_tens should be a generator object that casts multiples of ten
    # Invoking the next() method should produce the number 1 the first time and 10^(n-1) the nth time
    print(f'A9: Executing infinite_tens generator. Expected values: 1, 10, 100.')

    try:
        r = f'{next(g)}, {next(g)}, {next(g)}'
    except TypeError:
        r = None

    print(f'Returned values: {r}\n')
    # **************

    # ** TASK A10 **
    record_ids = [51, 23, 65, 66, 74, 85, 13, 20, 45, 111]
    # The method get_average_age should take a list of indexes representing IDs for the
    # personal records in peeps.json file. Each index should be sent to get_age which will
    # return a persons age. The get_average_age method should then return the average age.
    print(f'A10: Executing get_average_age. Expected value: 29.0.')
    print(f'Returned value: {get_average_age(record_ids)} \n')
    # **************

    # ** TASK B1 **
    print(f"B1: Executing calculator with multiple arguments. Expected values: (45.0, 10.0, 2.75, 'Error', 'Error').")
    r = multi_argument_calculator()
    print(f'Returned values: {r} \n')
    # **************

    # ** TASK B2 **
    print(f'B2: Executing intersection_answer.')
    print(f'Your answer to B2: {intersection_answer()} \n')
    # **************

    # ** TASK B3 **
    print(f"B3: Executing count_keys_between in linked list. Expected values: (3, 2, 0).")
    r = count_keys()
    print(f'Returned values: {r} \n')
    # **************

    # ** TASK B4 **
    print(f"B4: Executing to_list_set in binary search tree. Expected value: [3, 4, 19, 23, 83].")
    r = convert_to_list()
    print(f'Returned value: {r}')
    print(f'Your motivation to B4: {list_set_motivation()} \n')
    # **************

    # ** TASK B5 **
    print(f'B5: Executing calculate_average_distance_to_hq.')
    print(f'Average distance: {calculate_average_distance_to_hq()} km. \n')
    # **************
