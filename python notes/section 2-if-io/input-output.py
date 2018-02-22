
# coding: utf-8

# In[ ]:

'''
Input and output functions

1. stdout using print
2. formatted printing
3. stdin using 

'''


# In[ ]:

# number.zfill(n) will put zeros so that the 
# total number of digits in the number is n 
# if the number has a negative in front then the negative sign 
# is also accounted for.
'314'.zfill(10)


# In[ ]:

'-3.14'.zfill(10)


# In[ ]:

# formatted printing
print '{0} and {1}'.format('san jose','santa clara')


# In[ ]:

print '{0} and {1}'.format('san jose') # fails as we need to provide two values


# In[ ]:

print '{0}'.format('san jose','santa clara') 
# the first value in the list will be printed


# In[ ]:

print '{nearcity} and {farcity}'.format(farcity='Sacramento',nearcity='San jose')


# In[ ]:

import math 
print 'PI = {0:.5f}'.format(math.pi) # 0:.5 means 5 digits after decimal 
print 'PI = %0.5f'%(math.pi) # The () is optional for one input


# In[ ]:

a = 5
b = 3.25
print 'a = %d' %a


# In[ ]:

a = 5
b = 3.25
c = '5.6'
print 'a = %03d b = %0.2f c = %s' %(a,b,c)


# In[ ]:

a = 5.0
type(a)


# In[ ]:

f = open('/Users/sridevi/Desktop/Python_Fall/python_list.txt')
print f
for line in f.readlines():
    print line.strip


# In[ ]:

# Try change the path of the file()
f = open('/Users/sridevi/Desktop/python_list.txt')
print f
for line in f.readlines():
    print line.strip


# In[ ]:

'''
raw_input() gets input from the command line.
In this example, we are getting the input from the user and assigning it 
to variable s.
'''
s = raw_input('Enter a name : ')
print s


# In[ ]:

a = 'r'
b = str(2)
a+b


# In[ ]:

'''
Inclass activity: Create a txt file and write names of 10 states and close the file. Then open the file
and print each line. 
'''

