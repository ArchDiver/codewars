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





# # ---------------------------------------------------------------------------------------------





# # # ----------------------------------------------------------------------------------------------





# # ---------------------------------------------------------------------------------------------







# # # ----------------------------------------------------------------------------------------------





# # ---------------------------------------------------------------------------------------------





# # # ----------------------------------------------------------------------------------------------





# # ---------------------------------------------------------------------------------------------





# # # ----------------------------------------------------------------------------------------------





# # ---------------------------------------------------------------------------------------------





# # # ----------------------------------------------------------------------------------------------





# # ---------------------------------------------------------------------------------------------