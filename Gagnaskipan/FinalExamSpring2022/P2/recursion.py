from hashlib import new


class NotDivisibleException(Exception):
    pass

class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        if self.next == None:
            return str(self.data)
        return str(self.data) + " " + str(self.next)

def division(numerator, denominator):
    if numerator < 0:
        raise NotDivisibleException
    elif denominator <= 0:
        raise NotDivisibleException
    elif numerator < denominator:
        raise NotDivisibleException
    return division_helper(numerator, denominator)

def division_helper(numerator, denominator):
    if numerator < denominator:
        return 0
    return 1 + division_helper(numerator-denominator, denominator)

def set_intersection(head1, head2):
    if head1 == None or head2 == None:
        return None
    return set_intersection_helper(head1, head2)


def set_intersection_helper(head1, head2, new_head = None):
    if head2 != None or head2 != None:
        if head1.data == head2.data:
            new_head = SLL_Node(head1.data, new_head)
        if head1.next != None or head2.next != None:
            if head1.next.data == head2.data:
                new_head = SLL_Node(head2.data, new_head)
            elif head1.data == head2.next.data:
                new_head = SLL_Node(head1.next.data, new_head)
        return set_intersection_helper(head1.next, head2.next, new_head)
    return new_head    
    


if __name__ == "__main__":
    print("testing division:")
    try:
        print(division(20,4))
    except NotDivisibleException:
        print("not divisible")
    try:
        print(division(16,2))
    except NotDivisibleException:
        print("not divisible")
    try:
        print(division(1,5))
    except NotDivisibleException:
        print("not divisible")
    try:
        print(division(5,5))
    except NotDivisibleException:
        print("not divisible")
    try:
        print(division(16,6))
    except NotDivisibleException:
        print("not divisible")
    try:
        print(division(5,1))
    except NotDivisibleException:
        print("not divisible")

    print("testing intersection:")
    head1 = SLL_Node(1,SLL_Node(4,SLL_Node(2,SLL_Node(7))))
    head2 = SLL_Node(2,SLL_Node(3,SLL_Node(4,SLL_Node(5))))
    print(head1)
    print(head2)
    print(set_intersection(head1, head2))

    head1 = SLL_Node(1,SLL_Node(3,SLL_Node(7,SLL_Node(9))))
    head2 = SLL_Node(2,SLL_Node(4,SLL_Node(5,SLL_Node(8))))
    print(head1)
    print(head2)
    print(set_intersection(head1, head2))

    head1 = SLL_Node(1,SLL_Node(2,SLL_Node(3,SLL_Node(4))))
    head2 = SLL_Node(1,SLL_Node(2,SLL_Node(3,SLL_Node(4))))
    print(head1)
    print(head2)
    print(set_intersection(head1, head2))
    
