
class MyHashableKey:

    def __init__(self, int_value=None, string_value=None):
        self.int_value = int_value
        self.string_value = string_value

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        hash_val = 0
        if self.int_value is not None:
            hash_val = (((self.int_value + 254) - 50) * 20) / 2
        
        if self.string_value is not None:
            for char in self.string_value:
                hash_val += (((ord(char) + 254) - 50) * 20) / 2
        return int(hash_val)