# -*- coding: utf-8 -*-
"""
Created on Wed May 19 19:52:15 2021

@author: Hampus
"""

""" Program that estimates the value of PI by using Monte Carlo method"""

import random


def estimate_PI_MC(n):
    
    points_in_circle = 0
    for i in range(n):
        
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)        
        
        if rand_x**2 + rand_y**2 <= 1:
            points_in_circle += 1
        
    print(f'Number of points inside the circle: {points_in_circle}')
    
    

def main():
    estimate_PI_MC(100)
    

if __name__ == "__main__":
    main()