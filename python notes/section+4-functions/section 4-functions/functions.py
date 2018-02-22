
# coding: utf-8

# In[ ]:

'''
Functions
1. Arguments and outputs
2. default argument
3. keyword based arguments

Syntax for function
def name_of_the_function(list of arguments):
    statements that need to be executed
    return value
'''


# In[ ]:

def increment(a):
    b = a+1
    print 'the increment value is : %d' %b
    return b

increment(20) # calling the function and passing a required argument. 


# In[ ]:

# Scope of variables is local to the function. 
def increment(a):
    b = a+1
    print 'the increment value is : %d' %b
    return b

increment(20) # calling the function and passing a required argument. 
#print b # The variable b does not exist outside the function.  So we will get NameError exception


# In[ ]:

# A function can take multiple inputs
def increment(a,incr):
    c = a+incr
    print 'The value of a is: %d' %a
    return c

increment(3,10) # calling the function and passing two required arguments. 
# 10 will be assigned to a and 
# 3 will be assigned to incr. So these are called positional arguments. 


# In[ ]:

def increment(a,incr):
    c = a+incr
    return (c,a,incr)
    # returning multiple values as a tuple
increment(10,3)


# In[ ]:

# Specifying default values
def increment(a,incr=1):
    a = a+incr
    return a

print increment(3) # for this the incr will default to 1
print increment(3,4) 
# here the incr is assigned a value of 4 which overrides the default value


# In[ ]:

def increment(a=4,incr1=1):
    print 'the value of a is :%d' %a
    a = a+incr1
    return a

print increment(a=6,incr1=2) # 2 keyword arguments 


# In[ ]:

print increment(incr1=2,a=3)
# Unlike positional arguments, order is not important for keyword arguments. 


# In[ ]:

print increment(10,incr1=5) #if you assign a value for a keyword argument 
# then other arguments to its right should also be assigned values.


# In[ ]:

print increment(a=10,5) # This will generate a Syntax error


# In[ ]:

print increment(5,incr1=2) 
# if you assign a value for a keyword argument 
# then other keyword arguments to its right should also be assigned values. 


# In[ ]:

type(increment)
increment


# In[ ]:

# Pass by value or pass by reference
# http://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference


# <img src="http://i.stack.imgur.com/hKDcu.png">

# In[ ]:

def myfunc(a):# a is an int
    a = a*2
    print a
    return a
b = 2
myfunc(b)
print b


# In[ ]:

def myfunc(a):# a is a TUPLE that is completely replaced
    a = (4, 5, 6,)
    print a
    return a
b = (1,2,3)
myfunc(b)
print b


# In[ ]:

def myfunc(a):# a is a list that is completely replaced
    a = [4,5,6]
    print a
    return a
b = [1,2,3]
myfunc(b)
print b


# In[ ]:

def myfunc(a):# a is a LIST that is modified inline
    a.append(4)
    print a
    return a
b = [1,2,3]
myfunc(b)
print b


# In[ ]:

def myfunc(a):# a is a LIST that is modified inline
    a = a[:] # Creating a deepcopy will solve the problem of pass by reference
    a.append(4)
    print a
    return a
b = [1,2,3]
myfunc(b)
print b


# In[ ]:

'''
In-class activity

Create a function called squared which takes a list called mylist and returns 
another list where the elements are square of mylist. Also write another 
function that takes mylist and returns a dictionary where the key is the input 
and the value is the square of the input. 
'''
mylist = [2, -7, 10]


# In[ ]:



