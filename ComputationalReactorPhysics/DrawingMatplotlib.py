# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:04:26 2021

@author: Hampus
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def simple2DRectanglePlot():
    a=10.0
    fig, ax = plt.subplots()
    #defining the hexagon through its corners.
    rect=plt.Polygon([[-a/2,0.0],[-a/2,a/2],[a/2,a/2],
                        [a/2,0.0],[a/2, -a/2],[-a/2, -a/2]],facecolor='white',edgecolor='black')
    ax.add_artist(rect)
    plt.axvline(0.0,color='black')
    plt.axhline(0.0,color='black')
    plt.annotate(r'$y=\frac{1}{2}a$',(a*0.1,a*0.6)) #write this expression to that location
    plt.annotate(r'$x=\frac{1}{2}a$',(a*0.6,a*0.25))
    plt.annotate(r'$\frac{1}{2}a$',(a*0.53,0.5))
    plt.annotate(r'$-\frac{1}{2}a$',(-a*0.7,0.5))
    plt.xlim(-a,a)
    plt.ylim(-a,a)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().spines['right'].set_visible(False)#Switch off frame on right
    plt.gca().spines['top'].set_visible(False)#Switch off frame on top
    plt.show()

def hexFunc(x,y,a):
    """Function which disappears on the edge of a rectangle
    
    Parameters
    ----------
    X : ndarray
        meshgrid X values.
    Y : ndarray
        meshgrid Y values
    a : size of the rectangle
    """
    z = np.zeros(x.shape)
    mask = (y<=1/2*a)*(y>=-1/2*a) * \
            (x<=1/2*a)*(x>=-1/2*a)
    z[mask] = np.cos(y[mask]*np.pi/a)*np.cos(x[mask]*np.pi/a)
    return z


def simple3DRectanglePlot():

    a=10 #cm
    X = np.linspace(-a, a, 1000)
    Y = np.linspace(-a, a, 1000)
    Xn, Yn = np.meshgrid(X, Y)
    
    Z=hexFunc(Xn,Yn,a)
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf=ax.plot_surface(Xn, Yn, Z, cmap="plasma")
    fig.colorbar(surf)
    plt.show()
    
    plt.figure()
    plt.contour(Xn,Yn,Z)
    plt.axis('equal')
    plt.colorbar()
    plt.show()
    


def main():
    simple2DRectanglePlot()
    simple3DRectanglePlot()
    
    
if __name__ == "__main__":
    main()