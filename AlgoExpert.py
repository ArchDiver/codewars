# # Two Number Sum---------------------------------------------------------------------------------------------
def twoNumberSum(array, targetSum):
    # Write your code here.
    answer = []
    for i in range(len(array)):
        for j in range((i+1),len(array)):
            if (array[i] + array[j]) == targetSum:
                answer.append(array[i])
                answer.append(array[j])
    return answer

# # Validate Subsequence---------------------------------------------------------------------------------------------
def isValidSequence(a, b):
    # Write your code here. 
    if len(b) > len(a):
        return False
    for i in range(len(a)):
        bVal = b[i]
        if a == []:
            return False
        for j in range(len(a)):
            if b[i] in a:
                bVal = b[i]
                place = a.index(b[i])
                a = a[place+1:]
                break
            else:
                return False
    return True

# # Find Closest Value in BST---------------------------------------------------------------------------------------------
def findClosestValueinBst(tree, target):
    #write code here
    #float('inf') gives an infinite value. This helps to find the lowest value of something.
    close = float('inf')
    return closest(tree, target,close)
def closest(bst, t, c):
    if bst is None:
        return c
    if abs(t-c) > abs(t-bst.value):
        c = bst.value
    if t < bst.value:
        return closest(bst.left, t, c)
    elif t > bst.value:
        return closest(bst.right, t, c)
    else:
        return c
    

# # This is the class of the input tree. Do not edit.
# #Only use if you are bringing in a tree
# class BST:
#     def __int__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# # Branch Sums---------------------------------------------------------------------------------------------
# This is the class input root. Do not edit it.
#Only if you are inporting the tree
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

def branchSums(root):
    #write your code here.
    sumList = []
    bstSums(root, 0, sumList)
    return sumList

def bstSums(node, runSum, sumList):
    if node is None:
        return
    newRunSum = runSum + node.value
    if node.left is None and node.right is None:
        sumList.append(newRunSum)
        return
    bstSums(node.left, newRunSum, sumList)
    bstSums(node.right, newRunSum, sumList)


# # Node Depths---------------------------------------------------------------------------------------------
# Option 1 (recursive=clean) O(n) time | O(h) space
def nodeDepth(root, depth=0):
    # Write your code here.
    if root is None:
        return 0
    return depth + nodeDepth(root.left, depth + 1) + nodeDepth(root.right, depth + 1)


#Option 2 (iterative=same run time just less pretty) O(n) time | O(h) space
def nodeDepths(root):
    depthsSum = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfor["depth"]
        if node is None:
            continue
        depthsSum += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return depthsSum

# # Only use this when bringing in from somewhere
# #This is the class off the input binary tree
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# # Depth-first search---------------------------------------------------------------------------------------------
# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
        pass

# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------
# 
# # # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------
# 
# # # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------


# # ---------------------------------------------------------------------------------------------