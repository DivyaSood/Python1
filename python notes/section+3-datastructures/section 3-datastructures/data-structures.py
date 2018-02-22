
# coding: utf-8

# In[ ]:

'''
Data Structures

1. List
2. Dictionary
3. tuples
4. sets
5. strings
6. slicing lists and tuples
7. List comprehension
https://docs.python.org/2/tutorial/datastructures.html
'''    


# In[ ]:

# Syntax for list is n = [item1, item2, item3].  The items can be any Python object
# the index of the list starts from zero
mylist = [1,2,"CA",[3,4]]  # mylist is a collection of numbers, string and a list
print mylist


# In[ ]:

mylist[0] # this returns the first element in mylist


# In[ ]:

mylist[-2] # this returns the last but one element in mylist


# In[ ]:

mylist[-1][-2]


# In[ ]:

# mylist[a:b] will return elements with index starting from a up to b-1. 
# This process is called Slicing
mylist[0:2]


# In[ ]:

print mylist[-1][1] #this is used to get elements from a list of list


# In[ ]:

# append will add a value to the end of the list
mylist.append(3.14) 
print mylist


# In[ ]:

# Pop removes an element at the given index
print mylist.pop(2)
print mylist


# In[ ]:

# Insert adds an element at the given index
mylist.insert(2,"MN")
print mylist


# In[ ]:

print mylist[1]


# In[ ]:

mylist = ['couple','3','3a',1,5,2,2.4,'c','0'] # note '3' is a string
a = mylist.sort()
# print a, mylist
print a 
print mylist 


# In[ ]:

# sort() function will sort the list in ascending order. 
# If reverse = True is specified then it will sort the list on descending order
mylist.sort(reverse=True)
print mylist


# In[ ]:

# for list of lists, sort command sorts the lists with respect to the first element 
# in the lists
a = [[10,3],[5,2]]
a.sort()
print a


# In[ ]:

b = [['q', 'a'], ['dog','cat']]
b.sort()
print b


# In[ ]:

mylist = [2,3,2,5,6,6,6]
mylist.count(3) 
m = ['apple', 'cat', 'cat', 'sat']
m.count('cat')
#count will return the frequency of occurance of a particular value in the list


# In[ ]:

newlist = set(mylist)
print newlist, type(newlist)
newlist = list(set(mylist))
print newlist


# In[ ]:

d = dict(a=1, b=2, e=1, d=2, c=1, g=2, f=3)
print d
for items in d.iteritems():
    print items
a1 = {1:'a',2:'b'}
print a1


# In[ ]:

# EXTEND METHOD
mylist = [1,2,3]
newl = [4,5,6]
#mylist.append(newl)
mylist.extend(newl)
print mylist


# In[ ]:

mylist = [1,2,3]
bylist = mylist
mylist.extend([4,5,6])
print mylist
print bylist
#print "mylist extend",mylist_copy1
#print mylist,len(mylist)


# In[ ]:

# What is wrong with the next two statements?
mylist = [1,2,3]
mylist_copy = mylist
print mylist
print mylist_copy
mylist_copy.append([4,5,6])
#print "mylist append",mylist_copy
print mylist,len(mylist)
print mylist_copy,len(mylist_copy)
# len(object) will return the number of items of an object


# In[ ]:

'''
Note 1: mylist.append([4,5,6]) will add this list to the end of mylist. Whereas 
mylist.extend([4,5,6]) will add values 4, 5 and 6 to mylist.

Note 2: mylist_copy1 is a copy of mylist. Any changes to mylist_copy1 will also 
affect mylist because the copy we made is a shallow copy.
'''


# In[ ]:

#### DEEP COPY
mylist = [5,9,3]
mylist_copy2 = mylist[:]
mylist_copy2.append([11,2,3])
mylist.sort()
#mylist_copy2.sort()
print mylist
print mylist_copy2
#print "mylist append", mylist_copy2
#print mylist, len(mylist)


# In[ ]:

'''
Note: mylist_copy2 is a deep copy of mylist so any changes to mylist_copy2 will 
not affect mylist and vice versa.
'''


                # filter(), map(), and reduce()
                
# In[ ]:

for i in range(2,10):
    if i%2!=0:
        print i


# In[ ]:

# Get all odd numbers between 2 and 10
a = range(2,10)
print a

def f(x): 
    return x % 2 != 0

b = filter(f, a) 
# filter command takes two inputs one is a function and other one is iterable
# filter returns a list of values that satisfies the condition, 
# in this case it returns all the values between 2 and 9 that 
# are NOT divisible by 2. 
print b


# In[ ]:

# Get all odd numbers between 2 and 10 using LAMBDA FUNCTIONS
a = range(2,10)
b = filter(lambda x:x%2!=0, a) 
# We replaced the function f with a lambda function (also known as anonymous function)
# The lambda function needs to be read as follows
# The x to the left of the : is the argument to the function
# The expression x%2!=0 to the right of : is the operation being performed inside the function
# and also the value being returned by the function.
print b


# In[ ]:

def squared(x): 
    return x*x

print map(squared, range(1, 5)) 
'''
map command takes a function and iterable(s). In this case one input is 
the function and other input is the values. Map returns a list which is the 
output of the function. In this case it returns the squares of the values 
from 1 to 4. Map takes a set of values and returns another set of values 
based on the function.
'''


# In[ ]:

# LAMBDA function - anonymous functions
# lambda (input1, input2) : output
# An equivalent function is the squared function list above
print map(lambda x:x*x, range(1, 5)) 


# In[ ]:

# You can also give a name to the lambda function
lambdasq = lambda x:x*x
print map(lambdasq, range(1, 5)) 


# In[ ]:

a = [1,2,3]
b = [4,5,6]
def add(a1, b1): return a1+b1
map(add,a,b)
# here map takes two lists and adds them


# In[ ]:

# Reduce operation is used to shrink an iterable to a single value
# Find the sum of all elements in a list
a = [1,2,5]
reduce(lambda x,y: x+y, a)


# In[ ]:

a = [1,2,5]
reduce(lambda x,y: x*y , a)


# In[ ]:

## LIST COMPREHENSION


# In[ ]:

# traditional method
squares = []
for x in range(10):
    squares.append(x**2)
print squares


# In[ ]:

# smart method using list comprehension
squares = [x**2 for x in range(10)]
print squares


# In[ ]:

# an elaborate example of list comprehension which combines two lists and 
# returns a list of tuples
combined = [(x, y) for x in [1,2,3,4] for y in [3,1,4] if x != y and x>y]
print combined


# In[ ]:

'''
Tuple is a collection of immutable Python elements. That means we cannot 
delete, add or modify elements in a tuple. The syntax for a tuple is 
a = (item1,item2,item3,).  
'''


# In[ ]:

T1 = 1,2,'String'
# Here Python will automatically assumes T1 is a tuple
print T1


# In[ ]:

emptyTuple = ()
print emptyTuple


# In[ ]:

T2 = (1,2,)
# without the comma, T2 will be of type integer and not tuple
print T2,type(T2)


# In[ ]:

T2 = T2+1 # Not allowed, as tuple cannot be modified
print T2,type(T2)


# In[ ]:

T3 = T1,T2 # T3 is a tuple of tuples
print T3
print T3[0]
print T3[0][1] 
# 0 index indicates the first tuple and 1 index indicates the 
# second element in the first tuple


# In[ ]:

T3[0][0]=2 # New values cannot be assigned


# In[ ]:

t  = (1,2,3)
def squared(x): return x*x
map(squared, t) 
# map operation on a tuple. This returns a list. Note map function always 
# returns a list, even if the input is not a list. 


# In[ ]:

t  = (1,2,3)
print t,type(t)
l = list(t)
print l,type(l)
t2 = tuple(l)
print t2, type(t2)


# In[ ]:

B = (1,) # B is a tuple with one element
B = (1,2,) # a new tuple named B is created which has two elements
B = () # a new tuple named B is created with no elements
print B


# In[ ]:

A = (2,4,5,8,10,11)
B = ('CA', 'MN', 'TX')
C = A + B # + operation concatenates the tuples
print C


# In[ ]:

# Basic tuple operations
print len(A) 
print max(B)
print min(B)


# In[ ]:

# Basic tuple operations
H = ('Hello',)
print H*4 # * means repetition


# In[ ]:

# Basic tuple operations
serial1 = ('Belize','Costa Rica','Guatemala')
serial2 =['Ecuador', 'Belize','Nicaragua']
print cmp(serial1,serial1)
print cmp(serial1,serial2)
print tuple(serial1)


# In[ ]:

'''
Inclass activity: Consider the tuple t1 = (2,4,8). 
1. Try to modify the first element of the tuple to 5. 
2. Convert the tuple into a list and append the number 5 to the list
3. Use extend to add [1,4,5] to the list
4. Pop the third item from the list and then print the list.
5. Convert it back into a tuple. 
'''


# In[ ]:

'''
Dictionary is another useful data type built into Python is the dictionary 
(see Mapping Types — dict). Dictionaries are sometimes found in other languages 
as “associative memories” or “associative arrays”. Unlike sequences, which are 
indexed by a range of numbers, dictionaries are indexed by keys, 
which can be any immutable type; strings and numbers can always be keys. 
Tuples can be used as keys if they contain only strings, numbers, or tuples; 
if a tuple contains any mutable object either directly or indirectly, it cannot be 
used as a key. You can’t use lists as keys, since lists can be modified in place 
using index assignments, slice assignments, or methods like append() and extend(). 
https://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences
'''


# In[ ]:

ziploc = {}
print ziploc


# In[ ]:

# syntax for a dictionary is dict = {'key1': 'value1', 'key2': 'value2'}
# dict is a key-value pair
ziploc = {'95117': 'San Jose','94086':'Sunnyvale','95014': 'Cupertino'}
# in this example for key 95117, San Jose is the value, 
# for key 94086, Sunnyvale is the value
print ziploc
print ziploc.keys()
print tuple(ziploc.keys())
print ziploc.values()


# In[ ]:

print ziploc['95117']
ziploc['95117'] = 'Santa Clara'
print ziploc['95117']
ziploc['95054'] = 'Santa Clara'
print ziploc


# In[ ]:

for keys in ziploc:
    print keys,ziploc[keys]


# In[ ]:

for keys,value in ziploc.iteritems(): # Use .items() for version 3.0+
    print keys,value


# In[ ]:

ziploc['55421'] # Not allowed, as the dictionary does not have key 55421


# In[ ]:

exists = False
for k,v in ziploc.iteritems():
    if k == '95117':
        exists = True
        break
print exists


# In[ ]:

'55421' in ziploc


# In[ ]:

ziploc.items() # dict.items() returns a list of (key,value) tuple pairs


# In[ ]:

ziploc.values() #dict.values() returns the dictionary values


# In[ ]:

ziploc.clear() # removes all the elements of the dictionary
print ziploc


# In[ ]:

squared = {x: x**2 for x in range(5)}
# we are using dictionary comprehension 
print squared


# In[ ]:

mylist = [2,3,2,5,6,6,6]
mylist.count(3) 


# In[ ]:

countdict = {}
for items in newlist:
    countdict[items] = mylist.count(items)
print countdict


# In[ ]:

'''
Set - is a unordered collection of unique items
'''


# In[ ]:

vegetables = ['tomatoes','eggplant','cucumber','eggplant'] # A list
vegetables_set = set(vegetables)
# set command returns only unique items
print vegetables,vegetables_set


# In[ ]:

a = list(vegetables_set)
# vegetables_set[0] # Not allowed as set cannot be indexed. You can iterate 
# through them.
a[0]


# In[ ]:

for items in vegetables:
    print items 


# In[ ]:

for items in vegetables_set:
    print items 


# In[ ]:

print 'Cucumber' in vegetables_set 
# the above statement checks whether Cucumber is in vegetables_set


# In[ ]:

finallistofveg = list(vegetables_set)
print finallistofveg


# In[ ]:

a = [1,1,4,5,7]
print type(a), a
b = set(a)
c = list(b)
print c

list(set(a))


# In[ ]:

'''
From https://docs.python.org/2/library/sets.html, you can obtain a list of all operators that can 
be applied to sets
len(s): cardinality of set s
x in s: tests x for membership in s
x not in s: tests x for non-membership in s
s.issubset(t): <= t: test whether every element in s is in t
s.issuperset(t): s >= t: test whether every element in t is in s
s.union(t): s | t : new set with elements from both s and t
s.intersection(t): s & t : new set with elements common to s and t
s.difference(t): s - t : new set with elements in s but not in t
s.symmetric_difference(t) : s ^ t : new set with elements in either s or t but not both
s.copy(): new set with a shallow copy of s
'''


# In[ ]:

list1 = [1,2,3,45,76]
list2 = [2,3,45]
set1 = set(list1)
set2 = set(list2)
print set1,set2

print set1.union(set2)
print set1.intersection(set2)
print set1.difference(set2)
print 1 in set1 # Check if an element exists in a set using in keyword
print set1.issubset(set2) 


# In[ ]:



