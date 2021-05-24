# -*- coding: utf-8 -*-
"""
Created on Wed May 19 19:52:15 2021

@author: Hampus
"""

""" Program that estimates the value of a hypersphere by using Monte Carlo method"""

import random
import math
import functools
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future




def estimate_hyper_MC(n, d):
    
    r = 1
    no_points_in_hypersphere = 0
    for i in range(n):
        
        sphere_list = [random.uniform(-1, 1)**2 for x in range(d)]
        
        if functools.reduce(lambda x,y : x+y, map(abs,sphere_list)) <= 1 :
            no_points_in_hypersphere += 1
    
    volume_estimate = no_points_in_hypersphere/n*2**d*r**2                 #Hit/miss * volume of hypercube
    
    hyper_sphere_volume = math.pi**(d/2)/(math.gamma((d/2)+1))*r**d
    
    return no_points_in_hypersphere, volume_estimate, hyper_sphere_volume
    
    
    

def main():
    t1_start = pc()
    results = estimate_hyper_MC(10000000,11)
    t1_end = pc()
    print("Elapsed time:", t1_end - t1_start)
    print('Number of points in hypersphere: ', results[0])
    print('Volume estimate of hypersphere: ', results[1])
    print('Calculated colume of hypersphere: ', results[2])
    print()
    print()
    
    print('Testing method with 10 parallell processes')
    
    t2_start = pc()
    with future.ProcessPoolExecutor() as ex:
        p1 = ex.submit(estimate_hyper_MC, 1000000, 11)
        p2 = ex.submit(estimate_hyper_MC, 1000000, 11)
        p3 = ex.submit(estimate_hyper_MC, 1000000, 11)
        p4 = ex.submit(estimate_hyper_MC, 1000000, 11)
        p5 = ex.submit(estimate_hyper_MC, 1000000, 11)
        p6 = ex.submit(estimate_hyper_MC, 1000000, 11)
        p7 = ex.submit(estimate_hyper_MC, 1000000, 11)
        p8 = ex.submit(estimate_hyper_MC, 1000000, 11)
        p9 = ex.submit(estimate_hyper_MC, 1000000, 11)
        p10 = ex.submit(estimate_hyper_MC, 1000000, 11)
        r1 = p1.result()
        r2 = p2.result()
        r3 = p3.result()
        r4 = p4.result()
        r5 = p5.result()
        r6 = p6.result()
        r7 = p7.result()
        r8 = p8.result()
        r9 = p9.result()
        r10 = p10.result()
    t2_end = pc()
    print("Elapsed time:", t2_end - t2_start)
    p_results1 = r1[0] + r2[0] + r3[0] + r4[0] + r5[0] + r6[0] + r7[0] + r8[0] + r9[0] + r10[0]
    p_results2 = (r1[1] + r2[1] + r3[1] + r4[1] + r5[1] + r6[1] + r7[1] + r8[1] + r9[1] + r10[1])/10
    p_results3 = (r1[2] + r2[2] + r3[2] + r4[2] + r5[2] + r6[2] + r7[2] + r8[2] + r9[2] + r10[2])/10
    print('Number of points in hypersphere: ', p_results1)
    print('Volume estimate of hypersphere: ', p_results2)
    print('Calculated volume of hypersphere: ', p_results3)
    print()
        
    print('All done')
    
    

if __name__ == "__main__":
    main()