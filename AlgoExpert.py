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
        return closest(bst.left)
    elif t > bst.value:

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