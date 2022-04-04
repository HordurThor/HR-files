class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BSTSet:
    def __init__(self):
        self.root = None

    def __str__(self):
        l = self.root
        r = self.root.right
        ret_str = ""
        while l != None:
            ret_str += f"{l.data} "
            l = l.left
        while r != None:
            ret_str += f"{r.data} "
            r = r.right
        return ret_str
            
    def add(self, value):
        self.root = self.add_recur(self.root, value)

    def add_recur(self, node, value):
        if node == None:
            return BSTNode(value)
        elif value < node.data:
            node.left = self.add_recur(node.left, value)
        elif value > node.data:
            node.right = self.add_recur(node.right, value)
        else:
            print("value already exist in the tree")
        return node

    def remove(self, value):
        pass


tree = BSTSet()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)
print(tree)