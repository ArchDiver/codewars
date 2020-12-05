## practice answers
##--------------------------------------------------------------------------------
"""
Example

For a = [10, 2], the output should be concatenationsSum(a) = 1344.

a[0] ∘ a[0] = 10 ∘ 10 = 1010,
a[0] ∘ a[1] = 10 ∘ 2 = 102,
a[1] ∘ a[0] = 2 ∘ 10 = 210,
a[1] ∘ a[1] = 2 ∘ 2 = 22.
So the sum is equal to 1010 + 102 + 210 + 22 = 1344.

For a = [8], the output should be concatenationsSum(a) = 88.

There is only one number in a, and a[0] ∘ a[0] = 8 ∘ 8 = 88, so the answer is 88.

For a = [1, 2, 3], the output should be concatenationsSum(a) = 198.

a[0] ∘ a[0] = 1 ∘ 1 = 11,
a[0] ∘ a[1] = 1 ∘ 2 = 12,
a[0] ∘ a[2] = 1 ∘ 3 = 13,
a[1] ∘ a[0] = 2 ∘ 1 = 21,
a[1] ∘ a[1] = 2 ∘ 2 = 22,
a[1] ∘ a[2] = 2 ∘ 3 = 23,
a[2] ∘ a[0] = 3 ∘ 1 = 31,
a[2] ∘ a[1] = 3 ∘ 2 = 32,
a[2] ∘ a[2] = 3 ∘ 3 = 33.
The total result is 11 + 12 + 13 + 21 + 22 + 23 + 31 + 32 + 33 = 198.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

A non-empty array of positive integers.

Guaranteed constraints:
1 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ 106.

[output] integer64

The sum of all a[i] ∘ a[j]s. It's guaranteed that the answer is less than 253.
"""
# def concatenationsSum(a):
#     t=sum(a)
#     t1=t*len(a)
#     t2=sum([t*[len(str(x))-1 for x in a].count(j)*10**(j+1) for j in range(7)])
#     return t1+t2

## my first attempt. Need to cut time.
# def concatenationsSum(a):
#     final = []
#     for i in range(len(a)):
#         j = i
#         for j in range(len(a)):
#             final.append(int(str(a[i])+str(a[j])))
#     return sum(final)

## my second attempt
# def concatenationsSum(a):
#     sum1 = sum(a)
#     sum2 = 0
#     sum3 = (len(a) - 1) * sum1
#     for i in a:
#         sum2 += int(str(sum1) + str(i))
#     return sum2 + sum3
##third stripped bare
def concatenationsSum(a):
    return sum(int(str(sum(a)) + str(i)) for i in a) + ((len(a) - 1) * sum(a))


##--------------------------------------------------------------------------------
"""
Given an integer n and an array a of length n, your task is to apply the following mutation to an: Array a mutates into a new array b of length n.
For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].

So, the resulting array after the mutation will be [4, 5, -1, 2, 1].

Input/Output

[execution time limit] 3 seconds (java)
[input] integer n

An integer representing the length of the given array.

Guaranteed constraints:
1 ≤ n ≤ 103.

[input] array.integer a

An array of integers that needs to be mutated.

Guaranteed constraints:
a.length = n,
-103 ≤ a[i] ≤ 103.

[output] array.integer
The resulting array after the mutation.

Preciousorekha1 avatar
Example

For n = 5 and a = [4, 0, 1, -2, 3], the output should be mutateTheArray(n, a) = [4, 5, -1, 2, 1].

b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 =
"""
# def mutateTheArray(n, a):
#     return [a[0]+a[1]]+[sum(a[x-1:x+2])for x in range(1,len(a))]if n>1 else a

##First
# def mutateTheArray(n,a):
#     b = []
#     if len(a) < 2:
#         return a
#     for i in range(n):
#         if i == 0:
#             b.append((0 + (a[i]) + (a[i+1])))
#         if i == (n-1):
#             b.append((a[i-1] + a[i] + 0))
#         elif i != n-1 and i != 0:
#             b.append((a[i-1] + a[i] + a[i + 1]))
#     return b
## Second
# def mutateTheArray(n, a):
#     if n>1:
#         b = [a[0]]
#         for i in range(1,n):
#             b.append(sum(a[i-1:i+2]))
#         return b
#     else:
#         return a
## Third
# def mutateTheArray(n, a):
#     if n>1:
#         b = [sum(a[i-1:i+2])for i in range(1,n)] 
#         return [a[0]+a[1]] + b
#     else:
#         return a
## Fourth
# def mutateTheArray(n, a):
    # if n>1:
    #     return [a[0]+a[1]] + [sum(a[i-1:i+2])for i in range(1,n)] 
    # else:
    #     return a 
## Final
def mutateTheArray(n, a):
    return [a[0]+a[1]] + [sum(a[i-1:i+2])for i in range(1,n)] if n>1 else a 


n = 5
a = [4, 0, 1, -2, 3]

mutateTheArray(n,a)


##--------------------------------------------------------------------------------
"""
You are given two arrays of integers a and b of the same length, and an integer k. We will be iterating through array a from left to right, and simultaneously through array b from right to left, and looking at pairs (x, y), where x is from a and y is from b. Such a pair is called tiny if the concatenation xy is strictly less than k.

Your task is to return the number of tiny pairs that you'll encounter during the simultaneous iteration through a and b.

Example

For a = [1, 2, 3], b = [1, 2, 3], and k = 31, the output should be
countTinyPairs(a, b, k) = 2.

We're considering the following pairs during iteration:

(1, 3). Their concatenation equals 13, which is less than 31, so the pair is tiny;
(2, 2). Their concatenation equals 22, which is less than 31, so the pair is tiny;
(3, 1). Their concatenation equals 31, which is not less than 31, so the pair is not tiny.
As you can see, there are 2 tiny pairs during the iteration, so the answer is 2.

For a = [16, 1, 4, 2, 14], b = [7, 11, 2, 0, 15], and k = 743, the output should be
countTinyPairs(a, b, k) = 4.

We're considering the following pairs during iteration:

(16, 15). Their concatenation equals 1615, which is greater than 743, so the pair is not tiny;
(1, 0). Their concatenation equals 10, which is less than 743, so the pair is tiny;
(4, 2). Their concatenation equals 42, which is less than 743, so the pair is tiny.
(2, 11). Their concatenation equals 211, which is less than 743, so the pair is tiny;
(14, 7). Their concatenation equals 147, which is less than 743, so the pair is tiny.
There are 4 tiny pairs during the iteration, so the answer is 4.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

An array of non-negative integers.

Guaranteed constraints:
0 ≤ a.length ≤ 105,
0 ≤ a[i] ≤ 104.

[input] array.integer b

An array of non-negative integers.

Guaranteed constraints:
b.length = a.length,
0 ≤ b[i] ≤ 104.

[input] integer k

An integer to compare concatenated pairs with.

Guaranteed constraints:
0 ≤ k ≤ 109.

[output] integer

The number of tiny pairs during the iteration.
"""
# def countTinyPairs(a, b, k):
#     return sum([1 if int(str(x)+str(y))<k else 0for x,y in zip(a,b[::-1])])

##first
# def countTinyPairs(a, b, k):
#     pairs = []
#     for i in range(len(a)):
#         x = len(b) - i - 1
#         pair = int(f'{a[i]}{b[x]}')
        
#         if pair < k:
#             pairs.append(pair)
#     return len(pairs)

## Second
# def countTinyPairs(a, b, k):
#     pairs = []
#     for i in range(len(a)):      
#         if int(f'{a[i]}{b[(len(b)-1-i)]}') < k:
#             pairs.append(int(f'{a[i]}{b[(len(b)-1-i)]}'))
#     return len(pairs)
##Third
# def countTinyPairs(a, b, k):
#     pairs = []
#     for i,j in zip(a,b[::-1]):      
#         if int(f'{i}{j}') < k:
#             pairs.append(int(f'{i}{j}'))
#     return len(pairs)
##Fourth
def countTinyPairs(a, b, k):
    pairs = sum([1 if int(f'{i}{j}')<k else 0 for i,j in zip(a,b[::-1])])     
    return pairs
        
        
a= [1, 2, 3]
b= [1, 2, 3]
k= 31
countTinyPairs(a, b, k)

##--------------------------------------------------------------------------------
"""
You are given an array of arrays a. Your task is to group the arrays a[i] by their mean values, so that arrays with equal mean values are in the same group, and arrays with different mean values are in different groups.

Each group should contain a set of indices (i, j, etc), such that the corresponding arrays (a[i], a[j], etc) all have the same mean. Return the set of groups as an array of arrays, where the indices within each group are sorted in ascending order, and the groups are sorted in ascending order of their minimum element.

Example

For

a = [[3, 3, 4, 2],
     [4, 4],
     [4, 0, 3, 3],
     [2, 3],
     [3, 3, 3]]
the output should be

meanGroups(a) = [[0, 4],
                 [1],
                 [2, 3]]
mean(a[0]) = (3 + 3 + 4 + 2) / 4 = 3;
mean(a[1]) = (4 + 4) / 2 = 4;
mean(a[2]) = (4 + 0 + 3 + 3) / 4 = 2.5;
mean(a[3]) = (2 + 3) / 2 = 2.5;
mean(a[4]) = (3 + 3 + 3) / 3 = 3.
There are three groups of means: those with mean 2.5, 3, and 4. And they form the following groups:

Arrays with indices 0 and 4 form a group with mean 3;
Array with index 1 forms a group with mean 4;
Arrays with indices 2 and 3 form a group with mean 2.5.
Note that neither

meanGroups(a) = [[0, 4],
                 [2, 3],
                 [1]]
nor

meanGroups(a) = [[0, 4],
                 [1],
                 [3, 2]]
will be considered as a correct answer:

In the first case, the minimal element in the array at index 2 is 1, and it is less then the minimal element in the array at index 1, which is 2.
In the second case, the array at index 2 is not sorted in ascending order.
For

a = [[-5, 2, 3],
     [0, 0],
     [0],
     [-100, 100]]
the output should be

meanGroups(a) = [[0, 1, 2, 3]]
The mean values of all of the arrays are 0, so all of them are in the same group.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer a

An array of arrays of integers.

Guaranteed constraints:
1 ≤ a.length ≤ 100,
1 ≤ a[i].length ≤ 100,
-100 ≤ a[i][j] ≤ 100.

[output] array.array.integer

An array of arrays, representing the groups of indices.
"""
# def meanGroups(a):
#     d,e=[],[]
#     for i,j in enumerate(a):
#         if sum(j)/len(j)not in e:
#             e+=[sum(j)/len(j)]
#             d+=[[i]]
#         else:
#             d[e.index(sum(j)/len(j))]+=[i]
#     return d


##--------------------------------------------------------------------------------
# def alternatingSort(a):
#     c,l=0,a[0]
#     while c!=(len(a)-1)//2:
#         c=-c if c<0 else -c-1
#         if a[c]<=l:
#             return False
#         l=a[c]
#     return True
# # ---------------------------------------------------------------------------------------------
##first
# def alternatingSort(a):
#     b = []
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
#             return False   
#         else:
#             continue
#     print(b)
#     return True
## second
def alternatingSort(a):
    b, x = 0, a[0]
    while b != (len(a)-1)//2:
        if b < 0:
            b=-b
        else:
            b = -b-1
        if a[b] < x:
            return False
        x = a[b]
    return True
            





# a = [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]

# alt(a)

##--------------------------------------------------------------------------------
# def mergeStrings(s1, s2):
#     s,o1,o2='',s1,s2
#     while len(s1)*len(s2)!=0:
#         if o1.count(s1[0])>o2.count(s2[0]) or (o1.count(s1[0])==o2.count(s2[0]) and s1[0]>s2[0]):
#             s+=s2[0]
#             s2=s2[1:]
#         else:
#             s+=s1[0]
#             s1=s1[1:]
#     return s+s1+s2


##--------------------------------------------------------------------------------
"""
6


2
I had the below problem in a coding test and I got 28/30 tests passes and 2 failed due to a time-out.

Problem
You have created a programming language and now you have decided to add hashmap support to it. It was found that in common programming languages, it is impossible to add a number to all hashmap keys/values. So, you have decided to implement your own hashmap in your new language with following operations.

insert x y - insert and object with key x and value y
get x - return the value of an object with key x
addToKey x - add x to all keys in map
addToValue y - add y to all values in map
Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations

For Example

For queryType=["insert","insert","addToValue","addToKey","get"] and query=[[1,2],[2,3],[2],[1],[3]], the output should be hashMap(queryType,query)=5.
Explanation

insert 1 2 - hashmap will be {1:2}
insert 2 3 - hashmap will be {1:2,2:3}
addToValue 2 - hashmap will be {1:4,2:5}
addToKey 1 - hashmap will be {2:4,3:5}
get 3 - value is 5
Input/Output

[execution time limit] 3 seconds (Java)
[input] array.string queryType
Array of query types. its is guaranteed that each queryType[i] any one of the above mentioned operation
1<=queryType.length<=10^5
[input] array.array.integer query
Array of queries, where each query is mentioned by 2 numbers for insert and one number for others Key values are in range [-10^9,10^9]
"""
# 
# def hashMap(queryType, query):
#     d,s,c1,c2={},0,0,0
#     for i,j in zip(queryType,query):
#         if i == 'insert':
#             d[j[0]-c1]=j[1]-c2
#         elif i == 'addToValue':
#             c2+=j[0]
#         elif i == 'addToKey':
#             c1+=j[0]
#         elif i== 'get':
#             s+=d[j[0]-c1]+c2
#     return s