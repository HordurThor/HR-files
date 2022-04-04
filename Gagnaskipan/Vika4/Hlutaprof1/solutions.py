
### ARRAY LIST ###

from operator import is_
from tkinter import N


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




### RECURSION ###

def is_divisible(a, b):
    if b == 0:
        return False
    if b == a or a == 0:
        return True
    elif b < a:
        return is_divisible(a-b, b)
    return False

def count_matches(lis):
    if lis == []:
        return 0
    if len(lis) == 1:
        return 0
    if lis[0] == lis[1]:
        return count_matches(lis[1:])+1
    return count_matches(lis[1:])



### LIBRARY ###

class Book:
    def __init__(self):
        self.isbn = None
        self.name = None

    def get_isbn(self):
        return self.isbn

    def get_name(self):
        return self.name

    def set_isbn(self, ISBN):
        self.isbn = ISBN

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return f"({self.isbn}: {self.name})"

class Library:
    def __init__(self):
        self.books = []

    def __iter__(self):
        for book in self.books:
            yield book

    def add_book(self, ISBN, name):
        new_book = Book()
        new_book.set_isbn(ISBN)
        new_book.set_name(name)
        same_book = self.get_book(ISBN) #Gets a book if it has the same isbn number as the new book
        if same_book != None: #If it found a book then it overwrites the name and returns, else appends the new book
            same_book.set_name(name)
            return
        self.books.append(new_book)

    def get_book(self, ISBN):
        for book in self:
            if book.isbn == ISBN:
                return book
        return None

    def change_book(self, ISBN, name):
        book = self.get_book(ISBN)
        if book != None:
            book.set_name(name)
        
    def remove_book(self, ISBN):
        book = self.get_book(ISBN)
        if book != None:
            self.books.remove(book)

    def __str__(self):
        return_str = ""
        for book in self:
            return_str += str(book)+"\n"
        return return_str


def inst_test(arr_lis, val):
    print("The list {" + str(arr_lis) + "} has " + str(arr_lis.count_instances(val)) + " instances of " + str(val))

def array_tests():
    print()
    print("*********ARRAY_TESTS*********:")
    print("SOME APPENDS, PREPENDS AND INSERTS")
    arr_lis = ArrayList()
    arr_lis.append(6)
    arr_lis.append(7)
    arr_lis.append(8)
    arr_lis.append(9)
    arr_lis.prepend(4)
    arr_lis.prepend(3)
    arr_lis.prepend(2)
    arr_lis.prepend(1)
    arr_lis.insert(5, 4)
    print("THE LIST: " + str(arr_lis))

    print()
    arr_lis = ArrayList()
    inst_test(arr_lis, 4)
    arr_lis.append(4)
    inst_test(arr_lis, 4)
    arr_lis.append(4)
    inst_test(arr_lis, 4)
    arr_lis.append(5)
    inst_test(arr_lis, 4)
    arr_lis.append(4)
    inst_test(arr_lis, 4)
    arr_lis.append(5)
    inst_test(arr_lis, 4)
    arr_lis.append(5)
    inst_test(arr_lis, 4)
    arr_lis.append(4)
    inst_test(arr_lis, 4)

    print()
    print("SOME INSERTS")
    arr_lis = ArrayList()
    arr_lis.insert(8, 0)
    arr_lis.insert(7, 0)
    arr_lis.insert(8, 1)
    arr_lis.insert(9, 3)
    arr_lis.insert(8, 0)
    arr_lis.insert(7, 2)
    arr_lis.insert(8, 3)
    arr_lis.insert(7, 5)
    arr_lis.insert(5, 4)
    print("THE LIST: " + str(arr_lis))

    print()
    inst_test(arr_lis, 4)
    inst_test(arr_lis, 5)
    inst_test(arr_lis, 6)
    inst_test(arr_lis, 7)
    inst_test(arr_lis, 8)
    inst_test(arr_lis, 9)

    print()
    print("SOME INSERTS")
    arr_lis = ArrayList()
    arr_lis.insert(8, -1)
    arr_lis.insert(7, 0)
    arr_lis.insert(6, 2)
    arr_lis.insert(9, 3)
    arr_lis.insert(3, 0)
    arr_lis.insert(4, 2)
    arr_lis.insert(2, 3)
    arr_lis.insert(1, 2)
    arr_lis.insert(5, 5)
    print("THE LIST: " + str(arr_lis))

    print()

def div_test(a, b):
    print("is_divisible(" + str(a) + ", " + str(b) + "): " + str(is_divisible(a, b)))

def match_test(lis):
    print("The list " + str(lis) + " has " + str(count_matches(lis)) + " matches")


def recursion_tests():
    print()
    print("*********RECURSION_TESTS*********:")
    div_test(9, 3)
    div_test(8, 2)
    div_test(8, 4)
    div_test(8, 5)
    div_test(8, 3)
    div_test(15, 7)
    div_test(14, 7)
    div_test(4, 0)
    div_test(0, 4)
    div_test(117, 9)
    print()
    match_test([0,1,2,3,4,5,6,7,8,9])
    match_test([0,1,2,2,4,5,6,6,8,9])
    match_test([0,1,2,3,5,5,5,7,8,9])
    match_test([0,1,2,3,4,5,6,7,9,9])
    match_test([0,1,3,3,3,5,6,7,7,9])
    match_test([1,1,2,2,3,3,4,4,5,5])
    match_test([0,0,0,3,4,5,5,7,8,8])
    match_test([1,1,1,3,3,5,5,5,9,9])
    match_test([])
    match_test([1,1,1,1])
    print()

#IMPORTANT: the order of the books printed does not need to match the expected output
def library_tests():
    print()
    print("*********LIBRARY_TESTS*********:")
    b1 = Book()
    b1.set_isbn("1")
    b1.set_name("Dune")
    print("testing book1:")
    print(b1)

    b2 = Book()
    b2.set_isbn("2")
    b2.set_name("At the mountains of madness")
    print("testing book2:")
    print(b2)
    
    library = Library()
    library.add_book("3", "Don Kikoti")
    print("library with 1 book:")
    print(library)
    
    library.add_book("4", "Sjálfstætt fólk")
    print("library with 2 books:")
    print(library)
    
    book = library.get_book("4")
    print("printing book with id 4")
    print(book)

    library.change_book("3", "Don Quixote")
    print("changing a diffrent book")
    print(library)

    library.add_book("3", "The trial")
    print("overwrite Don Quixote")
    print(library)

    library.remove_book("4")
    print("removed independant people")
    print(library)

if __name__ == "__main__":
    array_tests()
    recursion_tests()
    library_tests()
