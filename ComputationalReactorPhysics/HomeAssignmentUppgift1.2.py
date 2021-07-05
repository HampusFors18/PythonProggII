# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 20:49:24 2021

@author: Hampus
"""
import numpy as np
import ComputationalReactorphysicsBindingEnergy as crpBE
import matplotlib.pyplot as plt


isotopes = {}


def readFromFile():
    
    with open('C:/Users/Hampu/Documents/PythonProggII/ComputationalReactorPhysics/HA1/HA1/HA1-relmass.txt') as f:
        contents = f.readlines()
    return contents

def linesToDict(fileContent):
    
    temp = []

    for line in fileContent:
        temp.append(line.strip().split())        
       
    
    for i in range(0,len(temp),8):
       isotopes[temp[i+1][3] + temp[i+2][3]] = {}       #Making nested dictionary for every isotope
    
    x = 0
    for key in isotopes:
        isotopes[key]['Z'] = int(temp[0+x][3])               #Adding values to every isotope
        isotopes[key]['A'] = int(temp[2+x][3])               #Every 8th row is a new isotope
        isotopes[key]['m'] = stripNumber(temp[3+x][4])
        x += 8
    
def addingEPS():
    for key in isotopes:
        isotopes[key]['eps'] = crpBE.BAZ(isotopes[key]['A'], isotopes[key]['Z'], isotopes[key]['m'])
        

def stripNumber(tal):
    
    #function that just takes away parentheses
    
    temp = ''
    for digit in tal:
        if digit == '.':
            temp += digit
        elif not digit.isnumeric():
            break
        else:
            temp += digit
    return float(temp)

def maxBindingEnergy():
    max_value = 0
    for key in isotopes:
        if isotopes[key]['eps'] > max_value:
            max_value = isotopes[key]['eps']
            max_key = key
        else: 
            pass
    return max_key

def twoDNumpyArray():
    NZ = np.zeros((119,178))
    #NZ[:] = np.NaN
    prev_key = 'H1'
    i = 0
    j = 0
    for key in isotopes:
        if isotopes[key]['Z'] == isotopes[prev_key]['Z']:
            NZ[j,i] = isotopes[key]['eps']
            i += 1
        else:
            j += 1
            i = 0
            NZ[j,i] = isotopes[key]['eps']
            prev_key = key
            i += 1
    
    return NZ
            
            
        
        
        
    #NZ[0,0]=isotopes['H1']['eps']
    #print(NZ)
    

    
def main():
    cont = readFromFile()
    linesToDict(cont)
    addingEPS()
    print(isotopes['H1'])
    print(isotopes['D2'])
    print(isotopes['T3'])
    print(isotopes['Ni62'])
    print(isotopes['Og295'])
    print()
    print('The max bidning energy have: ', maxBindingEnergy())
    print()
    numIMG = twoDNumpyArray()
    print(numIMG)
    
    plt.figure()
    plt.imshow(numIMG)
    plt.colorbar()
    plt.show()
    
    
if __name__ == "__main__":
    main()