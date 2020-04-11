#!/usr/bin/python3

class MyDeco:
	
	def __init__(self, func):
		self.__func = func
		self.counter = 0
	
	def __call__(self, *args, **kwargs):
		self.counter +=1
		print('Function was called: ' + str(self.counter))
		return self.__func(*args, **kwargs)
	

class MyIterator:
	
	def __init__(self, max_val):
		self.__current_val = 0
		self.__max_val = max_val
		self.a = 0
		self.b = 1
		

	def __iter__(self):
		return self

	
	def __next__(self):
		self.__current_val += 1
		tmp = self.a
		self.a, self.b = self.b, self.a + self.b

			
		if self.__current_val >= self.__max_val:
			raise StopIteration
		return tmp
	
@MyDeco		
def f():
	return
	
def main():
	
	obj = MyIterator(10)	
	it = iter(obj)
	for el in it:
		f()
		print(el)

	
if __name__ == '__main__':
	main()
