# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:52:05 2021

@author: Hampus
"""


"""


Investment calculator - Compound interest


"""


from tabulate import tabulate


start_value = 35000            #kronor

compound_interest = 0.07           #percentage value

monthly_contributions = 800    #kronor

time_of_savings = 20            #years

skatt = 0

courtage = 0

amount_money = start_value

i = 1

monthly_compound_interest = (1 + compound_interest)**(1/12)-1

list_table = []
avkast_list = []

for j in range(time_of_savings + 1):
    list_table.append([])

list_table[0].append('År')
list_table[0].append('Startvärde')
list_table[0].append('Årets sparande')
list_table[0].append('Avkastning')
list_table[0].append('Skatt')
list_table[0].append('Värde vid årets slut')
#print('--------------------')
#print(list_table)

while i < time_of_savings + 1:
    
    avkast_list = []
    list_table[i].append(i)
    list_table[i].append(amount_money)
    list_table[i].append(12*monthly_contributions)
    
    
    for x in range(12):
        
        if x == 0:
            Q1 = amount_money
        if x == 3:
            Q2 = amount_money
        if x == 6:
            Q3 = amount_money
        if x == 9:
            Q4 = amount_money
        
        temp_prev = amount_money                #for avkast list
        
        amount_money = amount_money*(1 + monthly_compound_interest)
        
        temp_after = amount_money - temp_prev       #For avkast list, avkastning per månad
        
        avkast_list.append(temp_after)
        
        avkastning = sum(avkast_list)       #Summerar avkastningen för varje månad
        
        amount_money = amount_money + monthly_contributions
    
    
    list_table[i].append(avkastning)
        
    
    schablon = (Q1+Q2+Q3+Q4+12000)/4

    skatt = schablon*0.0125*0.30
    list_table[i].append(skatt)
    
    amount_money = amount_money - skatt
    list_table[i].append(amount_money)
    
    
    i = i + 1
    
    


print(tabulate(list_table, headers='firstrow', tablefmt='grid'))