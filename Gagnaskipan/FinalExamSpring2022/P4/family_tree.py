

class TreeNode:
    def __init__(self, name, left = None, right = None):
        self.name = name
        self.children = []
        self.left = left
        self.right = right

class FamilyTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def build_tree_from_file(self, file_name):
        file = open(file_name, 'r')
        for name in file:
            name=name.strip()
            if self.root == None:
                self.add_root(name)
            else:
                names = name.split()
                self.add_child(name[0], name[1], self.root)

    def add_child(self, child, parent, node): 
        if parent == node.name:
            node.left = TreeNode(child)
            node.children.append(child)
            self.size += 1
            return
        if node.left != None:
            self.add_child(child, parent, node.left)
        elif node.right != None:
            self.add_child(child, parent, node.right)
        node.right = TreeNode(child)

    def add_root(self, name):
        self.root = TreeNode(name)
        self.size += 1
        

    def print_tree_preorder(self):
        l = self.root
        r = self.root.right
        ret_str = ""
        while l != None:
            ret_str += f"{l.name} "
            l = l.left
        while r != None:
            ret_str += f"{r.name} "
            r = r.right
        print(ret_str)
        


    def print_tree_postorder(self):
        pass


import sys

if __name__ == "__main__":
    tree = FamilyTree()
    tree.build_tree_from_file(sys.path[0] + "/family_file_small.txt")
    tree.print_tree_preorder()
    tree.print_tree_postorder()
    tree = FamilyTree()
    tree.build_tree_from_file(sys.path[0] + "/family_file_big.txt")
    tree.print_tree_preorder()
    tree.print_tree_postorder()