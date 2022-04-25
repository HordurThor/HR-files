class DLL_Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.header = DLL_Node("head sentinel node")
        self.tailer = DLL_Node("head sentinel node")
        self.header.next = self.tailer
        self.tailer.prev = self.header
        self.curr = self.tailer
        self.size = 0

    def __str__(self):
        node = self.header.next
        ret_str = ""
        while node != self.tailer:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

    def insert(self, data):
        node = DLL_Node(data, self.curr.prev, self.curr)
        node.prev.next = node
        node.next.prev = node
        self.curr = node
        self.size += 1

    def move_to_next(self):
        if self.curr != self.tailer:
            self.curr = self.curr.next

    def move_to_prev(self):
        if self.curr.prev != self.head:
            self.curr = self.curr.prev

    def remove(self):
        if self.curr != self.tailer:
            self.curr.prev.next = self.curr.next
            self.curr.next.prev = self.curr.prev
            self.size -= 1
            self.curr = self.curr.next

    def shift_around(self, num):
        data_temp =None
        while num > 0:
            self.curr = self.tailer.prev
            data_temp = self.curr.data
            self.remove()
            self.curr = self.header.next
            self.insert(data_temp)
            num -= 1
            

if __name__ == "__main__":
    print("testing shift_back:")
    dll = DLL()
    dll.insert(5)
    dll.insert(4)
    dll.insert(3)
    dll.insert(2)
    dll.insert(1)
    print(dll)
    dll.shift_around(2)
    print(dll)
    dll.shift_around(1)
    print(dll)
    dll.shift_around(2)
    print(dll)
    dll.shift_around(9)
    print(dll)