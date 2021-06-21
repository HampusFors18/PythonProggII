# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 21:01:55 2021

@author: Hampus
"""

def extractJsonData():
    import json
    with open('C:/Users/Hampu/Documents/PythonProggII/ComputationalReactorPhysics/Datalabs_tasks/Datalabs/Datalab03/03-sample.json') as json_file:
        inventory = json.load(json_file)
        
        
    ingestionAndTimeValues = [(inventory['inventory_data'][i]['ingestion_dose'],\
                               inventory['inventory_data'][i]['irradiation_time'],\
                               inventory['inventory_data'][i]['cooling_time'])  \
                              for i in range(len(inventory['inventory_data']))]
    return ingestionAndTimeValues
        
def calcTime(data):
    sumTime = 0
    for i in range(len(data)):
        if data[i][1] != data[i-1][1]:
            sumTime += data[i][1]
        else:
            sumTime += data[i][2]
    return sumTime

def main():
    data = extractJsonData()
    print('The total time (in seconds): ', calcTime(data))
    
    
if __name__ == "__main__":
    main()