from multiprocessing.sharedctypes import Array
import my_timer

def main(prog):
    t = my_timer.Timer()
    t.start()

    print(prog)

    t.stop()

# #-------------------------------------------------------------------------------
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

# #-------------------------------------------------------------------------------
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

# #-------------------------------------------------------------------------------
# #  Sorted Squared Array
# def sortedSquaredArray(array):
#   sq_array = []
#   for i in array:
#     sq_array.append(i**2)
#   return sorted(sq_array)

# array = [-4, 1, -7, 10, 5]

# print(sortedSquaredArray(array))


# def sortedSquaredArray2(array2):
#   pos = len(array2) - 1
#   sq_array2 = [0] * len(array2)
#   left = 0
#   right = len(array2) - 1
#   while left <= right:
#     if abs(array2[left]) >= abs(array2[right]):
#       sq_array2[pos] = array2[left]**2
#       left += 1
#     elif abs(array2[right]) > abs(array2[left]):
#       sq_array2[pos] = array2[right]**2
#       right -= 1
#     elif abs(array2[right]) == abs(array2[left]):
#       sq_array2[pos] = array2[right]**2
#       right -= 1
#       pos -=1
#       sq_array2[pos] = array2[left]**2
#       left +=1
#     pos -= 1
#   return sq_array2

# array2 = [-7, -5, -4, 3, 6, 8, 9]

# print(sortedSquaredArray2(array2))


# #-------------------------------------------------------------------------------
# # # #  Tournament Winner

# competitors = [
#     ["HTML", "C#"],
#     ["C#", "Python"],
#     ["Python", "HTML"],
# ]
# results = [0, 0, 1]

# def tournamentWinner1(competitions, results):
#     win = 3
#     final_winner = "fail"
#     competitors_list = {}
    
#     for i in range(len(competitions)):
#         # print(competitions[i][0], competitions[i][1])
        
#         if competitions[i][0] not in competitors_list:
#             competitors_list[competitions[i][0]] = 0
#         if competitions[i][1] not in competitors_list:
#             competitors_list[competitions[i][1]] = 0
            
#         # print(results[i])    
#         if results[i] == 1:
#             competitors_list[competitions[i][0]] = competitors_list[competitions[i][0]] + win
#             # print(competitors_list[competitions[i][0]])

#         else:
#             competitors_list[competitions[i][1]] = competitors_list[competitions[i][1]] + win
#             # print(competitors_list[competitions[i][1]])
#         # print(competitors_list)
    
#     # print(competitors_list)
#     final = sorted(competitors_list.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
#     # print(final)
#     final_winner = final[0]


#     # Write your code here.
#     return f"{final_winner}"


# # print(tournamentWinner1(competitors, results))

# #___Clean
# def tournamentWinner2(competitions, results):
#     win = 3
#     competitors_list = {}
    
#     for i in range(len(competitions)):
#         # This check to make sure the lang is in the dict
#         if competitions[i][0] not in competitors_list:
#             competitors_list[competitions[i][0]] = 0
#         if competitions[i][1] not in competitors_list:
#             competitors_list[competitions[i][1]] = 0

#         #This updates the winners scores    
#         if results[i] == 1:
#             competitors_list[competitions[i][0]] = competitors_list[competitions[i][0]] + win
#         else:
#             competitors_list[competitions[i][1]] = competitors_list[competitions[i][1]] + win

#     # Write your code here.
#     return (sorted(competitors_list.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))[0][0]


# # tournamentWinner2(competitors, results)

# #__Better 
# def tournamentWinner3(competitions, results):
#     # Ties only return the first winner.
#     winner = ''
#     rank = {winner: 0}
#     for teams, result in zip(competitions, results):
#         team = teams[0]  if result == 1 else teams[1]
#         if team not in rank:
#             rank[team] = 0
#         rank[team] += 3
#         if rank[team] > rank[winner]:
#             winner = team
#     return winner

# my_timer.timed(tournamentWinner1(competitors, results))
# my_timer.timed(tournamentWinner2(competitors, results))
# my_timer.timed(tournamentWinner3(competitors, results))

# #-------------------------------------------------------------------------------
# #  Non-Constructrable Change
# coins0 = []
# coins1 = [5, 7, 1, 1, 2, 3, 22]
# coins2 = [1, 2, 3, 4]


# #____Not working due to randoms
# def nonConstructibleChange(coins):
#     # Write your code here.
#     if not coins or min(coins) > 1:
#         return 1
    
#     highest = sum(coins)
#     s_coins = sorted(coins)
#     last_j = 0
#     for i in range(1, highest):
#         if i not in coins:
#             running = s_coins[last_j]

#             for j in range(len(s_coins)):
#                 if running > i:
#                     return i                    
#                 running = running + s_coins[j]
#                 if running == i:
#                     break
#         if i in s_coins:
#             last_j = s_coins.index(i)
#     highest += 1
#     return highest



# #___Try 2__nope
# def nonConstructibleChange(coins):
#     # Write your code here.
#     if not coins or min(coins) > 1:
#         return 1
    
#     highest = sum(coins)
#     s_coins = sorted(coins)
#     last_j = 0
#     for i in range(1, highest):
#         if i not in coins:
#             running = s_coins[last_j]
#             for j in range(len(s_coins)):
#                 if running > i:
#                     return i                    
#                 running = running + s_coins[j]
#                 if running == i:
#                     break
#         if i in s_coins:
#             last_j = s_coins.index(i)
#     highest += 1
#     return highest
    
#__Try 3
# def nonConstructibleChange(coins):
#     coins.sort()
#     total = 0
#     for coin in coins:
#         if coin > total + 1:
#             return total + 1
        
#         total += coin
    
#     return total + 1

# my_timer.run_time(print(nonConstructibleChange))


# # #-------------------------------------------------------------------------------
# # #  Find the closest Value in a BST
# # # Try 1
# def findClosestValueInBst(tree, target):
#     return tree_helper(tree, target, tree.value)
    

# def tree_helper(tree, target, closest):
#     current_Node = tree
#     while current_Node is not None:
#         if abs(target - closest) > abs(target - current_Node.value):
#             closest = current_Node.value
            
#         if target < current_Node.value:
#             current_Node = current_Node.left
#         elif target > current_Node.value:
#             current_Node = current_Node.right

#         else:
#             break
#     return closest
        
            

# # This is the class of the input tree. Do not edit.
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None




# # #-------------------------------------------------------------------------------
# # #  Branch Sums
# # This is the class of the input root. Do not edit it.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# def branchSums(root):
#     sums = []
#     branchSums_Helper(root, sums, 0)

#     return sums


# def branchSums_Helper(current_Node, sums, current_sum):
#     if current_Node is None:
#         return
#     new_Sum = current_sum + current_Node.value
#     if current_Node.left is None and current_Node.right is None:
#         sums.append(new_Sum)
#         return
    
#     branchSums_Helper(current_Node.left, sums, new_Sum)
#     branchSums_Helper(current_Node.right, sums, new_Sum)    


#     return sums



# # #-------------------------------------------------------------------------------
# #  Node Depths
# First try - Does not work returns only Zero
# def nodeDepths(root):
#     total = 0
#     nodeDepths_Helper(root, total, depth=0)
#     return total

# def nodeDepths_Helper(node, total, depth):
#     depth += 1
#     if node.left is None and node.right is None:
#         total += depth
#         return total
#     nodeDepths_Helper(node.left, total, depth)
#     nodeDepths_Helper(node.right, total, depth)


# # This is the class of the input binary tree.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# # Their answer
# def nodeDepth(root):
#     sumDepths = 0
#     stack = [{"node": root, "depth":0}]
#     while len(stack) > 0:
#         nodeInfo = stack.pop()
#         node, depth = nodeInfo["node"], nodeInfo["depth"]
#         if node is None:
#             continue
#         sumDepths += depth
#         stack.append({"node":node.left, "depth": depth +1})
#         stack.append({"node":node.right, "depth": depth + 1})
#     return depth



# # #-------------------------------------------------------------------------------
# # #  Depth first Search
# # Do not edit the class below except
# # for the depthFirstSearch method.
# # Feel free to add new properties
# # and methods to the class.
# class Node:
#     def __init__(self, name):
#         self.children = []
#         self.name = name

#     def addChild(self, name):
#         self.children.append(Node(name))
#         return self

#     def depthFirstSearch(self, array):
#         # Write your code here.
#         array.append(self.name)
#         for child in self.children:
#             child.depthFirstSearch(array)
#         return array

# # #-------------------------------------------------------------------------------
# #  Min wait time
# queries = [3, 2, 1, 2, 6]
# queries2 = [3, 2, 1, 2, 6]

# def minimumWaitingTime1(queries):
#     sortQ = sorted(queries)
#     total = 0
#     numRuns = len(sortQ) 
#     for wait in sortQ:
#         numRuns -= 1
#         total += wait * numRuns
#     return total

# def minimumWaitingTime2(queries):
#     queries.sort()
#     total, prev = 0, 0
#     for time in queries:
#         total += prev
#         prev += time
#     return total



# my_timer.timed(print(minimumWaitingTime1(queries)))
# my_timer.timed(print(minimumWaitingTime2(queries2)))

# #-------------------------------------------------------------------------------
# # #  Class Photo
#   redShirtHeights = [5, 8, 1, 3, 4],
#   blueShirtHeights =  [6, 9, 2, 4, 5]

#   def classPhotos(redShirtHeights, blueShirtHeights):
#     # Write your code here.
#     front = sorted(redShirtHeights, reverse = True)
#     back = sorted(blueShirtHeights, reverse = True)
#     if front[0] > back[0]:
#         front, back = back, front
    
#     for i in range(len(front)):
#         if front[i] >= back[i]:
#             return False

#     return True

# #-------------------------------------------------------------------------------
# #  Tandem Bike


# redShirtSpeeds =[5, 5, 3, 9, 2],
# blueShirtSpeeds = [3, 6, 7, 2, 1],
# fastest = "true"


# def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
#     # Write your code here.
#     speeds = 0
#     redShirtSpeeds.sort()
#     # if fastest == False:
#     #     blueShirtSpeeds.sort(reverse = True)
#     # else:
#     #     blueShirtSpeeds.sort()
#     blueShirtSpeeds.sort(reverse=fastest)
#     # for i in range(len(redShirtSpeeds)):
#     #     speeds += max(redShirtSpeeds[i], blueShirtSpeeds[i])

#     # return speeds
#     return sum([max(redShirtSpeeds[i], blueShirtSpeeds[i]) for i in range(len(redShirtSpeeds))])

# print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))


# #-------------------------------------------------------------------------------
# # 

# # Remove Duplicates From Linked List

# # This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# def removeDuplicatesFromLinkedList(linkedList):
#     currentNode = linkedList
#     # Write your code here.
#     while currentNode is not None:
#         nextNode = currentNode.next
#         while nextNode and nextNode.value == currentNode.value:
#             nextNode = nextNode.next
#         currentNode.next = nextNode
#         currentNode = nextNode
        
#     return linkedList


# #-------------------------------------------------------------------------------
# #  Nth Fibonacci
# Mine
# def getNthFib1(n):
#     fib = [0, 1]
#     count = 3
#     while count <= n:
#         nextFib = fib[0] + fib[1]
#         fib[0], fib[1] = fib[1], nextFib
#         count +=1
#     # if n > 1:
#     #     return fib[1]
#     # else:
#     #     return fib[0]
#     return fib[1] if n > 1 else fib[0]
    


# # algo recursive
# def getNthFib2(n):
#     if n == 2:
#         return 1
#     elif n == 1:
#         return 0
#     return getNthFib(n - 1) + getNthFib(n - 2)


# # best 
# def getNthFib(n):
#     # Write your code here.
#     a, b = 0, 1
#     for i in range(n-1):
#         a, b = b, a+b
#     return a


# #-------------------------------------------------------------------------------
# # Product Sum
# array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

# # Tip: You can use the type(element) function to check whether an item
# # is a list or an integer.
# def productSum(array, depth=1):
#     # Write your code here.
#     sum = 0
#     for i in array:
#         print(type(i))
#         if type(i) == list:
#             i = productSum(i, depth + 1)
#         sum += i

#     return sum * depth

# print(productSum(array))

# #-------------------------------------------------------------------------------

# # #  Binary Seach
# array = [1, 5, 23, 111]
# target = 5

# def binarySearch(array, target):
#     half = int(len(array)/2)
#     a = array[0]
#     b = array[half]
#     c = array[-1]
    
#     if target == array[half]:
#         if half == 0:
#             return 1
#         return half
#     elif target > array[half]:
#         subarray = array[half:]
#         return half + binarySearch(subarray, target)
#     elif target < array[half]:
#         subarray = array[:half]
#         return binarySearch(subarray, target)
#     else:
#         return -1

# print(binarySearch(array, target))


# #-------------------------------------------------------------------------------
# # Skilled Coding interview with Kevin
# [2, 4, -4, 0, -1, 5]

# Get all the three number tuples in the list with sum = 0

# [4, -4, 0]
# [-4, -1, 5]
# """

# numList = [-4, -4, -4, -1, 0, 2, 4, 5]

# a = [0]
# b = [-1]

# need = -(pointA + pointB )
# if need in ARRAY[PointA + 1:PointB]:
#      output.append[need]

# dedupated(output)


# NOT FINISHED


# def findThreeNumsSumN(lookList, target=0):
#     output = []
#     l, r = 0, len(lookList) -1
#     # max, min = sum(lookList[r], lookList[r - 1], lookList[r - 2]), sum(lookList[l], lookList[l + 1], lookList[l + 2])
#     # if target > max or target < min:
#     #     return "The target is out of range"
#     while l < r:
#         a, b = lookList[l], lookList[r]
#         have = a + b
#         need = target - (lookList[l], lookList[r])
#         # need = target - (lookList[l] + lookList[r])        
#         if need in lookList:
#             output = addOutput(lookList[l+1:r], output, l, r, need)
#         if 
            

#     return output

# def addOutput(look, out, l, r, need):
#     while need in look:
#         out.append((l, need, r))
#         look.remove(need)

#     return out

# Will work
# def threeNumberSum(array, targetSum):
#     array.sort()
#     output = []
#     for i in range(len(array) - 2):
#         l, r = i + 1, len(array) - 1
#         while l < r:
#             iSum = array[i] + array[l] + array[r]
#             if  iSum == targetSum:
#                 if [array[i], array[l], array[r]] not in output:
#                     output.append([array[i], array[l], array[r]])
#                 l += 1
#                 r -= 1
#             elif iSum < targetSum:
#                 l += 1
#             elif iSum > targetSum:
#                 r -= 1

#     return output
            

# numList = [-4, -4, -4, -1, 0, 2, 4, 5]
# threeNumberSum(numList, 0)

# #-------------------------------------------------------------------------------
# # #  Find Three largest numbers
# array = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]

# def findThreeLargestNumbers(array):
#     ans = [None,None,None]
#     # a, b , c = None, None, None
#     for i in array:
#         if ans[2] is None or i > ans[2]:
#             ans[0], ans[1], ans[2] = ans[1], ans[2], i
#         elif ans[1] is None or i >ans[1]:
#             ans[0], ans[1] = ans[1], i
#         elif ans[0] is None or i >ans[0]:
#             ans[0] = i
#     return ans

# print(findThreeLargestNumbers(array))


# #-------------------------------------------------------------------------------
# # # bubble sort

# array = [8, 5, 2, 9, 5, 6, 3]
# # # Mine
# def bubbleSort(array):
#     b_sorted = False
#     runs = 1
#     while b_sorted == False:
#         b_sorted = True
#         for i in range(len(array) - runs):
#             if array[i] > array[i + 1]:
#                 array[i], array[i + 1] = array[i + 1], array[i]
#                 b_sorted = False
#             else:
#                 continue
#         runs += 1

#     return array

# bubbleSort(array)

# #-------------------------------------------------------------------------------

# # #  insertion sort
# array = [8, 5, 2, 9, 5, 6, 3]

# def insertionSort(array):
#     for i in range(1, len(array)):
#         while array[i] < array[i - 1] and i != 0:
#             array[i], array[i - 1] = array[i - 1], array[i]
#             i -= 1
#     return array

# insertionSort(array)


# #-------------------------------------------------------------------------------
# # # Selection Sort
# array = [8, 5, 2, 9, 5, 6, 3]


# def selectionSort(array):
#     for i in range(len(array) - 1):
#         for j in range(i + 1, len(array)):
#             if array[j] < array[i]:
#                 array[i], array[j] = array[j], array[i]
#     return array

# selectionSort(array)
# #-------------------------------------------------------------------------------
# #  Palindrome Check
# string = "abcdcba"

# def isPalindrome(string):
#     l, r = 0, len(string)
#     while l < r:
#         if string[l] != string[r]:
#             return False
#     return True

# isPalindrome(string)

# #-------------------------------------------------------------------------------
# # # Ceasar Cipher Encryptor
# key = 25
# string = "iwufqnkqkqoolxzzlzihqfm"


# def caesarCipherEncryptor(string, key):
#     alph ="abcdefghijklmnopqrstuvwxyz"
#     newString = ""
#     for letter in string:
#         newString += (alph[(alph.find(letter) + key) % 26])
        
#     return newString


# caesarCipherEncryptor(string, key)




# #-------------------------------------------------------------------------------

# # #  run-length encoding
# def runLengthEncoding(string):
#     count, code = 1, ''
    
#     for i in range(1, len(string)):
#         last, current = string[i - 1], string[i]
#         if current != last or count == 9:
#             code += str(count) + last
#             count = 0
#         count += 1
#     code += str(count) + string[-1]

#     return code


# code = "AAAAAAAAAAABBCCCCDD"
# runLengthEncoding(code)
# ans = "9A2A2B4C2D"
        

# #-------------------------------------------------------------------------------
# # # Generate Document
# def generateDocument(characters, document):
#     usedChar = []
#     # characters, document = characters.lower(), document.lower()
#     for char in document:
#         if char in usedChar:
#             continue
#         else:
#             if document.count(char) > characters.count(char):
#                 return False
#             else:
#                 usedChar.append(char)    
    
#     return True


# characters = "Bste!hetsi ogEAxpelrt x "
# document =  "AlgoyExpert is the Best!"
# generateDocument(characters, document)

# #-------------------------------------------------------------------------------
# # #  First non-repeating character
# def firstNonRepeatingCharacter(string):
#     for char in string:
#         if string.count(char) == 1:
#             return string.index(char)
#     return -1

# goingIn = "faadabcbbebdf"
# firstNonRepeatingCharacter(goingIn)

# #-------------------------------------------------------------------------------
# # Three Number sum
# def threeNumberSum(array, targetSum):
#     answerList = list()
#     array.sort()
#     for i in range(len(array) - 2):
#         l, r = i + 1, len(array) - 1
#         while l < r:
#             nowSum = array[i] + array[l] + array[r]
#             if nowSum == targetSum and [array[i], array[l], array[r]] not in answerList:
#                 answerList.append([array[i], array[l], array[r]])
#                 l += 1
#                 r -= 1
#             elif nowSum < targetSum:
#                 l += 1
#             elif nowSum > targetSum:
#                 r -=1
    
#     return answerList

# x = [12, 3, 1, 2, -6, 5, -8, 6]
# target = 0
# threeNumberSum(x, target)


# #-------------------------------------------------------------------------------

# #  Smallest difference
# def smallestDifference(arrayOne, arrayTwo):
#     arrayOne.sort()
#     arrayTwo.sort()
#     longest = arrayOne if len(arrayOne) > len(arrayTwo) else arrayTwo
#     shortest = arrayTwo if longest == arrayOne else arrayOne
#     smallest, ansNums = (abs(shortest[0] - shortest[0])), list(shortest[0], shortest[0])
#     for i in range(1, len(longest)-1):
#         if i in shortest:
#             return [i, i]
#         else:
#             for j in range(len())

# # Broken
# def smallestDifference(arrayOne, arrayTwo):
#     arrayOne.sort()
#     arrayTwo.sort()
#     smallest, smallPair = (abs(arrayOne[0] - arrayTwo[0])), [arrayOne[0], arrayTwo[0]]
#     for i in range(len(arrayOne)):
#         curr_i_Num = arrayOne[i]
#         for j in range(len(arrayTwo)):
#             curr_j, next_j = arrayTwo[j], arrayTwo[j + 1]
#             next_sum = abs(curr_i_Num - next_j)
            
#             curr_Sum = abs(arrayOne[i] - arrayTwo[j])
#             if curr_Sum < smallest:
#                 smallPair = [arrayOne[i] , arrayTwo[j]]
#                 smallest = curr_Sum
#                 break
#             elif curr_Sum < abs(arrayOne[i] - arrayTwo[j + 1]):
#                 break

#     return smallPair

# def smallestDifference(arrayOne, arrayTwo):
#     arrayOne.sort()
#     arrayTwo.sort()
#     small, smallPair, idx1, idx2 = float('inf'), [], 0, 0
#     while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
#         curr_Sum = abs(arrayOne[idx1] - arrayTwo[idx2])
#         if abs(arrayOne[idx1] - arrayTwo[idx2]) < small:
#             small = abs(arrayOne[idx1] - arrayTwo[idx2])
#             smallPair = [arrayOne[idx1], arrayTwo[idx2]]
#         if arrayOne[idx1] > arrayTwo[idx2]:
#             idx2 +=1
#         else:
#             idx += 1

#     return smallPair


# a = [10, 0, 20, 25, 2000]
# b = [26, 134, 135, 15, 17]

# print(smallestDifference(a,b))

        
# #-------------------------------------------------------------------------------
# # Skilled July 29, 2022
# Word finding: Given a word w and some text t, write a function that finds whether w is in t. For example: w="nest", t=" Ibuiltanestandtestedit. "


# t = 20
# m = 17

# len(t) = n
# len(w) = m

# time => O(n)
# space => O(1)
# def finding(w,t):
# 	curr_word = ""
# 	for char in t: 
# 		if char == " ":
# 			if w == curr_word:
# 				return True
# 			else:
# 				curr_word = ""
# 		else:
# 			if len(curr_word) > len(w):
# 				continue
# 			else:
# 				curr_word += char
        
# 	return False



# w = "cast"
# t = "i built a nest and castle it "
# print(finding(w, t))


# #-------------------------------------------------------------------------------
# # #  MOve Element to End
# def moveElementToEnd(array, toMove):
#     for num in array:
#         if num == toMove:
#             array.pop(num)
#             array.append(num)
#     return array

# x = [2, 1, 2, 2, 2, 3, 4, 2]
# y = 2


# moveElementToEnd(x, y)

# # #  MOve Element to End
# def moveElementToEnd(array, toMove):
#     l, r = 0, len(array) - 1    
#     while l <  r and toMove in array:        
#         array.append(array.pop(array.index(toMove)))
#         l = array.index(toMove)
#         r -= 1
        
#     return array

# x = [2, 1, 3, 4, 2]
# y = 2
# moveElementToEnd(x, y)

# #-------------------------------------------------------------------------------
# # Monotonic Array
# messy
# def isMonotonic(array):
#     direction = 0
#     for i in range(len(array) - 1):
#         if array[i] == array[i + 1]:
#             continue
#         if direction == 0:
#             direction = -1 if array[i] > array[i + 1] else 1
#             # continue
#         if array[i] > array[i + 1] and direction == -1:
#             continue
#         elif array[i] < array[i + 1] and direction == 1:
#             continue
#         else:
#             return False
#     return True

#Clean with early breaks
# def isMonotonic(array):
#     arrInc, arrDec = False, False
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             arrDec = True
#         if array[i] < array[i + 1]:
#             arrInc = True
#         if arrDec == True and arrInc == True:
#             return False
#     return True



# x = [-1, -1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# isMonotonic(x)

# # #-------------------------------------------------------------------------------

# # #  
# def spiralTraverse(array):
#     useLen, ans, direction = len(array) - 1, [], False
#     topRow, lastRow = 0, len(array) - 1
#     topCol, lastCol = 0, len(array[0]) - 1
#     while topRow <= lastRow and topCol <= lastCol:
#         for col in range(topCol, lastCol + 1):
#             ans.append(array[topRow][col])
            
#         for row in range(topRow + 1, lastRow + 1):
#             ans.append(array[row][lastCol])
            
#         for col in range(lastCol - 1, topCol, -1):
#             if topRow == lastRow:
#                 break
#             ans.append(array[lastRow][col])
            
#         for row in range(lastRow, topRow, -1):
#             if topCol == lastCol:
#                 break
#             ans.append(array[row][topCol])
            
#         topRow += 1
#         lastRow -=1
#         topCol +=1        
#         lastCol -= 1     
    
#     return ans


# x = [
#     [1, 2, 3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10, 9, 8, 7]
# ]
# spiralTraverse(x)
# correctAnser = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# #-------------------------------------------------------------------------------
# # Longest Peak
# Mine that breaks on edge cases
# def longestPeak(array):
#     peak, current, i = 0, 0, 1
#     while i < len(array) - 1:
#         if array[i] > array[i - 1] or array[i + 1] > array[i] > array[i - 1]:
#             current += 1
#             peak = max(peak, current)
#             i += 1
            
#         elif array[i] < array[i - 1] > array[i - 2]:
#             current = 3
#             i += 1
#             while i < len(array) - 1 and array[i] < array[i - 1]:
#                 current +=1
#                 i += 1
#             peak = max(peak, current)
#             current = 0
#         else:
#             i += 1
#             current = 0
            
#     return peak

# # version found on Algo that is like mine
# def longestPeak(array):
#     ans_peak, curr_peak = 0, 0
#     for i in range(1,len(array)):
#         if array[i - 1] < array[i]:
#             if curr_peak == 0:
#                 curr_peak += 1
#             curr_peak += 1
#         elif array[i - 1] > array[i]:
#             if curr_peak > 0:
#                 curr_peak += 1
#                 ans_peak = max(ans_peak,curr_peak)
#                 if (i != len(array)-1) and array[i] < array[i + 1]:
#                     curr_peak = 0
#         else:
#             curr_peak = 0
#     return ans_peak



# x = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
# longestPeak(x)


# #-------------------------------------------------------------------------------
# #  Array of Products

#brute force O(n^2) time | O(n) space
# def arrayOfProducts(array):
#     ans = []
#     for i in range(len(array)):
#         running = 1
#         for num in (array[:i] + array[i+1:]):
#             running *= num
#         ans.append(running)
#     return ans

# #most efficient
# def arrayOfProducts(array):
#     ans = [1 for _ in range(len(array))]

#     running = 1
#     for i in range(len(array)):
#         ans[i] = running
#         running *= array[i]
    
#     running = 1
#     for i in reversed(range(len(array))):
#         ans[i] *= running
#         running *= array[i]
    
#     return ans


# x = [5, 1, 4, 2]
# arrayOfProducts(x)
# #-------------------------------------------------------------------------------
# # first duplicate value
# my best, their second best
# def firstDuplicateValue(array):
#     have = set()
#     for item in array:
#         if item in have:
#             return item
#         have.add(item)
#     return -1

# their best
# def firstDuplicateValue(array):
#     for item in array:
#         absVal = abs(item)
#         if absVal - 1 < 0:
#             return absVal
#         array[absVal - 1] *= -1
#     return -1


# x = [2, 1, 5, 2, 3, 3, 4]
# firstDuplicateValue(x)
# #-------------------------------------------------------------------------------

# # #  Merge Overlapping Intervals
# def mergeOverlappingIntervals(intervals):
#     sI = sorted(intervals, key=lambda x: x[0])
#     ans = [sI[0]]
#     for start, end in sI[1:]:
#         if start > ans[-1][1]:
#             ans.append([start,end])
#         else:
#             ans[-1][1] = max(end, ans[-1][1])        
    
#     return ans

# x= [
#     [1, 2],
#     [3, 5],
#     [4, 7],
#     [6, 8],
#     [9, 10]
#   ]
# mergeOverlappingIntervals(x)
# #-------------------------------------------------------------------------------
# # # Skilled with Adam
# # Can you see this?

# l = [1, 2, 3]

# d = {x: x + 1 for x in l}

# # Write me a function that will take in a string and return another string
# #   with all the letters in each word reversed (but the words in the original order still).
# #   e.g. "Hello world" -> "olleH dlrow"

# #Adam can you see this?


# def justLetter(string):
#     wordList =  string.split(" ")
#     for index, word in enumerate(wordList):
#         newWord = word[::-1]
#         wordList[index] = newWord

#     final = " ".join(wordList)
#     return final
    
    
# def justLetter(string):
#     return " ".join([word[::-1] for word in string.split(" ")])

# def justLetterOnly(string):
#     """This version only flips letters. It won't effect numbers"""
#     ans, word = '', []
#     for val in string:
#         if val.isalpha():
#             word.insert(0, val)
#         else:
#             ans += ''.join(word) + val
#             word = []
    
#     return ans

# def justLetterNum(string):
#     """This version flips letters AND numbers. In case there is leet code."""
#     ans, word = '', []
#     for val in string:
#         if val.isalpha() or val.isnumeric():
#             word.insert(0, val)
#         else:
#             ans += ''.join(word) + val
#             word = []
    
#     return ans



# print(justLetter("Hello  world!"))
# print(justLetterNum("He110  !W0R1*"))


# #-------------------------------------------------------------------------------
# #  skilled interview with Joel 
# class Node:
# 	value: int
#   left: Node
#   right: Node
  
#   def __init__(self, value):
#   	self.value = value
#     self.left = None
#     self.right = None
    
#   def isTargetInTree(self, target) -> bool:
#   		if target == self.value:
#         return True

#       elif target > self.value:
#       	if self.right == None:
#         	return False
#         else:
#         	return isTargetInTree(self.right, target)

#       elif target < self.value:
#       	if self.left == None:
#         	return False
#         else:
#         	return isTargetInTree(self.left, target)    



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------

# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------
# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------

# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------
# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------

# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------
# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------
# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------
# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------
# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------
# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------

# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------
# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------

# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------
# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------

# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------
# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------

# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------
# #  



# #-------------------------------------------------------------------------------
# # 


# #-------------------------------------------------------------------------------

