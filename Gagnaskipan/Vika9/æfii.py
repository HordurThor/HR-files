from random import Random

def hash(some_value):
    hash = 0
    for character in some_value:
        value = ord(character)
        hash += value - 64
    return hash


lis_size = 8
lis = [0] * lis_size
rand = Random()
rand.seed(1)
for i in range(100):
    string = ""
    for i in range(6):
        string += chr(rand.randint(65,90))
    print(string)
    h = hash(string)
    index = h % lis_size
    lis[index] += 1
print(lis)
diffrence = max(lis) - min(lis)
ratio = diffrence / max(lis)
print(ratio)
print(hash("AB"))
print(hash("BA"))