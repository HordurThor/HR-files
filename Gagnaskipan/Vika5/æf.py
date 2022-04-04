class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(head):
        n = head
        ret_str = ""
        while True:
            if n == None:
                return ret_str
            ret_str += f"{n.data} "
            n = n.next


def print_lis_recur(head):
    if head == None:
        print("")
        return
    print(head.data, end=" ")
    print_lis_recur(head.next)


def add_front(head=None, value=None):
    new_node = Node(value, head)
    return new_node


def add_back(head=None, value=None):
    if head == None:
        new_node = Node(value, head)
        return new_node
    head.next = add_back(head.next, value)
    return head
        

def linear_search(head, value):
    if head == None:
        return False
    if value == head.data:
        return True
    return linear_search(head.next, value)


def sum_list(head):
    if head == None:
        return 0
    return head.data + sum_list(head.next)


def remove_front(head):
    if head == None:
        return
    return head.next


def remove_back(head):
    pass


def remove_all_even(head):
    if head == None:
        return None
    if head.data % 2 == 0:
        return remove_all_even(head.next)
    head.next = remove_all_even(head.next)
    return head


def dublicate_all_divisble_by_value(head, value):
    if head == None:
        return None
    if head.data % value == 0:
        new_node = Node(head.data, None)
        new_node.next = dublicate_all_divisble_by_value(head.next, value)
        head.next = new_node
        return head
    head.next = dublicate_all_divisble_by_value(head.next, value)
    return head



head = None
head = add_front(head, 1)
head = add_front(head, 2)
head = add_front(head, 7)
head = add_front(head, 3)
head = add_front(head, 6)
head = add_front(head, 5)
head = add_back(head, 10)
head = add_back(head, 11)
head = remove_front(head)
print(head)
#print(linear_search(head, 2))
#print(sum_list(head))
#remove_all_even(head)
#head = dublicate_all_divisble_by_value(head, 7)
#print_lis_recur(head)