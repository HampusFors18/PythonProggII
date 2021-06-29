# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 19:37:21 2021

@author: Hampus
"""

import pandas as pd

fueldata=pd.read_csv('C:/Users/Hampu/Documents/PythonProggII/ComputationalReactorPhysics/Datalabs_tasks/Datalabs/Datalab03/03-sample.csv',header = 0, usecols=['BU','CT','IE','Cs134','Cs137','Eu154','U235','Pu239'])


subfuel=fueldata[(fueldata['BU']>40) & (fueldata['BU']<50) & (fueldata['IE']>2.5) & (fueldata['IE']<3.5) & (fueldata['CT']>3065) & (fueldata['CT']<6130)]

print(subfuel)
print()

print('Number of fuels that are conforming to the above conditions are : ', len(subfuel))



