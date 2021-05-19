# -*- coding: utf-8 -*-
"""
Created on Wed May 19 19:52:15 2021

@author: Hampus
"""

""" Program that estimates the value of PI by using Monte Carlo method"""

import random
import math
import matplotlib.pyplot as plt


def estimate_PI_MC(n):
    
    no_points_in_circle = 0
    x_points_inside = []
    y_points_inside = []
    x_points_outside = []
    y_points_outside = []
    for i in range(n):
        
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)
        
        if rand_x**2 + rand_y**2 <= 1:
            no_points_in_circle += 1
            x_points_inside.append(rand_x)
            y_points_inside.append(rand_y)
        else:
            x_points_outside.append(rand_x)
            y_points_outside.append(rand_y)
        
    print(f'Number of points inside the circle: {no_points_in_circle}')
    
    pi_estimate = 4*no_points_in_circle/n
    print(f'Estimate of PI with {n} points: {pi_estimate}')
    print(f'"Real" vale of PI: {math.pi}')
    
    plt.plot(x_points_inside, y_points_inside, 'ro')
    plt.plot(x_points_outside, y_points_outside, 'bo')
    plt.axis([-1,1,-1,1])
    
    

def main():
    estimate_PI_MC(10)
    

if __name__ == "__main__":
    main()