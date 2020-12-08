# fruits= ['apple', 'orange', 'bannana', 'grape']
# fruits[2] = 'pine'
# fruits.reverse()
# print(len(fruits))

# for value in range(1,5):
# print(value)

# numbers = list(range(1,6))
# print(numbers)
# # not finished

# avengers = ['thor', 'ironman', 'black panther', 'spider-man', 'hulk']

# print(avengers[2:4])

# current = 1

# while current <= 100:
#     x = current % 2
#     if x == 0:
#          print(current)
#          current+= 1
#     else:
#             current+= 1
# stock = {
#     'football': 4,
#     'boardgame': 10,
#     'leggos': 1,
#     'doll': 5,
# }
# def fillable(stock, merch, n):
#     # Your code goes here.
#     for merch in stock:
#         i = stock["merch"]
#         if n >= i:
#             print(True)
#         else:
#             print(False)
# fillable(stock, 'football', 2)

# def remove(s):
#     s.replace('!', '')
#     return s

# remove("hi!")
# remove('hi!!!')

# def high_and_low(numbers):
#     nums = numbers.split()
#     new_list = []
#     for n in nums:
#         new_list.append(int(n))
#     nums = new_list

#     x = str(max(nums))
#     y = str(min(nums))
#     # answer = (x, y)
#     print(x + " " +y)


# def high_and_low(numbers):
#     # ...
#     newlist = numbers.split()
    
#     new_numbers = []
#     for n in newlist:
#     	new_numbers.append(int(n))

#     newnums = new_numbers
#     # newlist = map(int, newnums)
#     maximum = str(max(newnums))
#     minimum = str(min(newnums))
#     output = 
#     return output
# def high_and_low(numbers): #z.
#     for s in numbers.split(" ")
#         print(s)
    # nn = [int(s) for s in numbers.split(" ")]
    # print(nn)
    # print(max(nn))
    # print(min(nn))
    # print(max(nn),min(nn))

    # return "%i %i" % (max(nn),min(nn))

# print(high_and_low("1 2 3 4 5"))  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Is your period late?
# # In this kata, we will make a function to test whether a period is late.
# # Our function will take three parameters:
# # last - The Date object with the date of the last period
# # today - The Date object with the date of the check
# # cycleLength - Integer representing the length of the cycle in days
# # If the today is later from last than the cycleLength, the function should return true. We consider it to be late if the number of passed days is larger than the cycleLength. Otherwise return false.

# def period_is_late(last,today,cycle_length):
# #     #your code here
#     print(last)
#     print(today)
#     print(cycle_length)
#     x = 0
#     x = date(last)
#     # if (datetime.date(last) + cycle_length) < datetime.date(today):
#     #     print(True)
#     #     return True
#     # else:
#     #     print(False)
#     #     return False
 

# from datetime import date
# period_is_late((2016, 6, 13), (2016, 7, 16), 35)
# from datetime import date


# myBday = date(1979, 11, 5)
# print(myBday)
# today = date.today()
# print(today)
# time_between = today - myBday
# print(time_between)
# years = (time_between / 365)
# print(years)
# -------------------------------------------------------------------------------
# # check for palindrome

# def pali (string):
#     string = string.lower()
#     if string == string [::-1]:
#         print("Palindrome")
#     else:
#         print("Not a palindrome")
# word =input("enter a word: ")
# pali(word)






# -----------------------------------------------------------------------------------------------------------
# import timeit
# max = 100
# # code_to_test = """
# # stop = 10,000
# # for x in range(2, stop+1):
# #     prime = True
# #     for y in range(2, x):
# #         if x % y == 0
# #         prime = False
# #     if prime:
# #         # print(x)
# # """
# # code2 = """"
# # for x in range(2, stop+1):
# #     prime = True
# #     for y in range(2, x):
# #         if x % y == 0
# #         prime = False
# #         break
# #     if prime:
# #         print(x)
# # """
# # code3 = """
# primesList = []

# for x in range(2, max+1):
#     prime = True

#     for y in range(2,x):
#         if x % y == 0:
#             prime = False
#             break
#     if prime:
#         primesList.append(x)
# print(primesList)
# # """
# # code_to_test = """

# max = 100
# primesList = []

# for x in range(2, max + 1):
#     prime = True

#     for y in range(2, (int(x**0.5)+1)):
#         if x % y == 0:
#             prime = False
#             break
#     if prime:
#         primesList.append(x)
# print(primesList)
# #"""

# # code1_time = timeit.timeit(code1, number=1)
# # print(code1_time)
# # code2_time = timeit.timeit(code2, number=100)/100
# # print(code2_time)
# code3_time = timeit.timeit(code3, number=100)/100
# print(code3_time)
# # code4_time = timeit.timeit(code4, number=100)/100
# # print(code4_time)

# # import timeit
# # code_to_test = """
# # a = range(100000)
# # b = []
# # for i in a:
# #     b.append(i*2)
# # """
# # elapsed_time = timeit.timeit(code_to_test, number=100)/100
# # print(elapsed_time)

# age_check = int(input("How old are you? "))
# print(age_check)

# if age_check < 18:
#     print("You are a kid.")
# elif: age_check >= 18 && age_check <= 65:
#     print("Your an adult.")
# else:
#     print("Your a senior. Congrats!")


# ----------------------------------------------------------------------
# # to get values, must traverse through keys

# dict_4 = {
#     'ice_cream':{
#         'cho':2.99,
#         'van':3.99,
#         'oreo':5.99
#     }
# }
# print(dict_4['ice_cream']['oreo'])
# print(type(dict_4['ice_cream']))

# ----------------------------------------------------------------------------------------------

# from IPython.display import clear_output

# # Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?
# def addCart():
#     cart = {}
#     answer = '0'    
#     # while answer != 'quit':
#     answer = input("Do you want to : Show/Add/Delete or Quit?")
#         if answer == 'quit':
#             print(cart)
#             break
#         elif answer == 'show':
#             print(cart)
#             continue
        
#         elif answer == 'add':
#             item = input("What would you like to add? ")
#             num = input(f"How many {item}?")
#             for items, nums in cart.items()
#                 if item in cart:
#                     cart[item] = num + nums
#                 else:
#                     cart[item] = num            
#         elif answer == 'delete':
#             item = lower(input("What item would you like to delete? "
#             num = int(input(f"How many {item} do you want to KEEP?")
#             if num == 0:
#                 del cart[item]
#             else:
#                 cart[item] = num
#         else:
#             continue
        

# addCart()

# # ----------------------------------------------------------------------------------------------
# import re

# def isDigit(string):
#     #11ELF
#     strip = string.strip(" ")
#     pattern = re.compile('-\d+.\d+')
#     print(pattern)
#     # return strip.isdecimal()
 


# isDigit("3")
# isDigit("  3  ")
# isDigit("-3.23")
# isDigit("3-4")
# isDigit("  3   5")
# isDigit("3 5")
# isDigit("zero")

# # ----------------------------------------------------------------------------------------------
# Write a comparator for a list of phonetic words for the letters of the greek alphabet.
# A comparator is:
# a custom comparison function of two arguments (iterable elements) which should return a negative, zero or positive number depending on whether the first argument is considered smaller than, equal to, or larger than the second argument
# (source: https://docs.python.org/2/library/functions.html#sorted)
# The greek alphabet is preloded for you as greek_alphabet:

# greek_alphabet = (
#     'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
#     'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
#     'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
#     'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')

# def greek_comparator(lhs, rhs):
# # the tuple greek_alphabet is defined in the global namespace

#     index1 = greek_alphabet.index(lhs)
#     index2 = greek_alphabet.index(rhs)
#     if index1 < index2:
#         return -1
#     if index1 == index2:
#         return 0
#     if index1 > index2:
#         return 1

# greek_comparator('alpha', 'beta') #  <  0
# greek_comparator('psi', 'psi')     # == 0
# greek_comparator('upsilon', 'rho')  #>  0

# # ----------------------------------------------------------------------------------------------
# # Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

# def bool_to_word(boolean):
#     # TODO
    
#     if  boolean == True:
#         return "Yes"
#     elif boolean == False:
#         return "No"

# print(bool_to_word(True))
# print(bool_to_word(False))



# # # ----------------------------------------------------------------------------------------------
# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# def digitize(n):
#     nstr = str(n)
#     output = []
#     for i in nstr:
#         output.insert(0,i)
#     return output

# print(digitize(35231))


# # # ----------------------------------------------------------------------------------------------
# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
# If the input array is empty or null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

# def count_positives_sum_negatives(arr):
#     #your code here
#     pos = 0 
#     neg = 0
#     if arr == []:
#         output = []
#     else:
#         for i in arr:
#             if i > 0:
#                 pos +=1
#             elif i < 0: 
#                 neg += i
#         output = [pos, neg]

#     return output


# print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
# print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
# print(count_positives_sum_negatives([1]))
# print(count_positives_sum_negatives([-1]))
# print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]))
# print(count_positives_sum_negatives([]))




# # # ----------------------------------------------------------------------------------------------
# You're in the casino, playing Roulette, going for the "1-18" bets only and desperate to beat the house and so you want to test how effective the Martingale strategy is.

# You will be given a starting cash balance and an array of binary digits to represent a win or a loss as you play: 0 for loss and 1 for win.

# You should create a function martingale to return the balance after playing all rounds.

# You start with a stake of 100 dollars(unit of cash). If you lose a round, you lose the stake placed on that round and double the stake for your next bet. When you win, you win 100% of the stake and revert back to staking 100 dollars on your next bet.

# Example

# martingale(1000, [1, 1, 0, 0, 1]) === 1300
# you win your 1st round: gain $100, balance = 1100
# win 2nd round: gain $100, balance = 1200
# lose 3rd round: lose $100 dollars, balance = 1100
# double stake for 4th round and lost: staked $200, lose $200, balance = 900
# double stake for 5th round and won: staked $400 won $400, balance = 1300

# NOTE: Your balance is allowed to go below 0 (debt) :(





# # ---------------------------------------------------------------------------------------------
# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
# my attempts
# def max_sequence(arr):
#     onlyNeg = sorted(arr)
#     if onlyNeg[-1] < 0:
#         return 0
#     substart = 0
#     prev = 0
#     for i in range(len(arr)-1):
#         new = arr[i]
#         current = prev + arr[i]
#         if new > prev:
#             substart = i
#             subend = i
#             prev = new
#             current = new
#         elif prev > current:
#             subend = i
        
#     return arr[substart:subend+1]
# # CLosest I got
# def max_sequence(arr):
    
#     onlyNeg = sorted(arr)
#     if onlyNeg[-1] < 1 or len(onlyNeg) == 0:
#         return 0
#     current = 0
#     total = []
#     for i in range(1,len(arr)-1):
#         a = arr[i-1]
#         b = arr[i]
#         past = current
#         if past == current and past != 0:
#             total.append(arr[i])
#         current = arr[i-1] + arr[i]
#         if current > past:
#             total.append(arr[i])
#     high = sum(total)    
#     return high

# # print(max_sequence([-2,-1,-3,-4,-5,-3,-4]))
# print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# # Correct!
# def max_sequence(arr):
#     onlyNeg = sorted(arr)
#     if len(onlyNeg) == 0 or onlyNeg[-1] < 1:
#         return 0
#     max=0 
#     now=0 
#     for i in range(len(arr)):
#         now = now + arr[i]
#         if max < now:
#             max = now
#         if now < 0:
#             now = 0
#     return max


# # Most stripped down
# def maxSequence(arr):
#     max,curr=0,0
#     for x in arr:
#         curr+=x
#         if curr<0:curr=0
#         if curr>max:max=curr
#     return max





# print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(max_sequence([-2,-1,-3,-4,-5,-3,-4]))



# # # ----------------------------------------------------------------------------------------------





# # ---------------------------------------------------------------------------------------------
# # Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

# # Examples
# # Valid arrays
# # a = [121, 144, 19, 161, 19, 144, 19, 11]  
# # b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# # comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

# # a = [121, 144, 19, 161, 19, 144, 19, 11] 
# # b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# # Invalid arrays
# # If we change the first number to something else, comp may not return true anymore:

# # a = [121, 144, 19, 161, 19, 144, 19, 11]  
# # b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
# # comp(a,b) returns false because in b 132 is not the square of any number of a.

# # a = [121, 144, 19, 161, 19, 144, 19, 11]  
# # b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
# # comp(a,b) returns false because in b 36100 is not the square of any number of a.

# # Remarks
# # a or b might be [] (all languages except R, Shell).
# # a or b might be nil or null or None or nothing (except in Haskell, Elixir, C++, Rust, R, Shell, PureScript).
# # If a or b are nil (or null or None), the problem doesn't make sense so return false.

# # Note for C
# # The two arrays have the same size (> 0) given as parameter in function comp.

# def comp(a, b):
#     if a == None or b == None:
#         return False
#     if sum(b) < sum(a):
#         a2 = b
#         b = a
#         a = b
#     return bool(sorted(list(map(lambda x: x**2, a))) == sorted(b))
    
    
    
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# a = [-121, -144, 19, -161, 19, -144, 19, -11]
# print(comp(a,b))

# shortest
# def comp(a1, a2):
#     return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)

# # also good
# def comp(array1, array2):
#     try:
#         return sorted([i ** 2 for i in array1]) == sorted(array2)
#     except:
#         return False


# # # ----------------------------------------------------------------------------------------------
# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

# Create a function which translates a given DNA string into RNA.

# For example:

# "GCAT"  =>  "GCAU"
# The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.
# def dna_to_rna(dna):
#     return dna.replace('T','U')



# # ---------------------------------------------------------------------------------------------
# # In this kata, we will make a function to test whether a period is late.
# # Our function will take three parameters:
# # last - The Date object with the date of the last period
# # today - The Date object with the date of the check
# # cycleLength - Integer representing the length of the cycle in days
# # If the today is later from last than the cycleLength, the function should return true. We consider it to be late if the number of passed days is larger than the cycleLength. Otherwise return false.

# # mine
# from datetime import date
# from datetime import timedelta
# def period_is_late(last,today,cycle_length):
#     tdelta = timedelta(days=(cycle_length))
#     print(tdelta)
#     late = last + tdelta
#     if today > late:
#         return True
#     else:
#         return False



# # best
# def period_is_late(last, today, cycle_length):
#     return (today - last).days > cycle_length

# print(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35))


# # # ----------------------------------------------------------------------------------------------
# You will be given a sphere with radius(r). Imagine that sphere gets cut with flat surface, in this case the figure that is made with this cut is circle. 
# You will also be given distance(h) between centres of sphere and circle.Your task is to return the area of the original sphere,area of circle and perimeter of circle, 
# all of them rounded to 3 decimal places and order must be same as in the description.
# Not correct
# from math import pi
# from math import sqrt
# def stereometry(r,h):
#     print((r , h))
#     h2 = h**2
#     a = 2*r*h-h2
#     cR = sqrt(a)
#     cA = round((3.141*(cR**2)),3)
#     cP = round((2*3.141*cR),3)
#     sA = round((4*3.141*r**2),3)
#     return (sA, cA, cP)
    
    
# print(stereometry(3,2))
    
    
# print(stereometry(2,1))



# # # ---------------------------------------------------------------------------------------------
# SCHEDULE YOUR DA(RRA)Y

# The best way to have a productive day is to plan out your work schedule. Given the following three inputs, please create an an array of time alloted to work, broken up with time alloted with breaks:

# Input 1: Hours - Number of hours available to you to get your work done!
# Input 2: Tasks - How many tasks you have to do througout the day
# Input 3: Duration (minutes)- How long each of your tasks will take to complete

# Criteria to bear in mind:

# Your schedule should start with work and end with work.
# It should also be in minutes, rounded to the nearest whole minute.
# If your work is going to take more time than you have, return "You're not sleeping tonight!"
# # mine:
# def day_plan(hours, tasks, duration):
#     #your code here
#     at = tasks * duration
#     tb = (hours*60) - at
#     plan = []
#     if tb < 0:
#         return "You're not sleeping tonight!"
#     elif tasks == 0:
#         return plan
#     elif tasks == 1:
#         plan = [duration]
#     else:
#         plan = [duration]
#         bt = round(tb/(tasks-1))
#         for i in range(tasks-1):
#             plan.append(bt)
#             plan.append(duration)
#     return plan

# # Best
# def day_plan(hours, tasks, duration):
#     breaks = (hours * 60 - tasks * duration) / (tasks - 1) if tasks > 1 else 0
#     if breaks < 0:
#         return "You're not sleeping tonight!"
#     return ([duration, round(breaks)] * tasks)[:-1]


# day_plan(8,5,30)
# day_plan(3,5,60)
# day_plan(2,2,60)


# # # ------------------------------------------------------------------------------------------
# def add(num1, num2):
#     final = ''
#     n1 = (str(num1))[::-1]
#     n2 = (str(num2))[::-1]

#     if len(n2) > len(n1):
#         dif = len(n2)-len(n1)
#         for  d in range(dif):
#             n1 = n1 + "0"
#     elif len(n1) > len(n2):
#         dif = len(n1)-len(n2)
#         for  d in range(dif):
#             n2 = n2 + "0"
#     count = n1
#     for i in range(len(count)):
#         final= str((int(n1[i]) + int(n2[i]))) + final
#     print(final)
#     return final

# #------------------
# def add(a,b):
#     s = ""
#     while a+b:
#         a,p = divmod(a,10)
#         b,q = divmod(b,10)
#         s = str(p+q)+s
#     return int(s or'0')
# ----------------------

    
# add(2,11)
# add(16,18)
# add(26,39)
# add(122,81)
# add(13, 128)





# # ---------------------------------------------------------------------------------------------
# def twoNumberSum(array, targetSum):
#     # Write your code here.
#     answer = []
#     anser2 = []
#     for i in range(len(array)):
#         j = i+1
#         for j in range((i+1),len(array)):
#             if (array[i] + array[j]) == targetSum:
#                 answer.append(array[i])
#                 answer.append(array[j])
#     return answer
    
# # print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
# print(twoNumberSum([4, 11, -1, 6], 10))

# # # ----------------------------------------------------------------------------------------------
# # mine
# def isValidSubsequence(a, b):
#     if len(b) > len(a):
#         return False        
#     for i in range(len(b)):
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

# # theirs1
# def isValidSubsequence(a, s):
#     arrIdx = 0
#     seqIdx = 0
#     while arrIdx < len(a) and seqIdx < len(s):
#         if a[arrIdx] == s[seqIdx]:
#             seqIdx += 1
#         arrIdx +=1
#     return seqIdx == len(s)

# # theirs2
# def isValidSubsequence(a, s):
#     seqIdx = 0
#     for value in array:
#         if seqIdx == len(s):
#             break
#         if s[seqIdx] == value:
#             seqIdx +=1
#     return seqIdx == len(s)

 
 
# print(isValidSubsequence( [1,1,6,1], [1,1,1,6]))
# print(isValidSubsequence( [5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 22, 6, -1, 8, 10]))




# # ---------------------------------------------------------------------------------------------
# # mine
# def findClosestValueInBst(tree, target):
#     # Write your code here.
# 	close = float('inf')
# 	return closest(tree, target, close)
# def closest(bst,t,c):
# 	if bst is None:
# 		return c
# 	if abs(t-c) > abs(t - bst.value):
# 		c = bst.value
# 	if t < bst.value:
# 		return closest(bst.left, t, c)
# 	elif t > bst.value:
# 		return closest(bst.right, t, c)
# 	else:
# 		return c

# # Algo1 is like mine
# #Algo2 
# def findClosestValueInBst(tree, target):
#     # Write your code here.
# 	return closest(tree, target, tree.value)

# def closest(bst,t,c):
#     currentNode = bst 
#     while currentNode is not None:
#         if abs(t - c) > abs(t - currentNode.value):
#             c = currentNode.value
#         if t < currentNode.value:
#             currentNode = currentNode.left
#         elif t > currentNode.value:
#             currentNode = currentNode.right
#         else:
#             break
#     return c


# # This is the class of the input tree. Do not edit.
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# {
#   "tree": {
#     "nodes": [
#       {"id": "10", "left": "5", "right": "15", "value": 10},
#       {"id": "15", "left": "13", "right": "22", "value": 15},
#       {"id": "22", "left": null, "right": null, "value": 22},
#       {"id": "13", "left": null, "right": "14", "value": 13},
#       {"id": "14", "left": null, "right": null, "value": 14},
#       {"id": "5", "left": "2", "right": "5-2", "value": 5},
#       {"id": "5-2", "left": null, "right": null, "value": 5},
#       {"id": "2", "left": "1", "right": null, "value": 2},
#       {"id": "1", "left": null, "right": null, "value": 1}
#     ],
#     "root": "10"
#   },
#   "target": 12
# }


# {
#   "tree": {
#     "nodes": [
#       {"id": "100", "left": "5", "right": "502", "value": 100},
#       {"id": "502", "left": "204", "right": "55000", "value": 502},
#       {"id": "55000", "left": "1001", "right": null, "value": 55000},
#       {"id": "1001", "left": null, "right": "4500", "value": 1001},
#       {"id": "4500", "left": null, "right": null, "value": 4500},
#       {"id": "204", "left": "203", "right": "205", "value": 204},
#       {"id": "205", "left": null, "right": "207", "value": 205},
#       {"id": "207", "left": "206", "right": "208", "value": 207},
#       {"id": "208", "left": null, "right": null, "value": 208},
#       {"id": "206", "left": null, "right": null, "value": 206},
#       {"id": "203", "left": null, "right": null, "value": 203},
#       {"id": "5", "left": "2", "right": "15", "value": 5},
#       {"id": "15", "left": "5-2", "right": "22", "value": 15},
#       {"id": "22", "left": null, "right": "57", "value": 22},
#       {"id": "57", "left": null, "right": "60", "value": 57},
#       {"id": "60", "left": null, "right": null, "value": 60},
#       {"id": "5-2", "left": null, "right": null, "value": 5},
#       {"id": "2", "left": "1", "right": "3", "value": 2},
#       {"id": "3", "left": null, "right": null, "value": 3},
#       {"id": "1", "left": "-51", "right": "1-2", "value": 1},
#       {"id": "1-2", "left": null, "right": "1-3", "value": 1},
#       {"id": "1-3", "left": null, "right": "1-4", "value": 1},
#       {"id": "1-4", "left": null, "right": "1-5", "value": 1},
#       {"id": "1-5", "left": null, "right": null, "value": 1},
#       {"id": "-51", "left": "-403", "right": null, "value": -51},
#       {"id": "-403", "left": null, "right": null, "value": -403}
#     ],
#     "root": "100"
#   },
#   "target": 100
# }
# # # ----------------------------------------------------------------------------------------------
# # Mine like there's
# def branchSums(root):
#     # Write your code here.
# 	sumList = []
# 	bstSums(root, 0, sumList)
# 	return sumList
	
	
# def bstSums(node, runSum, sumList):
# 	if node is None:
# 		return
# 	newRunSum = runSum + node.value
# 	if node.left is None and node.right is None:
# 		sumList.append(newRunSum)
# 		return
# 	bstSums(node.left, newRunSum, sumList)
# 	bstSums(node.right, newRunSum, sumList)	


# # This is the class of the input root. Do not edit it.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
# {
#   "tree": {
#     "nodes": [
#       {"id": "1", "left": "2", "right": "3", "value": 1},
#       {"id": "2", "left": "4", "right": "5", "value": 2},
#       {"id": "3", "left": "6", "right": "7", "value": 3},
#       {"id": "4", "left": "8", "right": "9", "value": 4},
#       {"id": "5", "left": "10", "right": null, "value": 5},
#       {"id": "6", "left": null, "right": null, "value": 6},
#       {"id": "7", "left": null, "right": null, "value": 7},
#       {"id": "8", "left": null, "right": null, "value": 8},
#       {"id": "9", "left": null, "right": null, "value": 9},
#       {"id": "10", "left": null, "right": null, "value": 10}
#     ],
#     "root": "1"
#   }
# }







# # ---------------------------------------------------------------------------------------------
# # mine
# def generate_hashtag(s):
#     if len(s) < 1:
#         return False
#     s = s.title()
#     s = s.split()
#     hashs = "#"
#     for i in s:
#         hashs += (i)
#     if len(hashs) > 140:
#         return False
#     else:
#         return hashs

# # ans1
# def generate_hashtag(s):
#     ans = '#'+ str(s.title().replace(' ',''))
#     return s and not len(ans)>140 and ans or False
# #ans2
# def generate_hashtag(s):
#     output = "#"
    
#     for word in s.split():
#         output += word.capitalize()
    
#     return False if (len(s) == 0 or len(output) > 140) else output



# print(generate_hashtag(" Hello there thanks for trying my Kata"))

# # # ----------------------------------------------------------------------------------------------
# # mine
# def make_readable(seconds):
#     min, sec = divmod(seconds, 60) 
#     hour, min = divmod(min, 60) 
#     return "%02d:%02d:%02d" % (hour, min, sec) 

# # ans
# def make_readable(s):
#     return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)


        
        
        
# print(make_readable(0))
# print(make_readable(5))
# print(make_readable(60))
# print(make_readable(3759))
# print(make_readable(359999))




# # ---------------------------------------------------------------------------------------------
# # Mine:
# def validBraces(s):
#     check = []
#     for i in range(len(s)):
#         if s[i] is '(' or s[i] is '[' or s[i] is '{':
#             check.append(s[i])
#         else:
#             if len(check) is 0:
#                 return False
#             last = check[-1]
#             if (s[i] is ']' and last is '[') or (s[i] is ')' and last is '(') or (s[i] is '}' and last is '{'):
#                 check.pop()
#             else:
#                 break
#     return (len(check) is 0)

# # codewars1
# def validBraces(string):
#     braces = {"(": ")", "[": "]", "{": "}"}
#     stack = []
#     for character in string:
#         if character in braces.keys():
#             stack.append(character)
#         else:
#             if len(stack) == 0 or braces[stack.pop()] != character:
#                 return False
#     return len(stack) == 0 
# # codewars2
# def validBraces(s, previous = ''):
#   while s != previous: previous, s = s, s.replace('[]','').replace('{}','').replace('()','')
#   return not s

# print(validBraces("(){}[]"))
# print(validBraces("([{}])"))
# print(validBraces("(}"))
# print(validBraces("[({})](]"))

# # ---------------------------------------------------------------------------------------------
# # Breaking a simple cipher
# def key(code):
#     letter_count = count(code)


#     cipher = ''

#     return cipher
# def count(code):
#     letter_count = {}
#     for char in code:
#         if char not in letter_count:
#             letter_count[char] = 1
#         else:
#             letter_count[char] += 1
#     print(letter_count)
#     return letter_count
        

# passage = "Lars Porsena of Clusium, by the Nine Gods he swore That the great house of Tarquin should suffer wrong no more. By the Nine Gods he swore it, and named a trysting day, And bade his messengers ride forth, East and West and South and North, To summon his array. East and West and South and North the messengers ride fast, And tower and town and cottage have heard the trumpet's blast. Shame on the false Etruscan who lingers in his home, When Porsena of Clusium is on the march for Rome!"
# print(key(passage))


# # ---------------------------------------------------------------------------------------------
# Leaderboard climbers
# In this kata you will be given a leaderboard of unique names for example:

# ['John', 
#  'Brian',
#  'Jim',
#  'Dave',
#  'Fred']
# Then you will be given a list of strings for example:

# ['Dave +1', 'Fred +4', 'Brian -1']
# Then you sort the leaderboard.

# The steps for our example would be:

# # Dave up 1
# ['John',
#  'Brian',
#  'Dave',
#  'Jim',
#  'Fred']
# # Fred up 4
# ['Fred',
#  'John',
#  'Brian',
#  'Dave',
#  'Jim']
# # Brian down 1
# ['Fred',
#  'John',
#  'Dave',
#  'Brian',
#  'Jim']
# Then once you have done this you need to return the leaderboard.

# All inputs will be valid. All strings in the second list will never ask to move a name up higher or lower than possible eg. 'John +3' could not be added to the end of the second input list in the example above.

# The strings in the second list will always be something in the leaderboard followed by a space and a + or - sign followed by a number.
# mine:
# def leaderboard_sort(leaderboard, changes):
#     for m in changes:
#         x  = m.split()
#         person = x[0]
#         if person in leaderboard:
#             newIndex = (leaderboard.index(person))+(int(x[1])*-1)
#             leaderboard.remove(person)
#             leaderboard.insert(newIndex, person)            
#     return leaderboard

# codewars1:
# def leaderboard_sort(leaderboard, changes):
#     for change in changes:
#         name, delta = change.split()
#         idx = leaderboard.index(name)
#         leaderboard.insert(idx - int(delta), leaderboard.pop(idx))
#     return leaderboard



# print(leaderboard_sort(['John', 'Brian', 'Jim', 'Dave', 'Fred'], ['Dave +1', 'Fred +4', 'Brian -1']))
# # ---------------------------------------------------------------------------------------------
# In this Kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.

# solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
# --we sort by highest frequency to lowest frequency. If two elements have same frequency, we sort by increasing value
# # mine
# def solve(arr):
#     print(arr)
#     count = {}
#     ans = []
#     for i in arr:
#         if i not in count:
#             count[i]= 1
#         else:
#             count[i] += 1
#     count = {k: v for k, v in sorted(count.items(), key=lambda items: items[1], reverse=True)}
#     for x in count:
#         for y in range(len(arr)):
#             if arr[y] is x:
#                 ans.append(x)
#     return ans

# print(solve([5, 9, 6, 9, 6, 5, 9, 9, 4, 4]))
# print(solve([4, 4, 2, 5, 1, 1, 3, 3, 2, 8]))



# # ---------------------------------------------------------------------------------------------
# # In this Kata, you will be given a series of times at which an alarm goes off. Your task will be to determine the maximum time interval between alarms. Each alarm starts ringing at the beginning of the corresponding minute and rings for exactly one minute. The times in the array are not in chronological order. Ignore duplicate times, if any.

# # For example:
# # solve(["14:51"]) = "23:59". If the alarm goes off now, it will not go off for another 23 hours and 59 minutes.
# # solve(["23:00","04:22","18:05","06:24"]) == "11:40". The max interval that the alarm will not go off is 11 hours and 40 minutes.
# # In the second example, the alarm goes off 4 times in a day.

# # More examples in test cases. Good luck!
# # mine
# from datetime
# def solve(arr):
#     if len(arr) < 1:
#         return "There are no alarms set."
#     if len(arr) < 2:
#         return "23:59"
#     sleep = ''
#     arr = sorted(arr)
#     app.append((datetime.timedetla(arr[0]+
#     for y in range(len(arr)-1):
#         a = datetime.strptime(arr[y],'%I:%M)
#         b = datetime.strptime(arr[y+1], '%I:%M)
#         nap = b - a
#         if nap > sleep:
#             sleep = nap    
#     return sleep



# print(solve(["21:14", "15:34", "14:51", "06:25", "15:30"]))
# print(solve(["14:51"]))
# # ---------------------------------------------------------------------------------------------
# # Instructions
# Output
# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

# Example:

# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas
# The code would be called like so:

# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"
# # mine 
# def solution(string,markers):
#     string = string.splitlines()
#     found = ''
#     for i in range(len(string)):
#         for j in range(len(markers)):
#             x = string[i]
#             y = markers[j]
#             if y in x:
#                 found = x.index(y)
#                 # found = string[i].index(markers[j])
#                 if found >= 0:
#                     string[i] = (string[i][:found]).rstrip()
#         # string[i] = string[i].rstrip()    
    
#     return '\n'.join(string)

# # mine stripped
# def solution(string,markers):
#     string = string.splitlines()
#     for i in range(len(string)):
#         for j in range(len(markers)):
#             if markers[j] in string[i]:
#                 found = string[i].index(markers[j])
#                 if found >= 0:
#                     string[i] = (string[i][:found]).rstrip()
    
#     return '\n'.join(string)

# # codewars answer
# def solution(string,markers):
#     parts = string.split('\n')
#     for s in markers:
#         parts = [v.split(s)[0].rstrip() for v in parts]
#     return '\n'.join(parts)


# print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
# print(solution("a #b\nc\nd $e f g", ["#", "$"]))





# # ---------------------------------------------------------------------------------------------
# # We want to create a function that will add numbers together when called in succession.

# # add(1)(2);
# # // returns 3
# # We also want to be able to continue to add numbers to our chain.

# # add(1)(2)(3); // 6
# # add(1)(2)(3)(4); // 10
# # add(1)(2)(3)(4)(5); // 15
# # and so on.

# # A single call should return the number passed in.

# # add(1); // 1
# # We should be able to store the returned values and reuse them.

# # var addTwo = add(2);
# # addTwo; // 2
# # addTwo + 5; // 7
# # addTwo(3); // 5
# # addTwo(3)(5); // 10
# # We can assume any number being passed in will be valid whole number.
# # mine:
# def add(*args):
#     return sum(args)

# # codewars:
# class add(int):
#     __call__ = lambda self, value: add(self + value)



# print(add(1))
# print(add(1)(2))
# print(add(1)(2)(3))




# # ---------------------------------------------------------------------------------------------
# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:


# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

# mine
# def snail(array):    
#     final = []
#     n = len(array)
#     nsq = n*n
#     rLen = n
#     cLen = n
#     rStart = 0
#     cStart = 0
#     count = 0
#     n_count = 0
#     if not array[0]:
#         return []
#     while True:
#         ##  right
#         for c in range(cStart, cStart + rLen):
#             final.append(array[rStart][c])
#             count += 1
#             n_count += 1
#             if n_count >= nsq: return final
#         cStart += (count - 1)
#         rStart += 1
#         cLen -= 1
#         count = 0
#         ##  down
#         for r in range(rStart, rStart + cLen):
#             final.append(array[r][cStart])
#             count += 1
#             n_count += 1
#             if n_count >= nsq: return final
#         rStart += (count - 1)
#         cStart -= 1
#         count = 0
#         rLen -= 1
#         ## left
#         for c in range(cStart, cStart - rLen, -1):
#             final.append(array[rStart][c])
#             count += 1
#             n_count += 1
#             if n_count >= nsq: return final
#         cStart -= (count - 1)
#         rStart -= 1
#         cLen -= 1
#         count = 0
#         ## up
#         for r in range(rStart, rStart - cLen, -1):
#             final.append(array[r][cStart])
#             count += 1
#             n_count += 1
#             if n_count >= nsq: return final
#         rStart -= (count - 1)
#         cStart += 1
#         count = 0
#         rLen -= 1

# # codewars 1
# def snail(array):
#     ret = []
#     if array and array[0]:
#         size = len(array)
#         for n in xrange((size + 1) // 2):
#             for x in xrange(n, size - n):
#                 ret.append(array[n][x])
#             for y in xrange(1 + n, size - n):
#                 ret.append(array[y][-1 - n])
#             for x in xrange(2 + n, size - n + 1):
#                 ret.append(array[-1 - n][-x])
#             for y in xrange(2 + n, size - n):
#                 ret.append(array[-y][n])
#     return ret


# # codewars 2
# import numpy as np

# def snail(array):
#     m = []
#     array = np.array(array)
#     while len(array) > 0:
#         m += array[0].tolist()
#         array = np.rot90(array[1:])
#     return m

# # codewars 3
# # my implementation/explanation of the solution by foxxyz
# def snail(array):
#   if array:
#     # force to list because zip returns a list of tuples
#     top_row = list(array[0])
#     # rotate the array by switching remaining rows & columns with zip
#     # the * expands the remaining rows so they can be matched by column
#     rotated_array = zip(*array[1:])
#     # then reverse rows to make the formerly last column the next top row
#     rotated_array = rotated_array[::-1]
#     return top_row + snail(rotated_array)
#   else:
#     return []


# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# print(snail(array))
# # ---------------------------------------------------------------------------------------------
# Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

# The keypad has the following layout:

# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
# He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

# He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

# * possible in sense of: the observed PIN itself and all variations considering the adjacent digits

# Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

# Detective, we are counting on you!

# For C# user: Do not use Mono. Mono is too slower when run your code.


# # mine:
# from itertools import product

# def get_pins(observed):
#     near = {
#     '1': ['1', '2', '4'],
#     '2': ['1', '2', '3', '5'],
#     '3': ['2', '3', '6'],
#     '4': ['1', '4', '5', '7'],
#     '5': ['2', '4', '5', '6', '8'],
#     '6': ['3', '5','6', '9'],
#     '7': ['4','7', '8'],
#     '8': ['5', '7','8', '9', '0'],
#     '9': ['6', '8','9'],
#     '0': ['0','8']
#     }
#     x = [near [i] for i in observed]
#     y = list(product(*x))
#     combos = [''.join(i) for i in y]
#     return combos
# # codewars 1
# from itertools import product

# ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

# def get_pins(observed):
#     return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]


# # codewars2
# def get_pins(observed):
#   map = [['8','0'], ['1','2','4'], ['1','2','3','5'], ['2','3','6'], ['1','4','5','7'], ['2','4','5','6','8'],
#          ['3','5','6','9'], ['4','7','8'], ['5','7','8','9','0'], ['6','8','9']]
#   return map[int(observed[0])] if len(observed) == 1 else [x + y for x in map[int(observed[0])] for y in get_pins(observed[1:])]


# # ---------------------------------------------------------------------------------------------
# def alternatingSort(a):
#     b = []
#     ascend = True
#     while len(a) > 0:
#         b.append(a.pop(0))
#         if len(a) > 0:
#             b.append(a.pop(-1))
#         else:
#             break
#     for i in range(len(b)-1):
#         c = b[i]
#         d = b[1+1]
#         if b[i] > b[i+1]:
#             ascend = False
#             break
#         else:
#             continue
#     print(b)
#     return ascend





# a = [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]

# alt(a)

# # ---------------------------------------------------------------------------------------------
# import math
# def century(y):
#     # c  = 0
#     # if y % 100 == 0:
#     #     c = math.floor(y/100)
#     # else:
#     #     c = math.(y/100)
#     return math.ceil(y/100)
    
# century(98)
# century(100)
# century(1001)

# # ---------------------------------------------------------------------------------------------
# def checkPalindrome(inputString):
#     z = inputString
#     x = True
#     for i in range(0,(round(len(z)/2)),1):
#         if z[i] != z[-1-i]:
#             x = False
#             break
#     return x
    
    
# checkPalindrome("racecar")

# # ---------------------------------------------------------------------------------------------
# def ele(x):
#     output = -1000
#     for i in range(len(x)-1):
#         if x[i] * x[i+1] > output:
#             output = x[i] * x[i+1]
#     return output
    
# x = [-23, 4, -3, 8, -12]
# ele(x)


# # ---------------------------------------------------------------------------------------------
# def shapeArea(n):
#     return ((n**2) + ((n-1)**2))

# # ---------------------------------------------------------------------------------------------
# def makeArrayConsecutive2(s):
#     s.sort()
#     more = 0
#     for i in range(len(s)-1):
#         a = s[i]
#         b= s[i+1]
#         if s[i]+1 != s[i+1]:
#             more += ((s[i+1]) - (s[i]+1))
#     return more
    

# s = [6, 2, 3, 8]
# makeArrayConsecutive2(s)


# # ---------------------------------------------------------------------------------------------
# def almost(s):
#     count = 0
#     for i in range(len(s)-1):
#         if s[i] >= s[i+1]:
#             count +=1
#             a = bool((i + 2 < len(s)) and (s[i+2] <= s[i]))
#             b = bool((i -1 >= 0) and (s[i+1] <= s[i-1]))
#             if (a and b) or (count > 1):
#                 return False
#     return True
    
# s= [1, 1, 2, 3, 4, 4]

# almost(s)

# # ---------------------------------------------------------------------------------------------
import math
def get_middle(s):
    #your code here
    if len(s) % 2 ==0:
        return f"{s[int((len(s)/2)-1)]}{s[int((len(s)/2))]}"
    else:
        return f"{s[math.floor(len(s)/2)]}"

s = "of"
get_middle(s)

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

