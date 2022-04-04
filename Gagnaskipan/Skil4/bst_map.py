
class BSTNode:
    def __init__(self, key=None, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BSTMap:
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        r = self.root
        ret_str = ""
        while r != None:
            ret_str += "{"+f"{r.key}: {r.data}"+"} "
            if r.left != None:
                rl = r.left
                while rl != None:
                    ret_str += "{"+f"{rl.key}: {rl.data}"+"} "
                    rl = rl.left
            r = r.right
        return ret_str
    
    def __len__(self):
        return self.size

    def insert(self, key, data):
        self.root = self.insert_recur(self.root, key, data)
        self.size += 1

    def insert_recur(self, node, key, data):
        if node == None:
            return BSTNode(key, data)
        elif key < node.key:
            node.left = self.insert_recur(node.left, key, data)
        elif key > node.key:
            node.right = self.insert_recur(node.right, key, data)
#        else:
#            raise ItemExistsExeption()
        return node

    def update(self, key, data):
        self.root = self.update_recur(self.root, key, data)

    def update_recur(self, node, key, data):
        if key < node.key:
            node.left = self.update_recur(node.left, key, data)
        elif key > node.key:
            node.right = self.update_recur(node.right, key, data)
        elif key == node.key:
            node.data = data
        #else:
        #    raise NotFoundException()
        return node
        


tree = BSTMap()
tree.insert(3, "three")
tree.insert(2, "two")
tree.insert(1, "one")
tree.insert(5, "five")
tree.insert(4, "four")

tree.update(4, "five")
print(tree)
print(len(tree))