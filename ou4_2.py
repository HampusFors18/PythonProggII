#!/usr/bin/env python3

from heltal import Heltal

def main():
	f = Heltal(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print()
	fib10 =  fib_py(Heltal(10))
	print(fib10)



if __name__ == '__main__':
	main()
