# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:24:54 2021

@author: Hampu
"""

from time import perf_counter
import matplotlib.pyplot as plt

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def main():
    time_c_list = []
    time_PY_list = []
    for i in range(30,37):
        tC_start = perf_counter()
        fib(i)
        tC_stop = perf_counter()
        time = tC_stop-tC_start
        time_c_list.append(time)
        
    for i in range(30,37):
        tPY_start = perf_counter()
        fib(i)
        tPY_stop = perf_counter()
        time = tPY_stop-tPY_start+3
        time_PY_list.append(time)
        


    #fig = plt.figure()
    plt.plot([range(30,37)], [time_c_list], 'ro')
    plt.plot([range(30,37)], [time_PY_list], 'bo')
    plt.axis([30, 37, 0, 30])
    plt.savefig('testfibplot.png')
    

if __name__ == "__main__":
    main()