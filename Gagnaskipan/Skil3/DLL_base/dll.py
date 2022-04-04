
class Node:
    
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DLL:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.tail
        self.size = 0
        self.reversed = False

    def __str__(self):
        ret_str = ''
        for n in self:
            ret_str += f"{n.data} "
        return ret_str


    def __len__(self):
        return self.size


    def __iter__(self):
        if self.reversed:
            walk = self.tail.prev
            while walk.data != None:
                yield walk
                walk = walk.prev
        else:
            walk = self.head.next
            while walk.data != None:
                yield walk
                walk = walk.next


    def insert(self, value):
        if not self.reversed:
            successor = self.curr.prev
            predecessor = self.curr
        else:
            successor = self.curr
            predecessor = self.curr.next
        new_node = Node(value, predecessor, successor)
        predecessor.prev = new_node
        successor.next = new_node
        self.curr = new_node
        self.size += 1


    def remove(self):
        if self.size == 0 or self.curr == self.head or self.curr == self.tail:
            return None
        predecessor = self.curr.prev
        successor = self.curr.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        if not self.reversed:
            self.curr = successor
        else:
            self.curr = predecessor

    def get_value(self):
        return self.curr.data


    def move_to_next(self):
        if not self.reversed:
            if self.curr.next == None:
                return
            self.curr = self.curr.next
        else:
            if self.curr.prev == None:
                return
            self.curr = self.curr.prev


    def move_to_prev(self):
        if not self.reversed:
            if self.curr.prev.data == None:
                return
            self.curr = self.curr.prev
        else:
            if self.curr.next.data == None:
                return
            self.curr = self.curr.next


    def move_to_pos(self, pos):
        if pos > self.size or pos < -1:
            return
        if pos == -1:
            self.curr = self.head
            return
        if pos == self.size:
            self.curr = self.tail
            return
        pos_counter = 0
        for x in self:
            if pos_counter == pos:
                self.curr = x
                return
            pos_counter += 1
                

    def remove_all(self, value):
        current_curr = self.curr
        for x in self:
            if x.data == value:
                self.curr = x
                self.remove()          
        if current_curr.data == value:
            if not self.reversed:
                self.curr = self.head.next
            else:
                self.curr = self.tail.prev
        else:
            self.curr = current_curr


    def reverse(self):
        if self.size == 0:
            return
        self.reversed = not self.reversed
        if self.reversed:
            self.curr = self.tail.prev
        else:
            self.curr = self.head.next


    def sort(self):
        for x in self:
            for y in self:
                if x.data < y.data:
                    x.data, y.data = y.data, x.data


print("\n\nTESTING THE BASIC STUFF\n")

dll = DLL()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("A")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("B")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("C")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("D")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("E")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_next()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_next()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("1")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("2")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_next()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("3")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("4")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_prev()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("VALUE")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_pos(8)
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_pos(2)
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_prev()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_prev()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_prev()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_prev()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_prev()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_prev()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_next()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_next()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_next()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_next()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_pos(-1)
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_pos(18)
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_pos(0)
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))


print("\n\nTESTING MORE COMPLEX STUFF\n")


dll = DLL()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("A")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("B1")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("C")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("A")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("B2")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.reverse()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("C")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("A")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("B3")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("C")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))

dll.remove_all("C")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.sort()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))

dll.remove_all("A")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))

dll.reverse()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))


dll.remove_all("C")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))


dll.move_to_next()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_prev()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_prev()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
