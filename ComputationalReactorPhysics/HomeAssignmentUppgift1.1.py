# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 21:01:55 2021

@author: Hampus
"""

import numpy as np
import matplotlib.pyplot as plt

def epsilon(t):
    """Function to evaluate Uranium enrichment at time t. The parameter t can be both float or array."""
    const = 0.0072/99.28
    halfLifeU235 = 7.13*10**8
    halfLifeU238 = 4.51*10**9
    upper_eps = 100*const*(1/2)**(t/halfLifeU235)
    lower_eps = const*(1/2)**(t/halfLifeU235) + (1/2)**(t/halfLifeU238)
    
    eps = upper_eps/lower_eps
    return eps

def main():
    print('Enrichment at the beginning of earth: ', epsilon(-4.5*10**9))
    print('Enrichment at Okla: ', epsilon(-1.7*10**9))


    a = np.linspace(-4.5*10**9, 0, num=20)
    
    b = epsilon(a)
    
    #print(b)
    
    fig = plt.figure()
    plt.plot(a,b, 'ro')
    plt.axvline(-4.5*10**9)
    plt.axvline(-1.7*10**9)
    plt.ylabel('Enrichment')
    plt.xlabel('Time')
    plt.annotate(r'$-1.7x10^9$',(-1.6*10**9,0.15))
    plt.annotate(r'$-4.5x10^9$',(-4.4*10**9,0.10))
    plt.show()
    
if __name__ == "__main__":
    main()