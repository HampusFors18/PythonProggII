# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:56:49 2021

@author: Hampus
"""
import numpy as np
import matplotlib.pyplot as plt

me=5.48579909070e-4 #u
mn=1.00866491588    #u
mp=1.007276466621   #u
muc2=931.49410242 #MeV
c = 299792458 #m/s

nuclides={'H2': {'Z': 1, 'A': 2, 'm': 2.01410177812},
        'H3': {'Z': 1, 'A': 3, 'm': 3.0160492779},
        'He3': {'Z': 2, 'A': 3, 'm': 3.0160293201},
        'He4': {'Z': 2, 'A': 4, 'm': 4.002603254},
        'Li6': {'Z': 3, 'A': 6, 'm': 6.0151228874},
        'O16': {'Z': 8, 'A': 16, 'm': 15.99491461957},
        'S34': {'Z': 16, 'A': 34, 'm': 33.96786701},
        'Fe56': {'Z': 26, 'A': 56, 'm': 55.9349375},
        'Ni62': {'Z': 28, 'A': 62, 'm': 61.92834537},   
        'Kr84': {'Z': 36, 'A': 84, 'm': 83.9114977282},
        'Sn119': {'Z': 50, 'A': 119, 'm': 118.90331117},
        'Ti205': {'Z': 81, 'A': 205, 'm': 204.9744278},
        'U238': {'Z': 92, 'A': 238, 'm': 238.0507884}}

def BAZ(A,Z,m):
    """Function to calculate the binding energy per nucleon
    
    Parameters
    ----------
    A : int
        Mass number of nuclide
    Z : int
        Proton number of nuclide
    m : float
        Mass of the nuclide
    """
    utoEV = 931.4941 #MeV/c^2 (1 u = 931.4941 MeV)
    mpeV = mp*utoEV
    mneV = mn*utoEV
    
    
    eps = (Z*mp+(A-Z)*mn - m)*utoEV
    return eps/A

def BAZ_BW(A,Z):
    """Function to calculate the binding energy per nucleon
    with the semi-empirical formula
    
    Parameters
    ----------
    A : int
        Mass number of nuclide
    Z : int
        Proton number of nuclide
    """
    delta = 0    
    
    if A % 2 == 0 and (A-Z) % 2 == 0:
        delta = 1
    elif (A % 2) != 0 and ((A-Z) % 2) != 0:
        delta = -1
    else:
        delta = 0
        
    pairTerm = 34*delta*A**(-3/4)
    eps = 15.75*A - 94.8*((A/2-Z)**2/A) - 17.8*A**(2/3) - 0.71*Z**2*A**(-1/3) + pairTerm
    #print('Pair Term: ', pairTerm)
    #print('eps: ', eps)
    
    return eps/A

#your code to apply these functions and to plot the results comes here.
def main():
    bindEnergyList = []
    for key in nuclides:
        temp = BAZ(nuclides[key]['A'], nuclides[key]['Z'], nuclides[key]['m'])
        bindEnergyList.append(temp)
        print(temp)
        
    atomicNumberList = []
    for key in nuclides:
        atomicNumberList.append(nuclides[key]['A'])
    print(atomicNumberList)
    
    bindEnergyListSemi = []
    for key in nuclides:
        #print('Atomic key: ', key)
        temp = BAZ_BW(nuclides[key]['A'], nuclides[key]['Z'])
        bindEnergyListSemi.append(temp)
        print('Energy: ', temp)
    
    maxNum = max(bindEnergyList)
    print(maxNum)
        
        
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(atomicNumberList, bindEnergyList, 'ro')
    plt.plot(atomicNumberList, bindEnergyListSemi)
    plt.xlabel('Atomic number')
    plt.ylabel('Binding energy MeV')
    plt.annotate(r'$Ni62$',(59,7.5))
    plt.show()
    
    
if __name__ == "__main__":
    main()