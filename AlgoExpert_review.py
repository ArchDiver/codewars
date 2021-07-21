# #--------------------------------------------------------------------------------
# #  Two Number Sum 
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10

# def twoNumberSum(array, targetSum):
#   nums = sorted(array)
#   high = len(nums)-1
#   low = 0
#   while high > low:
#     out = nums[high] + nums[low]
#     if out == targetSum:
#       return [nums[low], nums[high]]
#     elif out > targetSum:
#       high -=1
#     elif out < targetSum:
#       low +=1
#   return []

# print(twoNumberSum(array, targetSum))

# #--------------------------------------------------------------------------------
# #  Valid Subsequence
# def isValidSubsequence(a, b):
#   if len(b) > len(a):
#     return False
#   a_pos = 0  
#   for i in range(len(b)):
#     if a_pos == len(a)-1:
#       return False
#     else:
#       for j in range(a_pos, len(a)):
#         if a[j] == b[i]:
#           a_pos = j + 1
#           break
#         else:
#           a_pos = j
#   return True        

# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]

# print(isValidSubsequence(array, sequence))

# #--------------------------------------------------------------------------------
# #  Sorted Squared Array
# def sortedSquaredArray(array):
#   sq_array = []
#   for i in array:
#     sq_array.append(i**2)
#   return sorted(sq_array)

# array = [-4, 1, -7, 10, 5]

# print(sortedSquaredArray(array))


def sortedSquaredArray2(array2):
  pos = len(array2) - 1
  sq_array2 = [0] * len(array2)
  left = 0
  right = len(array2) - 1
  while left <= right:
    if abs(array2[left]) >= abs(array2[right]):
      sq_array2[pos] = array2[left]**2
      left += 1
    elif abs(array2[right]) > abs(array2[left]):
      sq_array2[pos] = array2[right]**2
      right -= 1
    elif abs(array2[right]) == abs(array2[left]):
      sq_array2[pos] = array2[right]**2
      right -= 1
      pos -=1
      sq_array2[pos] = array2[left]**2
      left +=1
    pos -= 1
  return sq_array2

array2 = [-7, -5, -4, 3, 6, 8, 9]

print(sortedSquaredArray2(array2))


# #--------------------------------------------------------------------------------
# #  



# #--------------------------------------------------------------------------------
# #  



# #--------------------------------------------------------------------------------
# #  



# #--------------------------------------------------------------------------------
# #  



# #--------------------------------------------------------------------------------
# #  



# #--------------------------------------------------------------------------------
# #  



# #--------------------------------------------------------------------------------
# #  



# #--------------------------------------------------------------------------------
# #  



# #--------------------------------------------------------------------------------
# #  