# # Two Number Sum---------------------------------------------------------------------------------------------
# def twoNumberSum(array, targetSum):
#     # Write your code here.
#     answer = []
#     for i in range(len(array)):
#         for j in range((i+1),len(array)):
#             if (array[i] + array[j]) == targetSum:
#                 answer.append(array[i])
#                 answer.append(array[j])
#     return answer

# # Validate Subsequence---------------------------------------------------------------------------------------------
# def isValidSequence(a, b):
#     # Write your code here. 
#     if len(b) > len(a):
#         return False
#     for i in range(len(a)):
#         bVal = b[i]
#         if a == []:
#             return False
#         for j in range(len(a)):
#             if b[i] in a:
#                 bVal = b[i]
#                 place = a.index(b[i])
#                 a = a[place+1:]
#                 break
#             else:
#                 return False
#     return True

# # Find Closest Value in BST---------------------------------------------------------------------------------------------
# def findClosestValueinBst(tree, target):
#     #write code here
#     #float('inf') gives an infinite value. This helps to find the lowest value of something.
#     close = float('inf')
#     return closest(tree, target,close)
# def closest(bst, t, c):
#     if bst is None:
#         return c
#     if abs(t-c) > abs(t-bst.value):
#         c = bst.value
#     if t < bst.value:
#         return closest(bst.left, t, c)
#     elif t > bst.value:
#         return closest(bst.right, t, c)
#     else:
#         return c
    

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

# def branchSums(root):
#     #write your code here.
#     sumList = []
#     bstSums(root, 0, sumList)
#     return sumList

# def bstSums(node, runSum, sumList):
#     if node is None:
#         return
#     newRunSum = runSum + node.value
#     if node.left is None and node.right is None:
#         sumList.append(newRunSum)
#         return
#     bstSums(node.left, newRunSum, sumList)
#     bstSums(node.right, newRunSum, sumList)


# # Node Depths---------------------------------------------------------------------------------------------
# Option 1 (recursive=clean) O(n) time | O(h) space
# def nodeDepth(root, depth=0):
#     # Write your code here.
#     if root is None:
#         return 0
#     return depth + nodeDepth(root.left, depth + 1) + nodeDepth(root.right, depth + 1)


#Option 2 (iterative=same run time just less pretty) O(n) time | O(h) space
# def nodeDepths(root):
#     depthsSum = 0
#     stack = [{"node": root, "depth": 0}]
#     while len(stack) > 0:
#         nodeInfo = stack.pop()
#         node, depth = nodeInfo["node"], nodeInfo["depth"]
#         if node is None:
#             continue
#         depthsSum += depth
#         stack.append({"node": node.left, "depth": depth + 1})
#         stack.append({"node": node.right, "depth": depth + 1})
#     return depthsSum

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
# class Node:
#     def __init__(self, name):
#         self.children = []
#         self.name = name

    # # Not sure this is needed
    # def addChild(self, name):
    #     self.children.append(Node(name))
    #     return self
    
    #This is where most of the action happens.
    # Time = O(v(ertices) + e(dges)) Space = O(v)
    # def depthFirstSearch(self, array):
    #     # Write your code here.
    #     array.append(self.name)
    #     for child in self.children:
    #         child.depthFirstSearch(array)
    #     return array
    #     pass

# # Min Wait Time---------------------------------------------------------------------------------------------
# Time = O(nlogn) , space = O(1)
# def minimumWaitingTime(queries):
#     queries.sort()
#     waitTime = 0

    # Theirs
    # for idx, val in enumerate(queries):
    #     waitTime += val * (len(queries) - (idx + 1)) 
    # return waitTime

    # # Mine
    # left = len(queries)
    # for dog in queries:
    #     left -= 1
    #     waitTime += dog * left
    # return waitTime

# # Nth Fibinacci---------------------------------------------------------------------------------------------

##weak time=O(2^n), space=O(n)
# def getNthFib(n):
#     Write your code here.

#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         # This section runs all of the branches over and over
#         return getNthFib(n-1) + getNthFib(n-2)
#  ## better time=O(n) space=O(n)
# def getNthFib(n, nums={1:0, 2:1}):
#     if n in nums:
#         return nums[n]
#     else:
#         nums[n] = getNthFib(n-1, nums) + getNthFib(n-2, nums)
#         return nums[n]
# Best time=O(n) space= o(1)
# def getNthFib(n):
#     fib = [0,1]
#     counter = 3
#     while counter <= n:
#         next = fib[1] + fib[0]
#         fib[0] = fib[1]
#         fib[1] = next
#         counter += 1
#     return fib[1] if n > 1 else fib[0]

# # Product Sum with a "special" array ---------------------------------------------------------------------------------------------
# # e.g. [x,[y,z]] = x + 2*(y+z) or [x[y[z]]] = x+ 2 * (y + 3 * (z)
# def productSum(array, depth=1):
#     sum = 0
#     for item in array:
#         if type(item) is list:
#             sum += productSum(item, depth + 1)
#         else:
#             sum += item
#     return sum * depth


# # Bianary Tree Search---------------------------------------------------------------------------------------------
#  # time = O(log(n)) space = O(log(n))
# def binarySearch(array, target):
#     return helper(array, target, 0, len(array)-1)

# def helper(a, t, l, r):
#     if l > r:
#         return -1
#     mid = (l + r ) // 2
#     match = a[mid]
#     if t == match:
#         return mid
#     elif t > match:
#         return helper(a, t, mid +1, r)
#     else:
#         return helper(a, t, l , mid -1)

# # # time = O(log(n)) space = O(1)
# def binarySearch(array, target):
#     return helper(array, target, 0, len(array)-1)
# def helper(a, t, r, l):
#     while l <= r:
#         mid = (l+r) //2
#         match = a[mid]
#         if t == match:
#             return mid
#         elif t < match:
#             r = mid - 1
#         elif t > match:
#             left = mid + 1
#         else:
#             return -1

# def binarySearch(array, target):
#     return helper(array, target, 0, len(array)-1)

# def helper(a, t, l, r):
    # while l <= r:
    #     mid = (l + r) // 2
    #     centerVal = a[mid]
    #     if t == centerVal:
    #         return mid
    #     elif t < centerVal:
    #         right = mid - 1
    #     elif t > centerVal:
    #         l = mid + 1
    #     else:
    #         return -1
    # if l > r:
    #     return -1
    # elif t < mid:
    #     return helper(array, target, 0, mid - 1)
    # else:
    #     return helper(array, target, mid + 1, r)

# # Find Three Largest Numbers---------------------------------------------------------------------------------------------
# def findThreeLargestNumbers(array):
#     # Write your code here.
# 	last = [None, None, None]
#     for num in array:
#         checkNum(last, num)
#     return last
# def checkNum(last, num):
# 	if last[2] is None or num > last[2]:
# 		updateLast(last, num, 2)
# 	elif last[1] is None or num > last[1]:
# 		updateLast(last, num, 1)
# 	elif last[0] is None or num > last[0]:
# 		updateLast(last, num, 0)
		
# def updateLast(last, num, idx):
# 	for i in range(idx + 1):
# 		if i == idx:
# 			last[i] = num
# 		else:last[i] = last[i + 1]



# # Bubble Sort---------------------------------------------------------------------------------------------
# # # Mine
# def bubbleSort(array):
#     swap = False
#     while not swap:
#         swap = True
#         for i in range(len(array) - 1):
#             b = array[i + 1]
#             array[i + 1] = array[i]
#             array[i] = b
#             swap = False
#         else:
#             continue
#     return array

# # # Algo's edits
# def bubbleSort(array):
#     swap = False
#     counter = 0
#     while not swap:
#         swap = True
#         for i in range(len(array) - 1 - counter):
#             if array[i] > array[i + 1]:
#                 switch(i, i+1, array)
#     return array

# def switch(i, j, array):
#     array[i], array[j] = array[j], array[i]




# # # Tournamaent Winner---------------------------------------------------------------------------------------------
# def tournamentWinner(competitions, results):
#     win = ''
#     rank = {win:0}
#     for teams, result in zip(competitions, results):
#         team = teams[0] if result == 1 else teams[1]
#         if team not in rank:
#             rank[team] = 0
#         rank[team] +=3
#         if rank[team] > rank[win]:
#             win = team
#     return win


# # Non-Constructible Change---------------------------------------------------------------------------------------------
# # Mine that didn't work and would have been inefficiant
# def nonConstructibleChange(coins):
#     c = sorted(coins)
# 	nope = False
# 	val = 1
# 	while not nope:
# 		if val in c or check(c, val):
# 			val += 1
# 		else:
# 			nope = True
#     return val

# def check(c, val):
# 	total = c[0]
# 	count = 1
# 	while total < val:
# 		total += c[count]
# 		count += 1
# 	return True if total == val else False

# Algo version time = O(nlogn) space = 0(1)
# def nonConstructibleChange(coins):
#     coins.sort()
#     total = 0
#     for coin in coins:
#         if coin > total + 1:
#             return total + 1
#         total += coin
#     return total + 1

# # Class Photo---------------------------------------------------------------------------------------------
# def classPhotos(front, back):
#     front.sort(reverse=True)
#     back.sort(reverse=True)
#     if front[0] > back[0]:
#         front, back = back, front
#     for i in range(len(front)):
#         if front[i] >= back[i]:
#             return False
#     return True

# # Remove Duplicates from linked list---------------------------------------------------------------------------------------------
# This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# def removeDuplicatesFromLinkedList(linkedList):
#     currentNode = linkedList
#     # this loops through the whole linked list
#     while currentNode is not None:
#         nextNode = currentNode.next
#         # This loops through checking for and removing duplicates. (This only works if they are sorted)
#         while nextNode is not None and nextNode.value == currentNode.value:
#             nextNode = nextNode.next
#         # this changes the point THEN changes the node
#         currentNode.next = nextNode
#         currentNode = nextNode

#     return linkedList
# def removeDuplicatesFromLinkedList(linkedList):
#     currentNode = linkedList
#     # this loops through the whole linked list
#     while currentNode is not None:
#         nextNode = currentNode.next
#         # This loops through checking for and removing duplicates. (This only works if they are sorted)
#         while nextNode is not None and nextNode.value == currentNode.value:
#             nextNode = nextNode.next
#         # this changes the point THEN changes the node
#         currentNode.next = nextNode
#         currentNode = nextNode

#     return linkedList


# # sorted sq array ---------------------------------------------------------------------------------------------
# # This version time = O(nLogn) Space = O(n)
# def squaredSorted(array):
#     squaredArray= []
    
#     for i in range(len(array)):
#         squaredArray.append(array[i]**2)
    
#     squaredArray.sort()
#     return squaredArray


# # This version is O(n) for both time and space
# def sortedSquared(array):
#     squareArray = []
#     lowValIdx = 0
#     highValIdx = len(array)-1

#     for i in reversed(range(len(array))):
#         low = array[lowValIdx]
#         high = array[highValIdx]

#         if abs(low) > abs(high):
#             squareArray[i] = low**2
#             lowValIdx +=1
#         else:
#             squareArray[i] = high**2
#             highValIdx -= 1

#     return squareArray

# # ---------------------------------------------------------------------------------------------
# # Insertion Sort

# def insertionSort(array):
#     # Write your code here.
#     for i in range(1,len(array)):
#         j = i 
#         while j > 0 and array[j] < array[j - 1]:
#             array[j-1], array[j] =  array[j], array[j-1]
#             j -= 1
#     return array
    
# array = [8, 5, 2, 9, 5, 6, 3]
# print(insertionSort(array))

# # ---------------------------------------------------------------------------------------------
# # Selection sort
# # time O(n^2) space O(1)

# def selectionSort(array):
#     # Write your code here.
# 	idx = 0
# 	while idx < len(array) - 1:
# 		small = idx
# 		for i in range(idx + 1, len(array)):
# 			if array[small] > array[i]:
# 				small = i
# 		array[idx], array[small] = array[small], array[idx]
# 		idx += 1			
#     return array


# array [8, 5, 2, 9, 5, 6, 3]
# print(selectionSort(array))

# # ---------------------------------------------------------------------------------------------
# # Palindrome Check
# def isPalindrome(string):
#     # Write your code here.
#     for i in range(1,round(len(string)/2)):
#         low = string[i - 1]
#         high = string[i * -1]
#         if low != high:
#             return False
#     return True

# #timeO(n^2) space O(n)
# def isPalindrome(string):
#     reversedString = ''
#     for i in reversed(range(len(string))):
#         reversedString += string[i]
#     return string == reversedString

# # time O(n) space O(n)
# def isPalindrome(string):
#     revChar = []
#     for i in reversed(range(len(string))):
#         revChar.append(string[i])
#     return string == "".join(revChar)

# # time O(n) space O(n)
# def isPalindrome(string, idx = 0):
#     j = len(string) -1 - idx
#     return True if idx >= j else string[idx] == string[j] and isPalindrome(string, idx + 1)

# # # Same as above just written out.
# def isPalindrome(string, idx = 0):
#     j = len(string) -1 - idx
#     if idx >= j:
#         return True
#     if string[idx] != string[j]:
#         return False
#     return isPalindrome(string, i + 1)

# string = "racecar"
# print(isPalindrome(string))

# # ---------------------------------------------------------------------------------------------
# # #caesar cipher
# def caesarCipherEncryptor(string, key):
    # Write your code here.
    # str = string
    
    # this catches a shift that is greater than 26
#     key = key % 26
#     new = []
#     for letter in string:
#         shift = (ord(letter) + key)
#         if shift <= 122:
#             new.append(chr(shift))
#         else:
#             new.append(chr(96 + (shift % 122)))
#     return str

# string = 'xyz'
# key = 2

# print(caesarCipherEncryptor(string, key))

# # # Algo option with unx 
# # O(n)for time and space
# def caesarCipherEncryptor(string, key):
#     newLetter = []
#     newKey = key % 26
#     for letter in string:
#         newLetter.append(getNewletter(letter, newKey))
#     return "".join(newLetter)

# def getNewletter(letter, key):
#     newLetterCode = ord(letter) + key
#     return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

# # Algo without unx
# # O(n)for time and space 
# def caesarCipherEncryptor(string, key):
#     newLetter = []
#     newKey = key % 26
#     alph = list("abcdefghijklmnopqrstuvwxyz")
#     for letter in string:
#         newLetter.append(getNewletter(letter, newKey, alph))
#     return "".join(newLetter)

# def getNewletter(letter, key, alph):
#     newLetterCode = alph.index(letter) + key
#     return alph[newLetterCode % 26]


# # ---------------------------------------------------------------------------------------------# # ---------------------------------------------------------------------------------------------
# # # Run-Length Encoding O(n) Time/Space
# def runLengthEncoding(string):
#     # Write your code here.
#     count = 1
#     string_list = [] 
    
#     for i in range(1, len(string)):

#         if string[i] != string[i-1] or count == 9:
#             string_list.append(str(count))
#             string_list.append(string[i-1])
#             count = 0            
#         count += 1
		
#     string_list.append(str(count))
#     string_list.append(string[-1])
	
#     return ''.join(string_list)


# string = "AAAAAAAAAAAAABBCCCCDD"

# print(runLengthEncoding(string))


# # ----Tandem Bicycle-----------------------------------------------------------------------------------------
# def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
#   red = sorted(redShirtSpeeds)
#   blue = sorted(blueShirtSpeeds)
#   total_speed = 0
#   if fastest == True:
#       x,y = 1, -1
#   elif fastest == False:
#       x,y = 0, 1        

#   for i in range(len(red)):
#       j = (i + x) * y
#       if red[i] >= blue[j]:
#           total_speed += red[i]
#       elif blue[j] > red[i]:
#           total_speed += blue[j]
          
#   return total_speed
  
# r = [5, 5, 3, 9, 2]
# b = [3, 6, 7, 2, 1]
# f = False

# print(tandemBicycle(r, b, f))

# # =====

# def tandemBicycle2(redShirtSpeeds, blueShirtSpeeds, fastest):
#   total_speed = 0
#   blueShirtSpeeds.sort()

#   if fastest == True:
#     redShirtSpeeds.sort(reverse=True)
#   elif fastest ==False:
#     redShirtSpeeds.sort()

#   for i in range(len(redShirtSpeeds)):
#     if redShirtSpeeds[i] >= blueShirtSpeeds[i]:
#       total_speed += redShirtSpeeds[i]
#     elif blueShirtSpeeds[i] > redShirtSpeeds[i]:
#       total_speed += blueShirtSpeeds[i]
          
#   return total_speed
    
# r2 = [5, 5, 3, 9, 2]
# b2 = [3, 6, 7, 2, 1]
# f2 = False

# print(tandemBicycle2(r2, b2, f2))
# # =====
# def tandemBicycle3(redShirtSpeeds, blueShirtSpeeds, fastest):
#   total_speed = 0
#   blueShirtSpeeds.sort()

#   if fastest == True:
#     redShirtSpeeds.sort(reverse=True)
#   elif fastest ==False:
#     redShirtSpeeds.sort()

#   for i in range(len(redShirtSpeeds)):
#     total_speed += max(redShirtSpeeds[i], blueShirtSpeeds[i])

          
#   return total_speed
    
# r3 = [5, 5, 3, 9, 2]
# b3 = [3, 6, 7, 2, 1]
# f3 = False

# print(tandemBicycle3(r3, b3, f3))

# # ----Generate Document-----------------------------------------------------------------------------------------
# def generateDocument(characters, document):
#   counted = {}
#   for char in characters:
#     if char not in counted:
#       counted[char] = 1
#     else:
#       counted[char] += 1

#   for char in document:
#     if char not in counted or counted[char] <= 0:
#       return False
#     else:
#       counted[char] -= 1

#   return True


# characters = "Bste!hetsi ogEAxpelrt x "
# document = "AlgoExpert is the Best!"

# print(generateDocument(characters, document))
# # ---------------------------------------------------------------------------------------------
# #This gives the value not the index
# def firstNonRepeatingCharacter(string):
#     stored_vals = {}
#     nonrepeat = None
#     for i in range(len(string)):
#         if string[i] not in stored_vals:
#             stored_vals[string[i]] = 1
#         else:
#             stored_vals[string[i]] += 1
            
#     for key, value in stored_vals.items():
#         if value == 1:
#             return key
    
#     return -1

# string = "abcdcaf"

# print(firstNonRepeatingCharacter(string))
# #-------Not correct-----
# def firstNonRepeatingCharacter(string):
#     stored_vals = {}
#     nonrepeat = None
#     for i in range(len(string)):
#         if string[i] not in stored_vals:
#             stored_vals[string[i]] = i
#         else:
#             stored_vals[string[i]] = stored_vals[string[i]], i
#     for key, value in stored_vals.items():
#         if value == 1:
#             return key
    
#     return -1

# string = "aaabcdcaf"

# print(firstNonRepeatingCharacter(string))
# # -----------
# def firstNonRepeatingCharacter(string):
#     stored_vals = {}
#     for char in string:
#         if char not in stored_vals:
#             stored_vals[char] = 1
#         else:
#             stored_vals[char] += 1
#     for key, value in stored_vals.items():
#         if value == 1:
#             for idx in range(len(string)):
#                 if string[idx] == key:
#                     return idx    
#     return -1

# string = "abcdcaf"

# print(firstNonRepeatingCharacter(string))
# #----------------"best?"----
# def firstNonRepeatingCharacter(string):
#     charFreq = {}
    
#     for char in string:
#         charFreq[char] = charFreq.get(char, 0) + 1
        
#     for i in range(len(string)):
#         character = string[i]
#         if charFreq[character] == 1:
#             return i
#     return -1

# string = "aabcdcaf"

# print(firstNonRepeatingCharacter(string))



# # ------Three number sum---------------------------------------------------------------------------------------
def threeNumberSum(array, targetSum):
    array.sort()
    dict = {}
    for i in array:
        needSum = targetSum - i
        

    return {}


array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print(threeNumberSum(array, targetSum))





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