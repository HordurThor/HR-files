class ArrayList:
    def __init__(self, capacity = 4):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        str_val = ""
        for i in range(self.size - 1):
            str_val += str(self.arr[i]) + ", "
        if self.size > 0:
            str_val += str(self.arr[self.size - 1])
        return str_val

    def resize(self):
        if self.size == self.capacity:
            self.capacity *= 2
            temp = [0] * self.capacity
            for i in range(0, self.size):
                temp[i] = self.arr[i]
            self.arr = temp

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.insert(value, 0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if index >= 0 and index <= self.size:
            self.resize()
            for i in range(self.size, index, -1):
                self.arr[i] = self.arr[i-1]
            self.arr[index] = value
            self.size += 1

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.insert(value, self.size)

    def count_instances(self, value):
        count = 0
        for i in range(self.size):
            if self.arr[i] == value:
                count += 1
        return count