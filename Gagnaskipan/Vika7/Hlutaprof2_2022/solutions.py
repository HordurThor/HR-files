
from gettext import find
from tabnanny import check


class SLL_Node:
    # THIS IMPLEMENTATION OF SINGLY-LINKED LIST NODE
    # MUST BE USED UNCHANGED, FOR TESTING PURPOSES
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


class DLL_Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL_Ordered:
    def __init__(self):
        self.header = DLL_Node()
        self.trailer = DLL_Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.current = self.trailer
    

    def __iter__(self):
        walk = self.header.next
        while walk.data != None:
            yield walk
            walk = walk.next
    

    def move_to_value(self, value):
        for x in self:
            if value < x.data:
                self.current = x
                return
        self.current = self.trailer

    def insert_ordered(self, value):
        self.move_to_value(value)
        successor = self.current.prev
        predecessor = self.current
        new_node = DLL_Node(value, successor, predecessor)
        predecessor.prev = new_node
        successor.next = new_node
        self.current = new_node

    
    def get_range(self, min, max):
        # THIS OPERATION SHOULD RETURN A NEW INSTANCE OF DLL_Ordered
        new_dll = DLL_Ordered()
        for x in self:
            if max >= x.data >= min:
                new_dll.insert_ordered(x.data)
        return new_dll


    def __str__(self):
        ret_str = ""
        node = self.header.next
        while node != self.trailer:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str



def is_value_higher_than_average(head, value):
    if head == None:
        return False
    sum_num = find_average_in_sll(head)
    len_num = find_len_of_sll(head)
    avg = sum_num / len_num
    if avg < value:
        return True
    return False

def find_average_in_sll(head):
    if head == None:
        return 0
    return find_average_in_sll(head.next)+head.data

def find_len_of_sll(head):
    if head == None:
        return 0
    return find_len_of_sll(head.next)+1


def is_sublist(head1, head2):
    if head1 == None:
        return True
    if head2 == None:
        return False
    if head1.data == head2.data:
        if check(head1, head2):
            return True
    return is_sublist(head1, head2.next)

def check(head1, head2):
    if head1 == None:
        return True
    if head2 == None:
        return False
    if head1.data == head2.data:
        return True and check(head1.next, head2.next)
    return False

# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    print("\nTesting DLL_ORDERED")
    dl = DLL_Ordered()
    dl.insert_ordered(17)
    dl.insert_ordered(45)
    dl.insert_ordered(12)
    dl.insert_ordered(89)
    dl.insert_ordered(23)
    dl.insert_ordered(56)
    dl.insert_ordered(34)
    dl.insert_ordered(45)
    print("dl: " + str(dl))
    dl.insert_ordered(10)
    dl.insert_ordered(23)
    dl.insert_ordered(22)
    dl.insert_ordered(71)
    dl.insert_ordered(23)
    dl.insert_ordered(45)
    dl.insert_ordered(22)
    dl.insert_ordered(98)
    print("dl: " + str(dl))


    print("\nTesting RANGE")
    def test_range(dl, min, max):
        print("range(" + str(min) + ", " + str(max) + "): " + str(dl.get_range(min, max)))

    test_range(dl, 23, 45)
    test_range(dl, 0, 100)
    test_range(dl, 45, 45)
    test_range(dl, 17, 89)
    test_range(dl, 10, 98)
    test_range(dl, 54, 76)
    test_range(dl, 20, 60)

    print("\nTesting is_value_higher_than_average")
    #5 6 3 7 4
    head = SLL_Node(5, SLL_Node(6, SLL_Node(3, SLL_Node(7, SLL_Node(4, None)))))
    print(is_value_higher_than_average(head, 6))
    print(is_value_higher_than_average(head, 5))
    print(is_value_higher_than_average(head, 4))
    #5 6 3 4 5
    head = SLL_Node(5, SLL_Node(6, SLL_Node(3, SLL_Node(4, SLL_Node(5, None)))))
    print(is_value_higher_than_average(head, 5))
    print(is_value_higher_than_average(head, 6))
    print(is_value_higher_than_average(head, 4))

    print("\nTesting is_sublist")
    head1 = SLL_Node(3, SLL_Node(4, SLL_Node(5, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(is_sublist(head1, head2))
    head1 = SLL_Node(4, SLL_Node(3, SLL_Node(5, None)))
    head2 = SLL_Node(7, SLL_Node(4, SLL_Node(3, SLL_Node(5, SLL_Node(1, SLL_Node(6, None))))))
    print(is_sublist(head1, head2))
    head1 = SLL_Node(5, SLL_Node(2, SLL_Node(3, None)))
    head2 = SLL_Node(5, SLL_Node(2, SLL_Node(3, SLL_Node(1, SLL_Node(7, SLL_Node(6, None))))))
    print(is_sublist(head1, head2))
    head1 = SLL_Node(1, SLL_Node(7, SLL_Node(6, None)))
    head2 = SLL_Node(5, SLL_Node(2, SLL_Node(3, SLL_Node(1, SLL_Node(7, SLL_Node(6, None))))))
    print(is_sublist(head1, head2))

    print()

    head1 = SLL_Node(1, SLL_Node(5, SLL_Node(2, None)))
    head2 = SLL_Node(5, SLL_Node(2, SLL_Node(3, SLL_Node(1, SLL_Node(7, SLL_Node(6, None))))))
    print(is_sublist(head1, head2))
    head1 = SLL_Node(5, SLL_Node(2, SLL_Node(1, None)))
    head2 = SLL_Node(5, SLL_Node(2, SLL_Node(3, SLL_Node(1, SLL_Node(7, SLL_Node(6, None))))))
    print(is_sublist(head1, head2))
    head1 = SLL_Node(4, SLL_Node(7, SLL_Node(6, None)))
    head2 = SLL_Node(5, SLL_Node(2, SLL_Node(3, SLL_Node(1, SLL_Node(7, SLL_Node(6, None))))))
    print(is_sublist(head1, head2))
    head1 = SLL_Node(7, SLL_Node(6, SLL_Node(1, None)))
    head2 = SLL_Node(5, SLL_Node(2, SLL_Node(3, SLL_Node(1, SLL_Node(7, SLL_Node(6, None))))))
    print(is_sublist(head1, head2))

    print()

    head1 = None
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(is_sublist(head1, head2))
    head1 = None
    head2 = None
    print(is_sublist(head1, head2))
    head1 = SLL_Node(5, SLL_Node(6, None))
    head2 = None
    print(is_sublist(head1, head2))