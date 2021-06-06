
#!/usr/bin/env python3

from heltal import Heltal
from heltal import fib_py
from time import perf_counter
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches



def main():
    time_c_list = []
    time_py_list = []
    f = Heltal(5)
    print(f.get())
    f.set(7)
    print(f.get())
    print()
    f.set(35)
    print(f.get())
    print("Testing fibonacci method with C++: computing 35th value")
    print('Fibonacci value:')
    t1_start = perf_counter()
    print(f.fib())
    t1_stop = perf_counter()
    print()
    print("Elapsed time for C++ solving fibonacci: ", t1_stop-t1_start)
    print()
    print()
    print()
    print("Testing fibonacci method(python): computing 35th value")
    print('Fibonacci value:')
    t2_start = perf_counter()
    print(fib_py(35))
    t2_stop = perf_counter()
    print()
    print("Elapsed time for python solving fibonacci: ", t2_stop-t2_start)
    
    
    for i in range(30,40):
        f.set(i)
        tC_start = perf_counter()
        f.fib()
        tC_stop = perf_counter()
        time = tC_stop-tC_start
        time_c_list.append(time)
        
    for i in range(30,40):
        tpy_start = perf_counter()
        fib_py(i)
        tpy_stop = perf_counter()
        time = tpy_stop-tpy_start
        time_py_list.append(time)
        
        


    #fig = plt.figure()
    plt.plot([range(30,40)], [time_c_list], 'ro')
    #linec, = plt.plot([range(30,40)], [time_c_list], 'ro')
    #linec_legend = plt.legend(handles=[linec], loc='upper right')
    plt.plot([range(30,40)], [time_py_list], 'bo')
    #linepy, = plt.plot([range(30,40)], [time_py_list], 'bo')
    #linepy_legend = plt.legend(handles=[linepy], loc='upper left')
    plt.axis([30, 40, 0, 100])
    #plt.gca().add_artist(linec_legend)
    #plt.gca().add_artist(linepy_legend)
    plt.savefig('testfibplot.png')
    

if __name__ == '__main__':
	main()
