class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push_front(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        if self.tail == None:
            self.tail = new_node
        self.size += 1
    
    def pop_front(self):
        if self.head == None:
            return None
        ret_val = self.head.data
        self.head = self.head.next
        self.size -= 1
        return ret_val
    
    def push_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def pop_back(self):
        if self.head == None:
            return None
        temp_list = self.head
        ret_val = self.tail.data
        if temp_list != self.tail:
            while temp_list.next != self.tail:
                temp_list = temp_list.next
            temp_list.next = None
            self.tail = temp_list
            self.size -= 1
            return ret_val
        self.head = None
        self.tail = None
        self.size -= 1
        return ret_val

    def get_size(self):
        return self.size

    def __str__(self):
        n = self.head
        ret_str = ""
        while True:
            if n == None:
                return ret_str
            ret_str += f"{n.data} "
            n = n.next


if __name__ == "__main__":
    lis = LinkedList()
    for i in range(6):
        lis.push_front(i)
    print(lis)
    print(lis.pop_front())
    lis.push_back(5)
    print(lis)
    print(lis.pop_back())
    print(lis.pop_back())
    print(lis.pop_back())
    print(lis)
    print(lis.get_size())