
class TreeNode:
    def __init__(self, name = ""):
        self.name = name
        self.parent = None
        self.children = []

class Tree:
    def __init__(self, root=None):
        self.root = root
        self.curr = self.root

'''
Note that all the "if False" and "if True" are simply there to
give you the correct success and error message formats.
You can use if sentences or try catch or any other
means of programming you control flow.
You can make an encapsulting class for everything and start with that,
rather than starting with the single TreeNode("root").
Just make sure the input and output of the program is exactly as
specified and fits with the  expected_out.txt when the tester
program is run with the original commands.txt.
Then feel free to make your own, more extensive tests.
'''

def run_commands_on_tree(tree):
    print("  current directory: " + tree.curr.name)
    while True:
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            print("  Making subdirectory " + command[1])
            succ = add_directory(tree, command[1])
            if not succ:
                print("  Subdirectory with same name already in directory")

        elif command[0] == "ls":
            print("  Listing the contents of current directory,  " + str(tree.curr.name)) # Add the name of the directory here
            list_children(tree)

        elif command[0] == "cd":
            print("  switching to directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            succ = change_dir(tree, command[1])
            if command[1] == "..":
                if not succ:
                    print("Exiting directory program")
                    break 
            else:
                if not succ:
                    print("  No folder with that name exists")
            print("  current directory: " + str(tree.curr.name)) # Add the name of the current directory here

        elif command[0] == "rm":
            print("  removing directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            succ = remove_dir(tree, command[1])
            if succ:
                print("  directory successfully removed!")
            else:
                print("  No folder with that name exists")
        else:
            print("  command not recognized")

def add_directory(tree, name):
    for child in tree.curr.children:
        if child.name == name:
            return 0
    new_node = TreeNode(name)
    new_node.parent = tree.curr
    if tree.curr.children == []:
        tree.curr.children.append(new_node)
        return 1
    for i, child in enumerate(tree.curr.children):
        if child.name > name:
            tree.curr.children.insert(i, new_node)
            return 1
    tree.curr.children.append(new_node)
    return 1

def change_dir(tree, name):
    if name == "..":
        if tree.curr == tree.root:
            return 0
        tree.curr=tree.curr.parent
        return 1
    for child in tree.curr.children:
        if child.name == name:
            tree.curr = child
            return 1
    return 0

def list_children(tree):
    for child in tree.curr.children:
        print(child.name)

def remove_dir(tree, name):
    for child in tree.curr.children:
        if child.name == name:
            tree.curr.children.remove(child)
            return 1

def run_directories_program():
    # YOU CAN CHANGE THE WHOLE THING IF YOU LIKE!!
    # YOU CAN DESIGN THIS DIFFERENTLY IF IT SUITS YOU
    directories = Tree(TreeNode("root"))
    run_commands_on_tree(directories)

if __name__ == "__main__":
    run_directories_program()
    
