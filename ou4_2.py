
#!/usr/bin/env python3

from heltal import Heltal
from heltal import fib_py
from time import perf_counter


def main():
	f = Heltal(5)
	print(f.get())
	f.set(7)
	print(f.get())
	f.set(10)
	print(f.get())
	print("Testing fibonacci method with C++: computing 10th value")
	print(f.fib())
	#fib10 =  fib_py(Heltal(10))
	#print(fib10)
	print("Testing fibonacci method(python): computing 10th value")
	fib10 = fib_py(10)
	print(fib10)
def main():
    f = Heltal(5)
    print(f.get())
    f.set(7)
    print(f.get())
    print()
    f.set(10)
    print(f.get())
    print("Testing fibonacci method with C++: computing 10th value")
    t1_start = perf_counter()
    print(f.fib())
    t1_stop = perf_counter()
    print()
    print("Elapsed time for C++ solving fibonacci: ", t1_stop-t1_start)
    print("Testing fibonacci method(python): computing 10th value")
    t2_start = perf_counter()
    print(fib_py(10))
    t2_stop = perf_counter()
    print()
    print("Elapsed time for C++ solving fibonacci: ", t2_stop-t2_start)


if __name__ == '__main__':
	main()
