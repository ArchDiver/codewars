class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, current, value):
        if self.root == None:
            self.root = Node(value)
        else:
            if value < current.value:
                if current.left == None:
                    current.left = Node(value)
                else:
                    self.add(current.left, value)
            else:  
                if current.right == None:
                    current.right = Node(value)
                else:
                    self.add(current.right, value)

    def build_From_list(self, list):
        for i in list:
            self.add(self.root, i)








class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traverse_type):
        if traverse_type == "preorder":
            order = self.preorder_print(tree.root, "")
            return print(f"{traverse_type}: {order}")
        elif traverse_type == "inorder":
            order = self.inorder_print(tree.root, "")
            return print(f"{traverse_type} {order}")
        elif traverse_type == "postorder":
            order = self.postorder_print(tree.root, "")
            return print(f"{traverse_type}r: {order}")
        
        else:
            print(f"The traversal type {traverse_type} is not supported")
            return False

    def preorder_print(self, start, traverse_list):
        """This goes Root->Left->Right"""
        if start:
            traverse_list += (str(start.value) + "->")
            traverse_list = self.preorder_print(start.left, traverse_list)
            traverse_list = self.preorder_print(start.right, traverse_list)

        return traverse_list

    def inorder_print(self, start, traverse_list):
        """This goes Left most Leaf then constantly looks for the furthest left
           Left>Root>Right
        """
        if start:
            traverse_list = self.inorder_print(start.left, traverse_list)
            traverse_list += (str(start.value) + "->")
            traverse_list = self.inorder_print(start.right, traverse_list)
        
        return traverse_list

    def postorder_print(self, start, traverse_list):
        """This goes Left->Right->Root"""
        if start:
            traverse_list = self.postorder_print(start.left, traverse_list)
            traverse_list = self.postorder_print(start.right, traverse_list)
            traverse_list += (str(start.value) + "->")

        return traverse_list




# This builds our tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

tree.print_tree("flarg")
tree.print_tree("preorder")
tree.print_tree("inorder")
tree.print_tree("postorder")