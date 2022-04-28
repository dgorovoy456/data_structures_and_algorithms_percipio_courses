class MyQueue:
    def __init__(self):
        """
        Create a new queue
        """
        self.items = []

    def is_empty(self):
        """
        Returns true if queue is empty
        """
        return len(self.items) == 0

    def enqueue(self, item):
        """
        Add a new element to the end of queue
        """
        self.items.append(item)

    def dequeue(self):
        """Remove element from the beginning of queue """
        return self.items.pop(0)

    def size(self):
        """
        Returns the size of the queue
        """
        return len(self.items)

    def peek(self):
        """
        Have a look at first element of the queue
        """
        if self.is_empty():
            raise Exception('Nothing to peak')
        return self.items[0]


olympics = MyQueue()

olympics.enqueue('United States(USA)')
olympics.enqueue('Great Britain(GBR)')

print(olympics.dequeue())

print(olympics.peek())
print(olympics.peek())

print(olympics.dequeue())

print(olympics.size())
