class Stack:

    def __init__(self):
        self.capacity = 4
        self.array = [None] * self.capacity
        self.size = 0

    def __str__(self):
        return f"Stack = {self.array}"

    def resize(self):
        if self.size == self.capacity:
            self.capacity *= 2
            temp = [None] * self.capacity
            for i in range(0, self.size):
                temp[i] = self.array[i]
            self.array = temp

    def pop(self):
        self.array[self.size-1] = None
        self.size -= 1

    def push(self, value):
        self.resize()
        self.array[self.size] = value
        self.size += 1

    
lis = Stack()
lis.push(2)
lis.push(3)
lis.push(4)
lis.push(5)
lis.push(6)
lis.pop()
lis.pop()
print(lis)


class Queue:

    def __init__(self):
        self.capacity = 4
        self.array = [None] * self.capacity
        self.size = 0

    def __str__(self):
        return f"Queue = {self.array}"
        
    def resize(self):
        if self.size == 0:
            self.capacity *= 2
            temp = [None] * self.capacity
            for i in range(0, self.size):
                temp[i] = self.array[i]
            self.array = temp

    def add(self, value):
        self.resize()
        self.array[self.size] = value
        self.size += 1

    def remove(self):
        return_val = self.array[0]
        self.array[0] = None
        for i in range(0, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1
        return return_val


queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
queue.add(5)
val = queue.remove()
val1 = queue.remove()
val2 = queue.remove()
print(queue)
print(val)
print(val1)
print(val2)