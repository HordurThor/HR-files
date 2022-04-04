

##### HASH MAP EXERCISE #####



class HashMap:
    def __init__(self):
        self.array_length = 16
        # MUST USE ONE OF THE FOLLOWING LINES, BUT NOT BOTH
       # self.hash_table = [ [ ] for _ in range(self.array_length) ]
        self.hash_table = [ { } for _ in range(self.array_length) ]
        self.item_count = 0

    def hash_function(self, key):
        return hash(key) % self.array_length

    def __setitem__(self, key, data): # overrides/updates if already there
        j = self.hash_function(key)
        oldsize = len(self.hash_table[j])
        self.hash_table[j][key] = data
        if oldsize < len(self.hash_table[j]):
            self.item_count += 1

    def __getitem__(self, key): # returns data - returns None if nothing there
        j = self.hash_function(key)
        return self.hash_table[j].get(key)

    def __len__(self):
        return self.item_count



##### PREFIX PARSE TREE EXERCISE #####

class PrefixParsingTreeNode:
    def __init__(self, token, left, right):
        self.token = token
        self.left = left
        self.right = right

class PrefixParsingTree:
    def __init__(self):
        self.root = None

    class Tokenizer:
        def __init__(self, str_statement):
            self.statement = str_statement
            self.position = 0

        def get_next_token(self):
            i = self.position
            while i < len(self.statement) and self.statement[i] != " ":
                i += 1
            ret_val = self.statement[self.position:i]
            self.position = i + 1
            return ret_val

    def build_tree_recursive(self, tokenizer):
        token = tokenizer.get_next_token()

        if token == "+" or token == "-":
            return PrefixParsingTreeNode(token, self.build_tree_recursive(tokenizer), self.build_tree_recursive(tokenizer))
        elif token.isdigit():
            return PrefixParsingTreeNode(token, None, None)
        else:
            return PrefixParsingTreeNode(token, None, None)

    def load_statement_string(self, statement):
        tokenizer = self.Tokenizer(statement)
        self.root = self.build_tree_recursive(tokenizer)

    def calculate_value(self):
        # IMPLEMENT THIS OPERATION
        # YOU CAN MAKE HELPER FUNCTIONS IN THE CLASS AS NEEDED
        if self.root == None:
            return None
        return self.calculate_help_recur(self.root)

    def calculate_help_recur(self, tree):
        if tree.token != "-" and tree.token != "+":
            return int(tree.token)
        else:
            op = tree.token
            left_val = self.calculate_help_recur(tree.left)
            right_val = self.calculate_help_recur(tree.right)
            if op == "+": 
                return left_val + right_val
            else:
                return left_val - right_val




##### BST EXERCISE #####

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        ret_str = ""
        if self.left != None:
            ret_str += str(self.left)
        ret_str += str(self.data) + " "
        if self.right != None:
            ret_str += str(self.right)
        return ret_str


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data):
        self.root = self.insert_recur(data, self.root)

    def insert_recur(self, data, node):
        if node == None:
            self.size += 1
            return BSTNode(data)
        elif data < node.data:
            node.left = self.insert_recur(data, node.left)
        elif node.data < data:
            node.right = self.insert_recur(data, node.right)
        else:
            #do nothing if value already exists
            pass
        return node

    # IMPLEMENT THIS OPERATION
    def remove_subtree(self, data):
        if self.root == None:
            return
        if self.root.data == data:
            self.root = None
        self.remove_subtree_recur(self.root, data)

    def remove_subtree_recur(self, tree, data):
        if tree.right.data == data:
            tree.right = None
            return
        elif tree.left.data == data:
            tree.left = None
            return

        if tree.right is not None:
            self.remove_subtree_recur(tree.right, data)
        elif tree.left is not None:
            self.remove_subtree_recur(tree.left, data)
        return


    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.root)




# OPERATION FOR TESTING THE PREFIX PARSING TREE
# DONT CHANGE
def test_prefix_tree(statement_string):
    print("This is the statement: " + statement_string)
    ppt = PrefixParsingTree()
    ppt.load_statement_string(statement_string)
    print("This is the result: " + str(ppt.calculate_value()))

def hash_map_tests():
    print("testing hash map")
    hm = HashMap()
    hm["key_value:345"] = "THIS IS THE DATA FOR KEY: key_value:345"
    hm[345] = "THIS IS THE DATA FOR KEY: 345"
    print(hm[345])
    print(hm[346])
    print(hm["key_value:345"])
    print(len(hm))
    hm[345] = "THIS IS THE NEW DATA FOR KEY: 345"
    print(hm[345])
    print(len(hm))
    print()

def prefix_tests():
    print("testing prefix tree")
    test_prefix_tree("- 12 + 4 5")
    test_prefix_tree("+ 12 + - 21 5 5")
    test_prefix_tree("+ 4 + - 4 6 - 9 8")
    test_prefix_tree("- + - + 6 9 8 + 1 + 5 5 - - + 6 7 - 9 8 - + 9 6 1")
    test_prefix_tree("+ + 8 4 - + - 3 3 2 - + 7 8 9")
    print()


def bst_tests():
    print("testing remove_subtree")
    #example tree
    #           5
    #     3           7
    #  2    4     6       10
    #                  8
    #                    9
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(6)
    bst.insert(10)
    bst.insert(8)
    bst.insert(9)
    print(bst)
    print("bst size: " + str(len(bst)))
    print("remove_subtree 3")
    bst.remove_subtree(3)
    print(bst)
    print("bst size: " + str(len(bst)))

    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(6)
    bst.insert(10)
    bst.insert(8)
    bst.insert(9)
    print(bst)
    print("bst size: " + str(len(bst)))
    print("remove_subtree 6")
    bst.remove_subtree(6)
    print(bst)
    print("bst size: " + str(len(bst)))

    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(6)
    bst.insert(10)
    bst.insert(8)
    bst.insert(9)
    print(bst)
    print("bst size: " + str(len(bst)))
    print("remove_subtree 10")
    bst.remove_subtree(10)
    print(bst)
    print("bst size: " + str(len(bst)))

    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(6)
    bst.insert(10)
    bst.insert(8)
    bst.insert(9)
    print(bst)
    print("bst size: " + str(len(bst)))
    print("remove_subtree 7")
    bst.remove_subtree(7)
    print(bst)
    print("bst size: " + str(len(bst)))
    print()

# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!
    print()

    hash_map_tests()
    prefix_tests()
    bst_tests()