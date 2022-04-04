from SLL import LinkedList

class MapBase:
    class _Item:
        __slots__ ='key', 'value'

        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __eq__(self, other):
            return self.key == other.key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self.key < other.key

        def __gt__(self, other):
            return self.key > other.key


class Bucket(MapBase):

    def __init__(self):
        self._table = LinkedList()


    def __str__(self):
        ret_str = ''
        for node in self._table:
            ret_str += "{"+f"{node.data.key}: {node.data.value}""} "
        return ret_str

    def __iter__(self):
        for node in self._table:
            yield node.data.key, node.data.value

    def __len__(self):
        return self._table.size


    def __setitem__(self, key, value):
        for node in self._table:
            if node.data.key == key:
                node.data.value = value
                return
        self._table.append(self._Item(key, value))


    def __getitem__(self, key):
        for node in self._table:
            if node.data.key == key:
                return node.data.value
        raise NotFoundException()


    def insert(self, key, value):
        for node in self._table:
            if node.data.key == key:
                raise ItemExistsException()
        new_item = self._Item(key, value)
        self._table.append(new_item)


    def remove(self, key):
        prev = None
        for node in self._table:
            if node.data.key == key:
                self._table.remove(prev, node)
                return
            prev = node
        raise NotFoundException()


    def update(self, key, value):
        for node in self._table:
            if node.data.key == key:
                node.data.value = value
                return
        raise NotFoundException()
    

    def find(self, key):
        for node in self._table:
            if node.data.key == key:
                return node.data.value
        raise NotFoundException()


    def contains(self, key):
        for node in self._table:
            if node.data.key == key:
                return True
        return False


class NotFoundException(Exception):
    
    def __init__(self):
        self.message = f"Key not found"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ItemExistsException(Exception):
    
    def __init__(self):
        self.message = f"Key already exists"
        super().__init__(self.message)

    def __str__(self):
        return self.message

