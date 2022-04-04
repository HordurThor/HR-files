from platform import node


class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __iter__(self):
        node = self.head
        while node != None:
            yield node
            node = node.next
    
    def remove(self, prev, node):
        if self.head == None:
            return
        if self.head == node:
            self.head = self.head.next
        else:
            prev.next = node.next
        self.size -= 1
        return
    
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def __str__(self):
        ret_str = ""
        for node in self:
            ret_str += f"{node.data} "
        return ret_str

