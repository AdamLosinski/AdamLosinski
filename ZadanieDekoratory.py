#dekorowane fukcje wypisywały informacje przydatne przy debugowaniu nazwa, argumenty
#dekorator zlicza ilość wywołań funkcji, ile razy funkcję wywołano, wypisuje liczbę dotychczasowych wywołań

#!/usr/bin/python3
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def debug(*args, **kwargs):
        print(func.__name__)
        for el in args:
            print(el)
        for key, value in kwargs.items():
            print('{0}={1}'.format(key,value))
        return func(*args, **kwargs)
    return debug
    
def my_decoratorcounter(func):
    def counter(*args, **kwargs):
        counter.calls += 1
        print('Function was called: ' + str(counter.calls))
        return func(*args, **kwargs)
    counter.calls = 0
    return counter
    
@my_decorator
def f():
    print('Function without arguments')
    
@my_decorator    
def g(*args, **kwargs):
    print('Function with arguments')
    
@my_decoratorcounter
def h():
    print('Function called multiple times')  
  

def main():
    f()
    g(1,2,3,4,5,6,a='7',b='8',c='9')
    for i in range(5):
        h()
    
if __name__ == '__main__':
    main()	
