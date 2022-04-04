from SLL import ArrayList

class Item:
    __slots__ ='key', 'value'

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.key < other.key

class MapADT:

    def __init__(self):
        self.table = ArrayList()
    
    def __str__(self):
        ret_str = ''
        for item in self.table.arr:
            if item == 0:
                return ret_str
            ret_str += "{"+f"{item.key}: {item.value}"+"} "
        return ret_str

    def __iter__(self):
        for item in self.table:
            yield item.key

    def insert(self, key, value):
        new_item = Item(key, value)
        for i in range(self.table.size):
            if self.table.arr[i].key == key:
                raise KeyError('Key already exists')
            if self.table.arr[i].key > key:
                self.table.insert(new_item, i)
                return
        self.table.insert(new_item, self.table.size)

    def find(self, key):
        for item in self.table.arr:
            if key == item.key:
                return item.value
        raise KeyError('Key Error: ' + repr(key))

    def update(self, key, value):
        for item in self.table.arr:
            if key == item.key:
                item.value = value
                return
        raise KeyError('Key Error' + repr(key))

    def remove(self, key):
        for j in range(len(self.table.arr)):
            if key == self.table.arr[j].key:
                self.table.arr.pop(j)
                return
        raise KeyError('Key Error' + repr(key))
    
    def __len__(self):
        return len(self.table)
    

adt = MapADT()
adt.insert(1, 'One')
adt.insert(3, 'Three')
adt.insert(2, 'Two')
adt.insert(4, 'Four')
adt.insert(5, 'Five')
adt.insert(6, 'Six')
adt.remove(4)
adt.update(1, 'Uno')
print(adt.find(3))
print(adt)