# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:16:38 2021

@author: Hampus

"""

import random
import math
import functools
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future




def estimate_hyper_MC(l):
    n,d = l
    r = 1
    no_points_in_hypersphere = 0
    for i in range(n):
        
        sphere_list = [random.uniform(-1, 1)**2 for x in range(d)]
        
        if functools.reduce(lambda x,y : x+y, map(abs,sphere_list)) <= 1 :
            no_points_in_hypersphere += 1
    
    volume_estimate = no_points_in_hypersphere/n*2**d*r**2                 #Hit/miss * volume of hypercube
    
    hyper_sphere_volume = math.pi**(d/2)/(math.gamma((d/2)+1))*r**d
    
    return no_points_in_hypersphere, volume_estimate, hyper_sphere_volume
    


if __name__== "__main__":
    n = 1000000
    d = 11
    start= pc()
    with future.ProcessPoolExecutor() as ex:
        p = [(n,d) for _ in range(10)]
        results = ex.map(estimate_hyper_MC, p)
        for r in results:
            print(r)
    end= pc()
    print(f"Process took{round(end-start,2)}seconds")