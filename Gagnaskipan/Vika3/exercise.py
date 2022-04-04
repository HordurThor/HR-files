
def length_of_string(string):
    if string == '':
        return 0
    return length_of_string(string[1:])+1
    

def linear_search(lis, value):
    if lis == []:
        return False
    if lis[0] == value:
        return True
    return linear_search(lis[1:], value)

lis = [1, 2, 3, 3, 4, 3, 5]

def count_instances(lis, value):
    if lis == []:
        return 0
    if lis[0] == value:
        return count_instances(lis[1:], value) +1
    return count_instances(lis[1:], value)+0
    
def dublicate_in_list_bool(lis):
    if lis == []:
        return False
    if linear_search(lis[1:], lis[0]):
        return True
    return dublicate_in_list_bool(lis[1:])

def remove_dublicate(lis):
    if lis == []:
        return []
    if linear_search(lis[1:], lis[0]):
        return [] + remove_dublicate(lis[1:])
    return [lis[0]] + remove_dublicate(lis[1:])

def binary_search(lis, value):
    if lis == []:
        return False
    mid = len(lis) // 2
    if lis[mid] == value:
        return True
    elif value < lis[mid]:
        return binary_search(lis[0:mid], value)
    elif value > lis[mid]:
        return binary_search(lis[mid+1:], value)

print(binary_search(lis, 5))