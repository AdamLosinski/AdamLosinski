class Stack:
    def __init__(self):
        self.__m_buffer = []

    def push(self, element):
        self.__m_buffer.append(element)

    def top(self):
        return self.__m_buffer[-1]

    def pop(self):
        self.__m_buffer.pop()

    def size(self):
        return len(self.__m_buffer)

    def is_empty(self):
        return self.size() == 0
    

class Stack2(Stack):
    def __init__(self):
        super().__init__()
        self.min_value = 0

    def look_for_min(self):
        self.min_value = min(self._Stack__m_buffer)
        print("Minimum value is: ", self.min_value)

    