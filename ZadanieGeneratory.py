#!/usr/bin/python3

def my_gen(N):
	a, b = 0, 1
	for el in range(N):
		a, b = b, a + b
		yield a
		
def main():
	obj = my_gen(100)
	seq = list(obj)
	print(seq)
	
	
if __name__ == '__main__':
	main()
