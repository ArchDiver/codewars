## practice answers
##--------------------------------------------------------------------------------
# def concatenationsSum(a):
#     t=sum(a)
#     t1=t*len(a)
#     t2=sum([t*[len(str(x))-1 for x in a].count(j)*10**(j+1) for j in range(7)])
#     return t1+t2

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

def mutateTheArray(n,a):
    b = []
    if len(a) < 2:
        return a
    for i in range(len(a)-1):
        if i == 0:
            b[0] = 0 + a[i] + a[a+1]
        if i == len(a):
            b[(len(a))] = a[i-1] + a[i] + 0
        elif i != len(a) and i != 0:
            b[i] = a[i-1] + a[i] + a[i + 1]
    return b 
        


n = 5
a = [4, 0, 1, -2, 3]

mutateTheArray(n,a)


##--------------------------------------------------------------------------------
# def countTinyPairs(a, b, k):
#     return sum([1 if int(str(x)+str(y))<k else 0for x,y in zip(a,b[::-1])])

##--------------------------------------------------------------------------------
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