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

# # Find Closest Value in ---------------------------------------------------------------------------------------------

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