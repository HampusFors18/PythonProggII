
#!/usr/bin/env python3

from heltal import Heltal
from heltal import fib_py
from time import perf_counter
import matplotlib.pyplot as plt



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
    t1_start = perf_counter()
    print(f.fib())
    t1_stop = perf_counter()
    print()
    print("Elapsed time for C++ solving fibonacci: ", t1_stop-t1_start)
    print("Testing fibonacci method(python): computing 35th value")
    t2_start = perf_counter()
    print(fib_py(35))
    t2_stop = perf_counter()
    print()
    print("Elapsed time for C++ solving fibonacci: ", t2_stop-t2_start)
    
    
    for i in range(30,45):
        print("Setting value of i:")
        f.set(i)
        print(f.get())
        print("Fibonacci numer of that i:")
        tC_start = perf_counter()
        print(f.fib())
        tC_stop = perf_counter()
        print("Elapsed time for that number: ", tC_start-tC_stop)
        


    #fig = plt.figure()
    

if __name__ == '__main__':
	main()
