class BinaryNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
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

    def populate_tree(self):
        self.root = self.populate_tree_recur()

    def populate_tree_recur(self):
        data = input("Enter the value of this node: ")
        if data == "":
            return None
        node = BinaryNode(data)
        return node


tree = BinaryTree()

tree.populate_tree()
tree.populate_tree()
tree.populate_tree()
tree.populate_tree()
tree.populate_tree()
print(tree)