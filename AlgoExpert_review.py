import my_timer

def main(prog):
    t = my_timer.Timer()
    t.start()

    print(prog)

    t.stop()

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


# #--------------------------------------------------------------------------------
# # #  Tournament Winner

competitors = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]
results = [0, 0, 1]

def tournamentWinner1(competitions, results):
    win = 3
    final_winner = "fail"
    competitors_list = {}
    
    for i in range(len(competitions)):
        print(competitions[i][0], competitions[i][1])
        
        if competitions[i][0] not in competitors_list:
            competitors_list[competitions[i][0]] = 0
        if competitions[i][1] not in competitors_list:
            competitors_list[competitions[i][1]] = 0
            
        print(results[i])    
        if results[i] == 1:
            competitors_list[competitions[i][0]] = competitors_list[competitions[i][0]] + win
            print(competitors_list[competitions[i][0]])

        else:
            competitors_list[competitions[i][1]] = competitors_list[competitions[i][1]] + win
            print(competitors_list[competitions[i][1]])
        print(competitors_list)
    
    print(competitors_list)
    final = sorted(competitors_list.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
    print(final)
    final_winner = final[0]


    # Write your code here.
    return f"{final_winner}"


# print(tournamentWinner1(competitors, results))

#___Clean
def tournamentWinner2(competitions, results):
    win = 3
    competitors_list = {}
    
    for i in range(len(competitions)):
        # This check to make sure the lang is in the dict
        if competitions[i][0] not in competitors_list:
            competitors_list[competitions[i][0]] = 0
        if competitions[i][1] not in competitors_list:
            competitors_list[competitions[i][1]] = 0

        #This updates the winners scores    
        if results[i] == 1:
            competitors_list[competitions[i][0]] = competitors_list[competitions[i][0]] + win
        else:
            competitors_list[competitions[i][1]] = competitors_list[competitions[i][1]] + win

    # Write your code here.
    return (sorted(competitors_list.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))[0][0]


# tournamentWinner2(competitors, results)

#__Better 
def tournamentWinner3(competitions, results):
    # Ties only return the first winner.
    winner = ''
    rank = {winner: 0}
    for teams, result in zip(competitions, results):
        team = teams[0]  if result == 1 else teams[1]
        if team not in rank:
            rank[team] = 0
        rank[team] += 3
        if rank[team] > rank[winner]:
            winner = team
    return winner

main(tournamentWinner1(competitors, results))
main(tournamentWinner2(competitors, results))
main(tournamentWinner3(competitors, results))

# #--------------------------------------------------------------------------------
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


# if __name__ == '__main__':
#     main()