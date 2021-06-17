# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 20:59:25 2021

@author: Hampus
"""

import numpy as np
import matplotlib.pyplot as plt

def derivDaughter(t,y,lp,ld, ld2, ld3):
    A=np.array([[-lp,0.0, 0.0, 0.0],[lp,-ld, 0.0, 0.0], [0.0, ld, -ld2, 0.0], [0.0, 0.0, ld2, -ld3]])
    return np.dot(A,y)

from scipy.integrate import solve_ivp


"""units in kyears"""
U234HL = 245.5
lamU234HL = np.log(2)/U234HL
Th230HL = 75.38
lamTh230HL = np.log(2)/Th230HL
Ra226HL = 1602*10**-3
lamRa226HL = np.log(2)/Ra226HL
Rn222HL = 3.82/365*10**-3
lamRn222HL = np.log(2)/Rn222HL



N0=5000000
Tstart=0.0
Tend=15 #kyears
Neval=50
T_eval=np.linspace(Tstart,Tend, Neval)
sol=solve_ivp(derivDaughter,(Tstart,Tend),[N0,0.0, 0.0, 0.0],t_eval=T_eval,args=(lamU234HL, lamTh230HL, lamRa226HL, lamRn222HL))

plt.figure()
plt.plot(sol.t,sol.y[0],label='U-234')
plt.plot(sol.t,sol.y[1],label='Th-230')
plt.plot(sol.t,sol.y[2],label='Ra-226')
plt.plot(sol.t,sol.y[3],label='Rn-222')
plt.xlabel('time (ky)')
plt.legend()
plt.ylabel('Number of nuclei')
plt.show()