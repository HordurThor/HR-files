
class SLL_Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    def resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.arr[i]
        self.arr = new_array

    def append(self, data):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = data
        self.size += 1

    def build_from_SLL(self, head):
        if head == None:
            return
        while head != None:
            if self.size == self.capacity:
                self.resize()
            if head.data != None:
                self.arr[self.size] = head.data
                self.size += 1
            head = head.next


    def reverse_from_SLL(self, head):
        temp_lis = []
        if head == None:
            return
        while head != None:
            temp_lis.append(head.data)
            head = head.next
        for item in temp_lis[::-1]:
            if self.size == self.capacity:
                self.resize()
            self.arr[self.size] = item
            self.size += 1

    def build_reverse_SLL_from_array(self):
        head = None
        for i in range(self.size):           
            head = SLL_Node(self.arr[i], head)
        return head
        

    def clear(self):
        self.size = 0

    def __str__(self):
        ret_str = ""
        for i in range(self.size):
            ret_str += str(self.arr[i]) + " "
        return ret_str

def test_SLL_to_array(test_head):
    test_arr = ArrayList()
    test_arr.build_from_SLL(test_head)
    print("ARRAY:          " + str(test_arr))
    test_arr.reverse_from_SLL(test_head)
    print("REVERSE:        " + str(test_arr))

def head_str(head):
    ret_str = ""
    while head != None:
        ret_str += str(head.data) + " "
        head = head.next
    return ret_str

def head_str_rec(head):
    if head != None:
        return str(head.data) + " " + head_str_rec(head.next)
    return ""

def test_array_to_SLL(test_arr):
    print("REVERSED SLL:   " + head_str_rec(test_arr.build_reverse_SLL_from_array()))

if __name__ == "__main__":
    sll = SLL_Node(4, SLL_Node(1, SLL_Node(3, SLL_Node(5, SLL_Node(2)))))
    print("ORIGINAL SLL:   " + head_str(sll))
    test_SLL_to_array(sll)

    my_arr_lis = ArrayList()
    my_arr_lis.append(7)
    my_arr_lis.append(8)
    my_arr_lis.append(6)
    my_arr_lis.append(9)
    my_arr_lis.append(2)
    print("ORIGINAL ARRAY: " + str(my_arr_lis))
    test_array_to_SLL(my_arr_lis)
