# -*- coding: utf-8 -*-
""" 
Datalab 1 Computational Reactor Physics with Python

"""


unit_dict = {
    "s": 1,
    "m": 60,
    "h": 3600,
    "d": 3600*24,
    "y": 3600*24*365
    }

def decayConst(hl,unit):
    """
    Function that calculates the decay constant

    Parameters
    ----------
    hl : float
        half-life of element.
    unit : string
        which type of time unit used.

    Raises
    ------
    ValueError
        If unit is not in dictionary.

    Returns
    -------
    lam : float
        decay constant in 1/s.

    """
    import math
    if unit in unit_dict:
        lam = math.log(2)/(hl*unit_dict[unit])
    else:
        raise ValueError("Unit needs to be either 's', 'm', 'h', 'd' or 'y'")  
    return lam


isotopes = {
    'Y-91': 58.5,
    'Zr-95': 64,
    'Nb-95': 35,
    'Ru-103': 39.2,
    'Ru-106': 372,
    'Sb-125': 2.76*365,
    'Cs-134': 2.065*365,
    'Cs-137': 30.1*365,
    'Eu-154': 8.6*365,
    'Eu-155': 4.75*365,          
    'Ce-141': 32.5,
    'Ce-144': 285
    }

isotopeInfo = {}

def isotopeInfoFunction():
    """
    Function that organizes information into a nested dictionary

    Returns
    -------
    None.

    """
    
    for key in isotopes:
        isotopeInfo[key] = {'hl': isotopes.get(key), 'lambda': decayConst(isotopes.get(key), 'd')}
        
activity = {}
    
def fileOpener():
    """
    Opens a file

    Returns
    -------
    content : list
        list of all information in file by line.

    """
    with open('C:/Users/Hampu/Documents/PythonProggII/ComputationalReactorPhysics/Datalabs_tasks/Datalabs/Datalab01/01-Sample.txt', 'r') as myFile:
        content = myFile.readlines()
    return content

def readingLinesToList(file):
    """
    Function to strip content of a file into a list with the neccesary information

    Parameters
    ----------
    file : file
        a text file.

    Returns
    -------
    strippedFile : list
        list with stripped information.

    """
    strippedFile = []
    temp = []
    for line in file:
        temp.append(line.strip().split())
        
    """Remove unneccesary information"""    
    strippedFile = [x for x in temp if len(x) == 4]
    
        
    return strippedFile

def listToDict(lista):
    
    for i in range(len(lista)):
        activity[lista[i][1] + '-' + lista[i][2]] = float(lista[i][3])



def main():
    print(decayConst(2,'s'))
    print(decayConst(2,'m'))
    print(decayConst(2,'h'))
    print(decayConst(2,'d'))
    print(decayConst(2,'y'))
    #print(decayConst(2, 'g'))
    print()
    
    isotopeInfoFunction()
    print(isotopeInfo)
    print()
    
    readFile = fileOpener()
    someList = readingLinesToList(readFile)
    print(someList)
    listToDict(someList)
    print()
    print(activity)
    
    
if __name__ == "__main__":
    main()
    