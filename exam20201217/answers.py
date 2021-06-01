EXAM_ID = ''  # Enter the ID number given when you registered for the exam
EMAIL = ''  # Enter your contact email address


"""***************
   *** TASK A1 ***
   ***************"""


def calculator_int():
    """Modify calculator.py so that it has a function
       which removes decimals.
       Leave this method as is."""

    import calculator as c

    r1 = c.run('int(2.8)')  # Expected value:  2
    r2 = c.run('int(-4.69)')  # Expected value: -4
    r3 = c.run('int(-.9)')  # Expected value:  0

    return r1, r2, r3


"""***************
   *** TASK A2 ***
   ***************"""


def calculator_factor():
    """Modify calculator.py so that it can handle
       factorials.
       Leave this method as is."""

    import calculator as c

    r1 = c.run('0!')  # Expected value:   1
    r2 = c.run('1!')  # Expected value:   1
    r3 = c.run('2!')  # Expected value:   2.0
    r4 = c.run('3!')  # Expected value:   6.0
    r5 = c.run('exp(3!) + 2!')  # Expected value: 405.4287934927351
    r6 = c.run('2.5!')  # Expected value: Error: Illegal argument to factorial: 2.5
    r7 = c.run('-1!')  # Expected value:  -1
    r8 = c.run('(-1)!')  # Expected value: Error: Illegal argument to factorial: -1.0

    return r1, r2, r3, r4, r5, r6, r7, r8


"""***************
   *** TASK A3 ***
   ***************"""


def qlist_enqueue():
    """Modify Qlist.py so that a value can be queued.
       Leave this method as is."""

    from Qlist import Queue

    q = Queue()

    for x in [6, 4, 6, 9, 4]:
        q.enqueue(x)

    return q


"""***************
   *** TASK A4 ***
   ***************"""


def qlist_dequeue():
    """Modify Qlist.py so that a value can be
       removed and returned.
       Leave this method as is."""

    from Qlist import Queue

    q = Queue()
    l = [2, 8, 2, 7, 8, 4, 9, 2]
    r = []

    for x in l:
        q.enqueue(x)

    for _ in range(int(len(l) / 2)):
        r.append(q.dequeue())

    return r


"""***************
   *** TASK A5 ***
   ***************"""


def operator_overload():
    """Modify Qlist.py so that two queues can
       be added using the + sign to create
       a third queue.
       Leave this method as is."""

    from Qlist import Queue

    q1 = Queue()
    q2 = Queue()

    for x in [5, 23, 2, 31]:
        q1.enqueue(x)

    for x in [9, 5, 56, 7]:
        q2.enqueue(x)

    try:
        q3 = q1 + q2
    except TypeError:
        q3 = None

    return q3


"""***************
   *** TASK A6 ***
   ***************"""


def smallest_in_list():
    """Modify PQlist.py so that the smallest
       item in the list is returned.
       Leave this method as is."""

    from PQlist import PQlist

    pq = PQlist()
    for x in [2, 5, 3, 7, 2, 3]:
        pq.enqueue(x)

    return pq.smallest()


"""***************
   *** TASK A7 ***
   ***************"""


def copy_list():
    """Modify PQlist.py so that it can
       produce a copy of itself.
       Leave this method as is."""

    from PQlist import PQlist

    pq = PQlist()
    for x in [5, 9, 3, 8, 5, 7]:
        pq.enqueue(x)

    return pq.copy()


"""***************
   *** TASK A8 ***
   ***************"""


def pqlist_complexity_answer():
    """Write your answer to the question in Task A8 in
       in the string being returned."""

    return ''


"""***************
   *** TASK A9 ***
   ***************"""


def pqbst_enqueue():
    """Modify PQbst.py so that a value can be queued.
       Leave this method as is."""

    from PQbst import PQbst

    pq = PQbst()
    l = [4, 8, 4, 10, 7, 4, 8, 1]

    for x in l:
        pq.enqueue(x)

    return pq


"""****************
   *** TASK A10 ***
   ****************"""


def fib(n):
    """Feel free to modify this method
       if you find it necessary in order
       to complete this task."""

    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def multi_fib(fr=30, to=38):
    """Run parallel calls to to the fib method
        and return a dictionary object."""

    pass  # Remove the pass statement and enter your code here


"""***************
   *** TASK B1 ***
   ***************"""


def print_pq():
    """Make the method run correctly"""

    from PQlist import PQlist

    pq = PQlist()

    for x in [2, 5, 3, 7, 2, 3]:
        pq.enqueue(x)

    result = ''

    try:
        for x in pq:
            result += f'{x} '
    except TypeError:
        result = None

    return result


"""***************
   *** TASK B2 ***
   ***************"""


def letter_combo(s, l1, l2):
    """Recursively calculate and return
       the number of times l1 directly
       precedes l2 in the given string"""

    pass  # Remove the pass statement and enter your code here


"""***************
   *** TASK B3 ***
   ***************"""


def pqbst_dequeue():
    """Modify PQbst.py so that a value can be queued.
       Leave this method as is"""

    from PQbst import PQbst

    pq = PQbst()
    l = [6, 7, 12, 6, 1, 18, 9, 6, 5]
    for x in l:
        pq.enqueue(x)

    x = 1
    while x <= 5:
        pq.dequeue()
        x += 1

    return pq


"""***************
   *** TASK B4 ***
   ***************"""


def pqbst_complexity_answer():
    """Write your answer to the question in Task B4 in
       in the string being returned."""

    return ''


"""***************
   *** TASK B5 ***
   ***************"""


def get_info(index):
    """This method opens the peeps.json file and returns
       the about info of the customer of the index given.
       Leave this method as is."""

    import json

    with open('peeps.json') as f:
        data = json.load(f)
        return data[index]['about']


def worker(data):
    """Employ this worker in your parallel
       execution if you need to, but do not add
       input arguments to this method."""

    pass  # Remove the pass statement and enter your code here


def calculate_occurrences(indexes, l1, l2):
    """Run each index concurrently.
       Return a total of occurrences
       found in the given customer's
       about info from get_info."""

    pass  # Remove the pass statement and enter your code here


"""************************************
   *** Run and test your code below ***
   ************************************"""

# Please note: The tests below are not exhaustive, meaning they do not cover all possible test cases.
# Make sure you write your own cases as well to fully test your code.


if __name__ == '__main__':
    # ** TASK A1 **
    print(f'A1: Executing int method in calculator. Expected value: (2, -4, 0).')
    print(f"Returned value: {calculator_int()} \n")
    # **************

    # ** TASK A2 **
    print(f"A2: Executing factorial method in calculator. "
          f"Expected value: (1, 1, 2.0, 6.0, 405.4287934927351, 'Error', -1, 'Error') .")
    print(f"Returned value: {calculator_factor()} \n")
    # **************

    # ** TASK A3 **
    print(f'A3: Executing enqueue of Qlist. Expected value: [6, 4, 6, 9, 4].')
    print(f"Returned value: {qlist_enqueue()} \n")
    # **************

    # ** TASK A4 **
    print(f'A4: Executing dequeue of Qlist. Expected value: [2, 8, 2, 7].')
    print(f"Returned value: {qlist_dequeue()} \n")
    # **************

    # ** TASK A5 **
    print(f'A5: Executing + operator on Qlist. Expected value: [5, 23, 2, 31, 9, 5, 56, 7].')
    print(f"Returned value: {operator_overload()} \n")
    # **************

    # ** TASK A6 **
    print(f'A6: Executing smallest of PQlist. Expected value: 2.')
    print(f"Returned value: {smallest_in_list()} \n")
    # **************

    # ** TASK A7 **
    print(f'A7: Executing copy of PQlist. Expected value: [7, 5, 8, 3, 9, 5].')
    print(f"Returned value: {copy_list()} \n")
    # **************

    # ** TASK A8 **
    print(f'A8: Executing pqlist_complexity_answer.')
    print(f'Your answer to A7: {pqlist_complexity_answer()} \n')
    # **************

    # ** TASK A9 **
    print(f'A9: Executing enqueue of PQbst. Expected value: < 1 4 4 4 7 8 8 10 >.')
    print(f"Returned value: {pqbst_enqueue()} \n")
    # **************

    # ** TASK A10 **
    # The method takes two integers and uses it as an
    # interval to calculate Fibonacci numbers. It should return a dictionary
    # with n as key and the nth Fibonacci number as value.
    print('A10: Executing multi_fib. Expected value: '
          '{'
          '30: 832040,'
          '31: 1346269, '
          '32: 2178309, '
          '33: 3524578, '
          '34: 5702887, '
          '35: 9227465, '
          '36: 14930352, '
          '37: 24157817, '
          '38: 39088169'
          '}.')
    print("\033[31m -- Uncomment the next line to test this method (can be slow!) -- \033[0m \n")
    #print(f"Returned value: {multi_fib()} \n")
    # **************

    # ** TASK B1 **
    print(f'B1: Executing print_pq. Expected value: 3 2 7 3 5 2  .')
    print(f"Returned value: {print_pq()} \n")
    # **************

    # ** TASK B2 **
    quote = "It’s hardware that makes a machine fast. It’s software that makes a fast machine slow."

    # The method letter_combo takes a string and two letters as arguments
    # and return the number of occurrences where letter 1 directly precedes letter 2.
    print(f'B2: Executing letter_combo. Expected value: 4.')
    print(f"Returned value: {letter_combo(quote, 'm', 'a')} \n")
    # **************

    # ** TASK B3 **
    print(f'B3: Executing dequeue of PQbst. Expected value: < 7 9 12 18 > .')
    print(f"Returned value: {pqbst_dequeue()} \n")
    # **************

    # ** TASK B4 **
    print(f'B4: Executing pqbst_complexity_answer.')
    print(f'Your answer to B4: {pqbst_complexity_answer()} \n')
    # **************

    # ** TASK B5 **
    customer_indexes = [12, 19, 27, 48, 51, 66, 68, 80, 91, 101]

    # The method calculate_occurrences takes a list of customer indexes
    # along with two letters as input arguments. It should return the
    # total of occurrences where letter 1 precedes letter 2 in the customer about info.
    print(f'B5: Executing calculate_occurrences. Expected value: 27.')
    print(f"Returned value: {calculate_occurrences(customer_indexes, 'n', 'i')} \n")
    # **************
