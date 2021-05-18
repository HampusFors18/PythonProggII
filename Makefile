# Makefile for OU4
all:
	g++ -c -fPIC heltal.cpp -o heltal.o
	g++ -shared -o libheltal.so  heltal.o	
clean:
	rm -fr *.o *.so __pycache__
