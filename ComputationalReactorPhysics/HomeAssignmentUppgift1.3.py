# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 19:07:53 2021

@author: Hampus
"""


import os
import re
import matplotlib.pyplot as plt
import pandas as pd

spentFueldict = {}

def fileDirectoryList():
    path = 'C:/Users/Hampu/Documents/PythonProggII/ComputationalReactorPhysics/HA1/HA1/train'
    dirList = os.listdir(path)
    return dirList

    
def getNuclearInfoReadFile(filename):
    os.chdir('C:/Users/Hampu/Documents/PythonProggII/ComputationalReactorPhysics/HA1/HA1/train')
    with open(filename) as f:
        contents = f.readlines()
        
    temp = []
    for line in contents:
        temp.append(line.strip().split())  
        
    return temp

def listToDict(filename, num):
        
    BU_CT_number_list = [float(s) for s in re.findall(r'[+-]?\d+\.\d+', filename)]
    
    spentFueldict[num] = {}
    spentFueldict[num]['BU'] = BU_CT_number_list[0]
    spentFueldict[num]['CT'] = BU_CT_number_list[1]
    
    concentrationList = getNuclearInfoReadFile(filename)
    
    for i in range(6,len(concentrationList)):
        spentFueldict[num][concentrationList[i][0]] = float(concentrationList[i][1])
        
        
def concPlotCs137():
    
    fueldata = pd.DataFrame(spentFueldict)
    fueldata_trans = fueldata.transpose()
    
    ctSubfuel_1 = fueldata_trans[(fueldata_trans['CT']>5) & (fueldata_trans['CT']<10)]
    ctSubfuel_2 = fueldata_trans[(fueldata_trans['CT']>10) & (fueldata_trans['CT']<15)]
    ctSubfuel_3 = fueldata_trans[(fueldata_trans['CT']>15) & (fueldata_trans['CT']<20)]
    ctSubfuel_4 = fueldata_trans[(fueldata_trans['CT']>20) & (fueldata_trans['CT']<25)]
    ctSubfuel_5 = fueldata_trans[(fueldata_trans['CT']>25)]
    
    
    plt.figure()
    #plt.plot(fueldata_trans['BU'],fueldata_trans['55137.15c'],'x')
    plt.plot(ctSubfuel_1['BU'], ctSubfuel_1['55137.15c'], 'bx')
    plt.plot(ctSubfuel_2['BU'], ctSubfuel_2['55137.15c'], 'rx')
    plt.plot(ctSubfuel_3['BU'], ctSubfuel_3['55137.15c'], 'gx')
    plt.plot(ctSubfuel_4['BU'], ctSubfuel_4['55137.15c'], 'yx')
    plt.plot(ctSubfuel_5['BU'], ctSubfuel_5['55137.15c'], 'mx')
    plt.xlabel('Burnup (MWd/kgU)')
    plt.ylabel(r'Cs-137 concentration $(10^{24}/cm^3)$ ')
    plt.show()
    
    
        
def beqConversion():
    
    
    

def main():
    i = 1
    for line in fileDirectoryList():
        listToDict(line, i)
        i += 1
    
    concPlotCs137()
    #print(spentFueldict)
    
if __name__ == "__main__":
    main()