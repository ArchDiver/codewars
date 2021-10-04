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
# import math
# def threeNumberSum(array, targetSum):
#     array.sort()
#     # dict = {}
#     answer = []
#     # for i in array:
#     #     needSum = targetSum - i
#     #     dict[i] = needSum
#     go = math.ceil((len(array)-1) / 2)
#     for j in range(go):
#         char = array[j]
#         need = targetSum - char
#         left, right = j+1, (len(array)-1)
#         while left < right:
#             al = array[left]
#             ar = array[right]
#             sum = al + ar
#             if sum == need:
#                 list = [char, al, ar]
#                 answer.append(list)
#                 right -= 1
#                 left += 1
#             elif sum > need:
#                 right -= 1
#             else:
#                 left += 1

#     if answer:
#         return answer
#     return []


# array = [12, 3, 1, 2, -6, 5, -8, 6]
# targetSum = 0

# print(threeNumberSum(array, targetSum))

# # ----Mine longer run--
# import math
# def threeNumberSum(array, targetSum):
# 	# print(array, targetSum)
#     array.sort()
#     answer = []

#     # go = math.ceil((len(array)-1) / 2)
#     for j in range(len(array)-2):
#         char = array[j]
#         need = targetSum - char
#         left, right = j+1, (len(array)-1)
#         while left < right:
#             al = array[left]
#             ar = array[right]
#             sum = al + ar
#             if sum == need:
#                 list = [char, al, ar]
#                 answer.append(list)
#                 right -= 1
#                 left += 1
#             elif sum > need:
#                 right -= 1
#             else:
#                 left += 1
#     if answer:
#         return answer


#     return []

# array = [12, 3, 1, 2, -6, 5, -8, 6]
# targetSum = 0

# print(threeNumberSum(array, targetSum))

# # ----Thiers----
# def threeNumberSum(array, targetSum):
#     array.sort()
#     answers = []
#     for i in range(len(array) - 2):
#         left = i + 1
#         right = len(array) - 1
#         while left < right:
#             sum = array[i] + array[left] + array[right]
#             if sum == targetSum:
#                 answers.append([array[i], array[left], array[right]])
#                 left += 1
#                 right -= 1
#             elif sum < targetSum:
#                 left += 1
#             elif sum > targetSum:
#                 right -= 1

#     return answers
        
        
        
        
        
# array = [12, 3, 1, 2, -6, 5, -8, 6]
# targetSum = 0

# print(threeNumberSum(array, targetSum))

# # -------Smallest Diffenece--------------------------------------------------------------------------------------
# #------Mine-------
# def smallestDifference(arrayOne, arrayTwo):
#     arrayTwo.sort()
#     a1Num = arrayOne[0]
#     a2Num = arrayTwo[0]
#     diff = abs(a1Num - a2Num)
#     for num in arrayOne:
#         a1Num, a2Num, diff = check(num, arrayTwo, a1Num, a2Num, diff)
#     return [a1Num, a2Num]


# def check(num, arrayTwo, a1Num, a2Num, diff):
#     for i in range(len(arrayTwo) - 1):
#         j = i + 1
#         # diff2 = abs(arrayTwo[i] - num)
#         # diff3 = abs(arrayTwo[j] - num)
#         if abs(arrayTwo[i] - num) < abs(arrayTwo[j] - num):
#             if abs(arrayTwo[i] - num) < diff:
#                 return num, arrayTwo[i], abs(arrayTwo[i] - num)
#             else:
#                 return a1Num, a2Num, diff
#         if arrayTwo[j] == arrayTwo[-1]:
#             if abs(arrayTwo[j] - num) < diff:
#                 return num, arrayTwo[j], abs(arrayTwo[j] - num)
#             else:
#                 return a1Num, a2Num, diff



# arrayOne = [10, 0, 20, 25, 2000]
# arrayTwo = [1005, 1006, 1014, 1032, 1031]
# print(smallestDifference(arrayOne, arrayTwo))
# #-------Theirs------
# def smallestDifference(arrayOne, arrayTwo):
#     arrayOne.sort()
#     arrayTwo.sort()
#     idxOne, idxTwo, smallest = 0, 0, float('inf')
#     # current = float('inf')
#     smallestPair = []
#     while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
#         numOne, numTwo = arrayOne[idxOne], arrayTwo[idxTwo]
#         if numOne < numTwo:
#             current = numTwo - numOne
#             idxOne += 1
#         elif numTwo < numOne:
#             current = numOne - numTwo
#             idxTwo += 1
#         else:
#             return [numOne, numTwo]
#         if current < smallest:
#             smallest = current
#             smallestPair = [numOne, numTwo]
#     return smallestPair


# arrayOne = [10, 0, 20, 25, 2000]
# arrayTwo = [1005, 1006, 1014, 1032, 1031]
# print(smallestDifference(arrayOne, arrayTwo))


# # ------Move Element to end---------------------------------------------------------------------------------------
# # #------First try
# def moveElementToEnd(array, toMove):
# 	for i in range(len(array) - 1):
# 		if array[i] == toMove:
# 			array.append(array.pop(array.index(i)))
# 	return array

# array = [2, 1, 2, 2, 2, 3, 4, 2]
# toMove = 2

# print(moveElementToEnd(array, toMove))

# #------really stripped with __eq__
# def moveElementToEnd(array, toMove):
#     array = array.sort(key = toMove.__eq__)
#     return array

# array = [2, 1, 2, 2, 2, 3, 4, 2]
# toMove = 2

# print(moveElementToEnd(array, toMove))

# #----------thiers
# def moveElementToEnd(array, toMove):
#     i, j = 0, len(array) - 1
#     while i < j:
#         while i < j and array[j] == toMove:
#             j -= 1
#         if array[i] == toMove:
#             array[i], array[j] = array[j], array[i]
#         i += 1

#     return array

# array = [2, 1, 2, 2, 2, 3, 4, 2]
# toMove = 2

# print(moveElementToEnd(array, toMove))

# # ------Monotonic Array---------------------------------------------------------------------------------------
# # -----Mine----
# def isMonotonic(array):
#     if array == [] or len(array) == 1:
#         return True
#     for i in range(len(array) - 1):
#         j = i + 1
#         while array[i] == array[j]:
#             i += 1
#             j += 1
#         if array[i] < array[j]:
#             for k in range(i, len(array) - 1):
#                 j = k + 1
#                 if array[k] > array[j]:
#                     return False
#             return True
#         elif array[i] > array[j]:
#             for k in range(i, len(array) - 1):
#                 j = k + 1
#                 if array[k] < array[j]:
#                     return False
#             return True
#     return True


# array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

# print(isMonotonic(array))

# #------theirs (with my add to cut short if found early)----
# def isMonotonic(array):
#     nonDec = True
#     nonInc = True
#     for i in range(1, len(array)):
#         if array[i] < array[i-1]:
#             nonDec = False
#         if array[i] > array[i - 1]:
#             nonInc = False
#         # # I added the next line to cut the run shorter
#         if nonDec == False and nonInc == False:
#             return False
#     return True


# # ------Spiral Traverse---------------------------------------------------------------------------------------
# # #----Iterative
# # # 0(n) Time and 0(n) space 
# def spiralTraverse(array):
#     solution = []
#     firstRow, lastRow = 0, len(array)-1
#     firstCol, lastCol = 0, len(array[0]) -1
#     while firstRow <= lastRow and firstCol <= lastCol:
#         for col in range(firstCol, lastCol +1):
#             solution.append(array[firstRow][col])
#         for row in range(firstRow + 1, lastRow + 1):
#             solution.append(array[row][lastCol])
#         for col in reversed(range(firstCol, lastCol)):
#             if firstRow == lastRow:
#                 break
#             solution.append(array[lastRow][col])
#         for row in reversed(range(firstRow + 1, lastRow)):
#             if firstCol == lastCol:
#                 break
#             solution.append(array[row][firstCol])
#         firstRow += 1
#         lastRow -= 1
#         firstCol += 1
#         lastCol -= 1
        
#     return solution



# array = [
#   [1, 2, 3, 4],
#   [12, 13, 14, 5],
#   [11, 16, 15, 6],
#   [10, 9, 8, 7]
# ]
# print(spiralTraverse(array))

# # # ------Recursive
# def spiralTraverse(array):
#     solution = []
#     spiralPath(array, 0, len(array) - 1, 0, len(array[0]) - 1, solution)
#     return solution

# def spiralPath(array, fr, lr, fc, lc, solution):
#     if fc > lc or fr > lr:
#         return
#     for col in range(fc, lc + 1):
#         solution.append(array[fr][col])
#     for row in range(fr + 1, lr + 1):
#         solution.append(array[row][lc])
#     for col in reversed(range(fc, lc)):
#         if fr == lr:
#             break
#         solution.append(array[lr][col])
#     for row in reversed(range(fr + 1, lr)):
#         if fc == lc:
#             break
#         solution.append(array[row][fc])
    
#     spiralPath(array, fr + 1, lr - 1, fc + 1, lc - 1, solution)
    
# array = [
#     [1, 2, 3, 4],
#     [10, 11, 12, 5],
#     [9, 8, 7, 6]
#   ]
# print(spiralTraverse(array))

# # -----Longest Peak----------------------------------------------------------------------------------------
# # -----mine---not working
# def longestPeak(array):
#     peak = float('inf')
#     longest = []
#     currentLong = []
#     i = 0
#     while i < len(array) - 1:
#         j = i + 1
#         k = j + 1
#         while array[i] < array[j] < array[k]:
#             currentLong.append(array[i],array[j],array[k])
#             if array[k + 1] < array[k]:
#                 if len(currentLong) > len(longest):
#                     longest = currentLong
#                     peak = k
#                 i = k + 1
#                 break
#             i = k
#             j = i + 1
#             k = j + 1
                
#     return peak

# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

# print(longestPeak(array))
# #---Mine after version 2
# def longestPeak(array):
#     longestPeak  = 0
#     i = 1
#     while i < len(array)-1:
#         j, k = i - 1, i + 1
#         peak = array[j] < array[i] and array[k] < array[i]
#         if not peak:
#             i += 1
#             continue
        

#         while array[j] > array[j - 1]:
#             currentPeak +=1
#             j -= 1
#         while array[k] > array[k + 1]:
#             currentPeak += 1
#             k += 1
#         if currentPeak > longestPeak:
#             longestPeak = currentPeak

                
#     return longestPeak

# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

# print(longestPeak(array))
# # #-------theirs
# def longestPeak(array):
#     longestPeak  = 0
#     i = 1
#     while i < len(array)-1:
#         peak = array[i - 1] < array[i] and array[i + 1] < array[i]
#         if not peak:
#             i += 1
#             continue
        
#         left = i - 2
#         while left >= 0 and array[left] < array[left + 1]:
#             left -= 1
#         right = i + 2
#         while right < len(array) and array[right] < array[right - 1]:
#             right +=1
#         currentPeak = right - left - 1
#         longestPeak = max(longestPeak, currentPeak)
#         i = right
                
#     return longestPeak

# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

# print(longestPeak(array))

# # -----Array of Products----------------------------------------------------------------------------------------
# # -----mine worst time complexity
# # O(n^2) time and O(n)
# def arrayOfProducts(array):
#     array2 = []
#     i = 0
#     for  i in range(len(array)):
#         product = 1
#         for j in range(len(array)):
#             if j == i:
#                 continue
#             product *= array[j]
#         array2.append(product)
#     return array2

# array = [5,1,4,2]
# print(arrayOfProducts(array))
# # Thiers 
# # O(n) time and O(n)
# def arrayOfProducts(array):
#     out_array = [1 for _ in range(len(array))]
#     r_array = [1 for _ in range(len(array))]
#     l_array = [1 for _ in range(len(array))]
#     product = 1
#     for i in range(len(array)):
#         r_array[i] = product
#         product *= array[i]
#     product = 1
#     for i in reversed(range(len(array))):
#         l_array[i]  = product
#         product *= array[i]
#     for i in range(len(array)):
#         out_array[i] = r_array[i] * l_array[i]

#     return out_array

# array = [5,1,4,2]
# print(arrayOfProducts(array))
# # # -----Best
# # # O(n) time and O(n)
# def arrayOfProducts(array):
#     out_array = [1 for _ in range(len(array))]

#     product = 1
#     for i in range(len(array)):
#         out_array[i] = product
#         product *= array[i]
#     product = 1
#     for i in reversed(range(len(array))):
#         out_array[i]  *= product
#         product *= array[i]

#     return out_array

# array = [5,1,4,2]
# print(arrayOfProducts(array))

# # ----First Duplicate Value-----------------------------------------------------------------------------------------
# #---mine
# def firstDuplicateValue(array):
#     seen_array = []
#     for i in array:
#         if i in seen_array:
#             return i
#         seen_array.append(i)
#     return -1

# array = [2, 1 , 5, 2, 3, 3, 4]
# print(firstDuplicateValue(array))
# # #---Best but only under the circumstances where we have int 1 to n and can mutate
# def firstDuplicateValue(array):
#     for i in array:
#         abs_val = abs(i)
#         if array[abs_val - 1] < 0:
#             return abs_val
#         array[abs_val - 1] *= -1

#     return -1

        

# array = [2, 1 , 5, 2, 3, 3, 4]
# print(firstDuplicateValue(array))


# # ------Merge Overlapping Intervals---------------------------------------------------------------------------------------
# # -----Mine first
# def mergeOverlappingIntervals(intervals):
#     out_array = []
#     intervals.sort()
#     for index, interval in enumerate(intervals):
#         next = intervals[index + 1]
#         if interval[1] > next[0]:
#             if out_array[-1][1] < next[1]:
#                 out_array = [[out_array[0],next[1]]]
#             else:
#                 out_array.append([interval[0], next[1]])
#         else:
#             out_array.append(interval)
    
#     return out_array

# intervals = [
#     [1, 2],
#     [3, 5],
#     [4, 7],
#     [6, 8],
#     [9, 10]
# ]

# print(mergeOverlappingIntervals(intervals))

# # -----
# def mergeOverlappingIntervals(intervals):
#     out_array = []
#     intervals.sort()
#     i = 0
#     while i < range(len(intervals) - 2):
#         j = i + 1
#         if intervals[i][1] < intervals[j][0]:
#             low = intervals[i][0]
#             high = high = max(intervals[i][1], intervals[j][1])
#             while intervals[i][1] < intervals[j][0]:
#                 high = max(intervals[i][1], intervals[j][1])
#                 i += 1
#                 j += 1
#             out_array.append([low, high])
#         else:
#             out_array.append(intervals[i])
    
#     return out_array

# intervals = [
#     [1, 2],
#     [3, 5],
#     [4, 7],
#     [6, 8],
#     [9, 10]
# ]

# print(mergeOverlappingIntervals(intervals))
# #------Mine working
# def mergeOverlappingIntervals(intervals):
#     intervals.sort()
#     out_array = [intervals[0]]
#     i = 1
#     while i < len(intervals):
#         if intervals[i][0] <= out_array[-1][1]:
#             out_array[-1][1] = max(intervals[i][1],out_array[-1][1])
#         else:
#             out_array.append(intervals[i])        
#         i += 1
    
#     return out_array

# intervals = [
#     [1, 2],
#     [3, 5],
#     [4, 7],
#     [6, 8],
#     [9, 10]
# ]

# print(mergeOverlappingIntervals(intervals))
# # ----Their code--O(nlog(n)) time | O(n) space
# def mergeOverlappingIntervals(intervals):
#     sortedIntervals = sorted(intervals, key=lambda x: x[0])
#     mergedIntervals = []
#     currentInterval = sortedIntervals[0]
#     mergedIntervals.append(currentInterval)

#     for nextInterval in sortedIntervals:
#         _, currentIntervalEnd = currentInterval
#         nextIntervalStart, nextIntervalEnd = nextInterval

#         if currentIntervalEnd >= nextIntervalStart:
#             currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)

#         else:
#             currentInterval = nextInterval
#             mergedIntervals.append(currentInterval)

#     return mergedIntervals
# # -----BST Construction----------------------------------------------------------------------------------------
# #---Theirs
# # Avg = O(log(n)) time| O(log(n)) space(if recursive) or O(1) space(if iterative), worst O(n) time | O(log(n)) space(if recursive) or O(1) space(if iterative)
# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
# # ----iterative  O(log(n)) time | O(1) space
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right

        return self

    def contains(self, value):

        pass

    def remove(self, value, parentNode = None):

        return self

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