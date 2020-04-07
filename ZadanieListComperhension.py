#!/usr/bin/python3
def main():
	my_list = list(range(1000))
	print([el for el in my_list if all(el%i != 0 for i in range(2,el))])
	
	
	
if __name__ == '__main__':
	main()
