# coding=utf-8
"""
Exemple code in module 1

"""
import random   
import time
import itertools
import functools
   

def fac(n):
    """ Computes and returns n!""" 
    if n==0:
        return 1
    else:
        return n*fac(n-1)


def power(x,n):
    """ Computes and returns x**n recursively"""
    
    if n == 0:                                  #Basfall
        return 1
    elif n > 0:
        return x*power(x, n-1)                  #För positiva n
    else:
        return 1./power(x, -n)                  #För negativa n

    
def multiply(m,n):
    """ Computes and returns the product m*n recursively"""
    
    if m == 0 or n == 0:                        #Basfall
        return 0
    elif m < n:
        return n + multiply(n, m-1)             #Rekursivt anrop m < n
    else:
        return m + multiply(m, n-1)             #Rekursivt anrop n < m
    
    
def divide(t,n):
    """ Computes and returns the number of times n goes into t"""
    
    if t < n:                                   #Basfall
        return 0
    else:
        return 1 + divide(t-n, n)               #Rekursivt anrop
    
    
def harmonic (n):
    """ Computes and returns the nth value of the Harmonic serie"""
    
    if n == 1:                                  #Basfall
        return 1
    else:
        return 1/n + harmonic(n-1)              #Rekursivt anrop
    
    """Iterative method"""
#def digit_sum_iterative(x):
#    
#    tot = 0
#    while (x > 0):
#        dig = x%10
#        tot = tot + dig
#        x=x//10   
#    return tot


def digit_sum(x):
    """ Computes and returns the sum of digits recursively"""
    
    if (x < 10):                                #Basfall
        return x
    else: 
        return x%10 + digit_sum(x//10)          #Rekursivt anrop
        

def get_binary(x):
    """Returns the binary value of a number x"""
    
    if x == 0:                                  #Basfall
        return ' '
    elif x < 0:
        return '-' + get_binary(-x//2) + str(x%2)    
    else: 
        return get_binary(x//2) + str(x%2)
        

def reverse_mid(x):
    """ Returns s reversed """
    if len(x) <= 1:
        return x
    else:
        mid = len(x)//2
        return reverse_mid(x[mid:]) + reverse_mid(x[:mid])
    
    
def largest(a):
    """Returns the largest value of the list using recursion"""
   
    if len(a) == 1:                             #Basfall       
        return a[0]
    else:
        return largest(a[1:]) if largest(a[1:]) > a[0] else a[0]
    
    
def count(x,s):
    """Returns the number of times x is in all levels of the list s"""
   
    if len(s) == 0:                             #Basfall
        return 0
    elif s[0] == x:
        return 1 + count(x, s[1:])
    elif type(s[0]) == list:
        return count(x, s[0]) + count(x, s[1:])
    else:
        return count(x, s[1:])


def zippa(l1, l2):
    """Returns a list of alternating listelements from l1 and l2"""
    
    if len(l1) == 0:                            #Basfall
        return l2.copy()
    elif len(l2) == 0:
        return l1.copy()
    else:
        return [l1[0]] + zippa(l2, l1[1:])      #zipping procedure
    
        
def bricklek(f, t, h, n):
    """Solves the Hanoi Tower problem using recursion and prints the solution as a list of movements"""
    
    if n == 0:                                  #Basfall
        return []
    else:
       return bricklek(f, h, t, n-1) + [f"{f}->{t}"] + bricklek(h, t, f, n-1)       #Moving the pieces


def exchange(a, coins):
    """ Count possible way to exchange a with the coins in coins"""
    if a == 0:
        return 1
    elif (a < 0) or (len(coins) == 0):
        return 0
    else:
        return exchange(a, coins[1:]) + exchange(a - coins[0], coins)


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

memory = {0:0, 1:1}
def fib_mem(n, memory):
    if n in memory:
        return memory[n]
    else:
        memory[n] = fib_mem(n-1, memory) + fib_mem(n-2, memory)
        return memory[n]     




def insertion_sort_rec(l, n):
    """ Recursive insertion sort. Not suitable for large lists"""
    if n > 1:
        insertion_sort_rec( l, n-1 )    # sort the n-1 first
        x = l[n-1]
        i = n-2              # move elements larger than x to the right
        while i>=0 and l[i]>x :
            l[i+1] = l[i]
            i=i-1
        l[i+1] = x           # put in x


def insertion_sort(l):
    """ Iterative insertion sort """
    for j in range(1, len(l)):
        x = l[j]
        i = j-1
        while i >= 0 and x < l[i]:
            l[i+1] = l[i]
            i -= 1
        l[i+1] = x
             

def merge(l1, l2):
    """ Merges two lists.
    Not suitable for large lists because of the recursion depth
    and because of a lot of list building.
    """
    if len(l1) == 0:
        return l2.copy()
    elif len(l2) == 0:
        return l1.copy()
    elif l1[0] <= l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    else:
        return [l2[0]] + merge(l1, l2[1:])       
  
  
def merge_sort(l):
    """ Merge sort. Just to demonstrate the idea"""
    if len(l) <= 1:
        return l
    else:
        n = len(l)//2
        l1 = l[:n]
        l2 = l[n:]
        l1 = merge_sort(l1)
        l2 = merge_sort(l2)
        return merge(l1, l2)


def main():
    
   # print(f"fac(100) = {fac(100)}\n")
    
    print(f"power(2, 5) = {power(2, 5)}")
    print(f"power(2,-1) = {power(2,-1)}\n")
    
    print(f"multiply(2, 6) = {multiply(2, 6)}")
    
    print(f"divide(3,3) = {divide(3,3)}")
    
    print(f"harmonic(10) = {harmonic(10)}")
    
   # print(f"digit_sum_iterative(2301) = {digit_sum_iterative(2301)}")
   # print(f"digit_sum_iterative(101207) = {digit_sum_iterative(101207)}")
    
    print(f"digit_sum(2301) = {digit_sum(2301)}")
    print(f"digit_sum(101207) = {digit_sum(101207)}")
    
    
    print(f"get_binary(5) = {get_binary(5)}")
    print(f"get_binary(15) = {get_binary(15)}")
    print(f"get_binary(-18) = {get_binary(-18)}")
    
    print(f"largest([1,2,3,4,5,6,7])) = {largest([1,2,3,4,5,6,7])}")
    print(f"largest([9,2,3,4,5,6,7])) = {largest([9,2,3,4,5,6,7])}")
    print(f"largest([1,2,4,4,5,5,2])) = {largest([1,2,4,4,5,5,2])}")
    print(f"largest([12,2,3,27,10,5,11,19,0])) = {largest([12,2,3,27,10,5,11,19,0])}")
    
    
    
    print(f"count(([1,4], [1, 'a', 3, 7, 1, [1, 4]]) = {count([1,4], [1, 'a', 3, 7, 1, [1, 4]])}")
    print(f"count(4, [1, 2, 3, 4]) = {count(4, [1, 2, 3, 4])}")
    print(f"count(4, [4, [3], 2, 3, 4]) = {count(4, [4, [3], 2, 3, 4])}")
    print(f"count(4, [4, [4], 2, 3, 4]) = {count(4, [4, [4], 2, 3, 4])}")
    print(f"count(4, [[3], 1, 2, 3, 4]) = {count(4, [[3], 1, 2, 3, 4])}")
    print(f"count(4, [[4], 1, 2, 3, 4]) = {count(4, [[4], 1, 2, 3, 4])}")
    print(f"count(4, [4, 1, 2, 3, 4]) = {count(4, [4, 1, 2, 3, 4])}")
    print(f"count(4, [1, 4, 2, ['a', [ [ 4 ] , 3, 4] ] ] ) = {count(4, [1, 4, 2, ['a', [ [ 4 ] , 3, 4] ] ] )}")
    
    
    print(f"zippa([], [2,3]) = {zippa([], [2,3])}")
    print(f"zippa([1,2], []) = {zippa([1,2], [])}")
    print(f"zippa([1], [2]) = {zippa([1], [2])}")
    print(f"zippa([1,3], [2,4]) = {zippa([1,3], [2,4])}")
    print(f"zippa([], [2,4,6,8,10]) = {zippa([], [2,4,6,8,10])}")
    print(f"zippa([1,3,5], [2,4,6,8,10]) = {zippa([1,3,5], [2,4,6,8,10])}")
    
    #print(f"tower(4, 'A', 'C', 'B') = {tower(4, 'A', 'C', 'B')}")
    print(f"bricklek('f', 't', 'h', 2) = {bricklek('f', 't', 'h', 2)}")
    print(f"bricklek('f', 't', 'h', 4) = {bricklek('f', 't', 'h', 4)}")
    
    print(f"exchange(100, [1, 5, 10, 50, 100]) = {exchange(100, [1, 5, 10, 50, 100])}")
    
    tstart = time.perf_counter ()
    print(f"fib(42) = {fib(42)}")
    tstop = time.perf_counter ()
    print(f"Measured  time: {tstop -tstart} seconds")

    
    tstart = time.perf_counter ()
    print(f"fib_mem(100, memory) = {fib_mem(100, memory)}")
    tstop = time.perf_counter ()
    print(f"Measured  time: {tstop -tstart} seconds")
    
    
#    diff = 0
#    for x in range(20):
#        tstart = time.perf_counter ()
#        print(f"fib(30) = {fib(30)}")
#        tstop = time.perf_counter ()
#        diff = (diff + (tstop-tstart))
#        print(f"Measured  time: {tstop -tstart} seconds")
#        print(f"Diff time: {diff} seconds")
#    average = diff/20
#    print(f"Average time: {average} seconds")
    
#    tstart = time.perf_counter ()
#    print(f"fib(439) = {fib(39)}")
#    tstop = time.perf_counter ()
#    print(f"Measured  time: {tstop -tstart} seconds")
#    
#    tstart = time.perf_counter ()
#    print(f"fib(40) = {fib(40)}")
#    tstop = time.perf_counter ()
#    print(f"Measured  time: {tstop -tstart} seconds")
#    
    #print(f"fib(10) = {fib(10)}")

#    coins = (1, 5, 10, 50, 100)
#    for a in [1, 4, 5, 9, 10, 100]:
#        print(f"exchange({a}, {coins}) : {exchange(a, coins)}")
#    print()
#
#    for i in [0, 1, 2, 5, 10]:
#        print(f"fib({i}) : {fib(i)}")
#    print()
#    
#    for i in [0, 1, 2, 5, 10]:
#        print(f"fib_mem({i}) : {fib_mem(i, {0:0, 1:1})}")
#    print()
#    
#    print('Trying merge sort')
#    test_size = 20
#    l =[random.randint(1,100) for i in range(test_size)]
#    print('Created list:', l)
#    r = merge_sort(l)
#    print('Sorted list :', r[0:test_size])
#   
#   
#    # Demonstrates how the time complexity can be verified by experiments
#    print('\nSorting with non recursive insertion sort')
#    for test_size in [1000, 2000, 4000, 8000]:   
#        l =[random.random() for i in range(test_size)]
#        tstart = time.perf_counter()
#        insertion_sort(l)
#        tstop = time.perf_counter()
#        print(f"Time for sorting {test_size} values: {tstop-tstart:.2f} seconds")
        
if __name__ == "__main__":
    main()
    print('Bye!')


"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 15: Time for bricklek with 50 bricks:
  
  2^50-1 sekunder =         (Att ta ett steg motsvarar 1 sekund)
  3,57*10^7 år =
  35,7 miljoner år
  
  
  
  
  Exercise 16: Time for Fibonacci:
  
  a) på 20 itereringar:
    
För fib(33) tar det 2.5628 sekunder (medelvärde)
För fib(34) tar det 4.1049 sekunder (medelvärde)
  
4.1049/2.5628 = 1.602 sekunder

Vi ser alltså att mellan två steg växer tiden med ungefär 1.618 sekunder

  
  b)

1.618^40 operationer för fib(40) (46.086 sekunder)

1.618^40 operationer / 46.086 sekunder = 4.96x10^6 operationer per sekund

för fib (50) => 1.618^50 operationer

1.618^50 / 4.96x10^6 = ca 95 minuter



för fib(100) => 1.618^100 operationer

1.618^100 / 4.96x10^6 = ca 5 miljoner år

    

Det tog ca 8x10^-5 sekunder att räkna fib_mem(100)
      
      
  
  
  
  Exercise 19: Comparison sorting methods:
  
  För instickssortering har vi att tiden motsvarar n^2
  
  För mergesortering har vi att tiden motsvarar n*log n
  
  
  Om det tar lika lång tid för 1000 slumptal, dvs 1 sekund
  
  för instickssortering har vi då att
  
  n = 10^6:
  
  (10^6)^2 / 1000^2 = 10^6, alltså tar det 10^6 gånger längre tid då tiden ökar kvadratiskt
  
  Det motsvarar alltså en miljon sekunder för 10^6 itereringar, eller 11.57 timmar
  
  n = 10^9:
  
  (10^9)^2 / 1000^2 = 10^12
  
  Tiden detta motsvarar är hissnande 31710 år!
  
  
  För mergesortering har vi
  
  n = 10^6:
  
  (10^6* log (10^6)) / (1000*log 1000) = 2000
  
  Alltså tar det 2000 gånger längre tid för mergesortering för 10^6 itereringar
  
  det motsvarar 33.3 minuter
  
  n = 10^9:
      
  (10^9* log (10^9)) / (1000*log 1000) = 3*10^6
  
  detta motsvarar ungeför 34.7 dagar

      
      
  
  Exercise 20: Comparison Theta(n) and Theta(n log n)
  
  
  
  För A:
      
      n på n sekunder, alltså 10 skunder när n = 10

  För B:
      
      B tar 1 sekund när n=10
      
      Vi löser ut c:
          
      c*10*log 10 = 1 => c=1/10
      
      
      Vi sätter uttrycken lika
      
      n/10*log n - n = 0
      
      Vi löser ut n
      
      n = 10^10
      
      så för n > 10^10 är det bättre använda algoritm A
  
  
  





"""
