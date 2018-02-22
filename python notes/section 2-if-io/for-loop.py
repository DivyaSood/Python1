
# coding: utf-8

# In[ ]:

'''
Basic statements
1. if-else
2. while
3. for
4. for with range and xrange
'''


# In[ ]:

# Syntax of if-else
# if statement a:
#    execute statement(s) that are under this block
# else:
#    execute statement(s) that are under this block

x = int(raw_input("Please enter your choice (1-3): "))
if x < 0:
    print 'Negative number not allowed'
elif x == 0:
    print "Zero"
elif x == 1:
    print 'One'
elif x == 2:
    print 'Two'
elif x == 3:
    print 'Three'
else:
    print 'Number more than 3 not allowed'


# In[ ]:

'''
Truthiness in Python

https://www.udacity.com/wiki/cs258/truthiness-in-python

https://docs.python.org/release/2.5.2/lib/truth.html

'''


# In[ ]:

a = []
if a == []:
    print "No value"


# In[ ]:

a = []

if a:
    print a[0]
    print "Value"
else:
    print "No value"


# In[ ]:

a = [1]
if a==[]:
    print "No value"
else:
    print "Has value"


# In[ ]:

a = {}
if a == {}:
    print "No value"


# In[ ]:

a = None
if a == None:
    print "No value"


# In[ ]:

# Syntax of the for statement
# for each_item in something:
#     execute statement(s) that are under this block
fruits= ['apple', 'grapes', 'peach']
for f in fruits:
    print f


# In[ ]:

# range returns a list of values
# range(n) will return a list of values from 0 to n-1
print range(5)
for i in range(len(fruits)):
    print i,fruits[i]


# In[ ]:

# range(n1,n2) will return a list from n1 to n2-1
print range(2,9)


# In[ ]:

# range(n1,n2,incr) will return a list from n1 to n2-1 in steps of incr
print range(2,9,3)


# In[ ]:

# xrange creates an object with an iterator that returns the value on demand
# the demand is in the loop
for i in xrange(len(fruits)):
    print i, fruits[i]


# In[ ]:

# f is a filehandler
f = open('/Users/chityala/Dropbox/ucsc/Latest Notes/section2-if-io/python_list.txt')
# readlines reads one line at a time from the file
# Syntax filehandle.readlines()
for line in f.readlines():
    print line.strip() 
    # strip removes newline, carriage return, space etc at the beginning and at the end of the line
f.close()


# In[ ]:

'the    life  is    good   '.strip(' ')


# In[ ]:

';the    life  is    good   '.strip(';')


# In[ ]:

for i in range(len(fruits)):
   if i == 1:
        print "first fruit",i, fruits[i]
   elif i == 2:
        print "second fruit",i, fruits[i] 
   elif i == 3:
        pass 


# In[ ]:

a = range(5)
print a


# In[ ]:

a = range(5)
for i in a:
    print i


# In[ ]:

a = range(5)
count = 0
# Syntax of While
# While something is true:
#     execute statement(s) that are under this block 
while True:
    print a[count]
    count = count+1
    if count == len(a):
        break # this statement breaks out of the loop


# In[ ]:

for n in range(22, 30):
    if n % 3 == 0:
        print n, 'is the first multiple of 3'
        break
    else:
        print n, 'is not a multiple of 3'


# In[ ]:

for n in range(22, 30):
    if n % 4 == 0:
        print n, 'is a multiple of 4'
        continue
        print 'after'
    else:
        print n, 'is not a multiple of 4'


# In[ ]:

a = 1
for i in range(5):
    a *= (i+1)
print a,i


# In[ ]:

for item in []:
    pass # this statement will do nothing  

print item # Will give NameError. Why?


# In[ ]:

for item in [1]:
    pass 
print item


# In[ ]:

some_list = [1, 3, 6, -2, 5, 8]
print some_list


# In[ ]:

for items in some_list:
    if items < 0:
        # we are iterating through some_list until we hit the first negative number
        print items
        break


# In[ ]:

'''
Inclass activity:
Write a code that will take name from the user until the user decides to quit by entering q or Q. 
Also perform a check to see whether the user entered anything. If the user didn't enter anything, 
ask them to enter a name. 
'''

