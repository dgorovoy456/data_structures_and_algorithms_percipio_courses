class MyStack:
    def __init__(self):
        """
        Create a new stack
        """
        self.stack = []

    def push(self, data):
        """
        Add a element to the stack
        """
        self.stack.append(data)

    def pop(self):
        """
        Remove the top element from the stack
        """
        if self.is_empty():
            raise Exception('Nothing to peek')
        return self.stack.pop(len(self.stack) - 1)

    def peek(self):
        """
        Have a look at top element of the stack
        """
        if self.is_empty():
            raise Exception('Nothing to peek')

        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        """
        Returns true if stack is empty
        """
        return len(self.stack) == 0

    def size(self):
        """
        Returns size of the stack
        """
        return len(self.stack)


olympics = MyStack()

olympics.push('United States(USA)')
olympics.push('Great Britain(GBR)')
olympics.push('China(CHN)')
olympics.push('Ukraine(UA)')
olympics.push('Poland(PL)')

print(olympics.size())
print(olympics.is_empty())
print(olympics.peek())

while not olympics.is_empty():
    print(olympics.pop())
