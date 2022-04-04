import re


class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        # TODO: remove 'pass' and implement functionality
        self.capacity = 4
        self.lis = [None] * self.capacity
        self.size = 0
        

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        # TODO: remove 'pass' and implement functionality
        return_str = str(self.lis)
        return return_str

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.resize()
        for i in range(self.size, 0, -1):
            self.lis[i] = self.lis[i-1]
        self.lis[0] = value
        self.size += 1

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        self.resize()
        for i in range(self.size, index, -1):
            self.lis[i] = self.lis[i-1]
        self.lis[index] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.lis[self.size] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index > self.size-1:
            raise IndexOutOfBounds()
        else:
            self.lis[index] = value
            self.size += 1
            

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.lis == [None] * self.capacity:
            raise Empty()
        else:
            return self.lis[0] 

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if index > self.size-1:
            raise IndexOutOfBounds()
        else:
            return self.lis[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.lis == [None] * self.capacity:
            raise Empty()
        else:
            return self.lis[self.size-1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        if self.size == self.capacity:
            self.capacity *= 2
            temp = [None] * self.capacity
            for i in range(0, self.size):
                temp[i] = self.lis[i]
            self.lis = temp

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if index > self.size-1:
            raise IndexOutOfBounds()
        self.resize()
        self.lis[index] = None
        for i in range(self.size, index, -1):
            self.lis[i] = self.lis[i-1]
        self.size -= 1
            

    #Time complexity: O(1) - constant time
    def clear(self):
        temp = [None] * self.capacity
        self.lis = temp
        self.size = 0

    def if_ordered(self, lis):
        for i in range(self.size):
            pass

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    arr_lis.prepend(1)
    arr_lis.prepend(2)
    arr_lis.prepend(3)
    arr_lis.prepend(4)
    arr_lis.remove_at(1)
    #arr_lis.clear()
    print(str(arr_lis))
    #print(val)