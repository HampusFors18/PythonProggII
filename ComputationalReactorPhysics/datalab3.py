# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 20:42:02 2021

@author: Hampus
"""

import re
import functools

class Material:
    """A class used to represent a Material.
    Parameters
    ----------
    nuclides : dict
      Dictionary to store nuclides. Keys nuclide identifiers, values atomic fraction.
    density : dict
      Density of material in g/cm3
    Attributes
    ----------
    nuclides : dict
        Dictionary to store nuclides. Keys nuclide identifiers, values atomic fraction.
    density : float
        Density of material in g/cm3
    """

    def __init__(self, nuclides={},density=None):
        """Function to initialize an instance of Material()"""
        self.nuclides = nuclides
        self.density = density
        
    def __repr__(self):
        if self.density is None:
            return "This is a material with no specified density"
        else:
            return "This is a material with density %.2f" %self.density

    def add_nuclide(self, symbol, fraction):
        """The method adds or updates the atomic fraction of a nuclide.
        
        Parameters
        ----------
        symbol : str
            Symbol of the nuclide (eg. U-238)
        fraction : float
            Atomic fraction of the nuclide.
        """
        self.nuclides[symbol]=fraction
        
    def set_density(self, density=None):
        """Method to set the density of the Material.
        
        Parameters
        ----------
        density : float
            density of material in g/cm2
        """
        self.density=density
        
    def get_density(self,unit='g/cm3'):
        """Method to get the density of the instance."""
        if self.density is None:
            raise ValueError('Density is not specified yet')
        elif unit=='g/cm3':
            return self.density
        elif unit=='kg/m3':
            return self.density*1000
        else:
            ValueError('Only g/cm3 and kg/m3 are available')
            
    def massDToAtomD(self):
        """
        

        Raises
        ------
        ValueError
            When the atomic fractions does not equal one.

        Returns
        -------
        atomicDensity : float
            The number of atoms per cm^3

        """
        sum = 0
        atomicMolarList = []
        NA = 6.022*10**23       #Avogadros number
        for key in self.nuclides:
            sum += self.nuclides[key]
            
        if sum != 1:
            raise ValueError(f'The total atomic fraction is equal to: {sum}, but should be equal to 1.')
        else:
            for key,value in self.nuclides.items():
                temp = re.findall(r'\d+', key)              #find the number i.e '27' in the string 'Al27'
                res = list(map(int, temp))                  #map it to list as int
                atomicMolarList.append(res[0]*value)        #weighted list of molarmass for every istotope
            atomicDensity = self.get_density()/(functools.reduce(lambda a, b: a+b, atomicMolarList))*NA     #calculate the atomic density
        return atomicDensity
    
    """
    
    (densitet / summan av den viktade molmassan) * avagadros nummer = atomdensiteten
    
    """
            
            
def main():
    iron = Material()
    print(iron)
    aluminium = Material({'Al27': 0.5, 'Al25': 0.5},density=3.6)
    print(aluminium)
    print('Atom density of aluminium: ', aluminium.massDToAtomD())
    uranium = Material({'U238': 1}, density=19.05)
    print('Atom density of Uranium: ', uranium.massDToAtomD())
    potassium = Material({'K39': 0.9213, 'K40': 0.0117, 'K41': 0.067}, density = 0.89)
    print('Atom density of potassium: ', potassium.massDToAtomD())
    
    
if __name__ == "__main__":
    main()