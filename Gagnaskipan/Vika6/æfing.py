class Node:

    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DLL_Deque:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def __str__(self):
        n = self.head
        ret_str = ""
        while True:
            if n == None:
                return ret_str
            ret_str += f"{n.data} "
            n = n.next

    def __len__(self):
        return self.size

    def insert_between(self, value, successor, predecessor):
        new_node = Node(value, successor, predecessor)
        predecessor.next = new_node
        successor.prev = new_node
        self.size += 1
        return new_node

    def pop(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        data = node.data
        node.prev = node.next = node.data = None
        return data

    def push_front(self, value):
        self.insert_between(value, self.head, self.head.next)




dll = DLL_Deque()
dll.push_front(1)
dll.push_front(2)
dll.push_front(3)
dll.push_front(4)
print(dll)