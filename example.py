# -*- coding: utf-8 -*-
"""
Created on Fri May 21 16:43:19 2021

@author: Hampu
"""

from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future

def runner(n):
    print(f"Performing a costly function {n}")
    pause(1)
    return f"Function {n} has completed"
    
if __name__ == "__main__":
    start= pc()
    with future.ThreadPoolExecutor() as ex:
        p = [5, 4, 3, 2, 1]
        results = ex.map(runner, p)
        for r in results:
            print(r)
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")
        
        
    
