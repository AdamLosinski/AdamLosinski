from stack import Stack
from stack import Stack2


def main():
    stack = Stack2()


    stack.push(3)
    stack.push(8)
    stack.push(2)
    stack.push(3)
    stack.push(1)
    stack.push(8)

    while not stack.is_empty():
        print("Stack top is: ", stack.top())
        stack.look_for_min()
        stack.pop()


if '__main__' == __name__:
    main()
