#!/usr/bin/env python3

from heltal import Heltal
from heltal import fib_py

def main():
	f = Heltal(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print()
	f.set(10)
	print(f.get())
	print("Testing fibonacci method with C++: computing 10th value")
	f.fib()
	print(f.fib())
	#fib10 =  fib_py(Heltal(10))
	#print(fib10)
	print("Testing fibonacci method(python): computing 10th value")
	fib10 = fib_py(10)
	print(fib10)



if __name__ == '__main__':
	main()
