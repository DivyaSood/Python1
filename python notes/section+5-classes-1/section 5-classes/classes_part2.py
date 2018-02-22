
# coding: utf-8

# In[ ]:

'''
In this notebook we will discuss the following:
1) Operator overloading
2) Abstract classes
3) Proxy design pattern
4) Factory design pattern
'''


# In[5]:

'''
Operator overloading: The assignment of more than one function to a 
particular operator.

https://docs.python.org/2/reference/datamodel.html
'''

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
   
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)
    

v1 = Vector(5,8)
v2 = Vector(5,-2)
print v1+ v2


# In[ ]:

'''

Abstract classes are used to define a signature that will be implemented 
by all the classes that inherit it. For example, let us say that two 
programming groups have to read and write into files but how they read and 
write method may differ. In such cases we can have read and write method 
signature in the abstract class and the two groups can inherit from the 
abstract class and create their own concrete classes.
'''


# In[1]:

# This is an example of an abstract class without importing any special 
# module
class AbstractImage():
    def read(self):
        raise NotImplementedError()
    def write(self):
        raise NotImplementedError()
'''
Here the abstract class AbstractImage has the methods that consist of 
signature that all the child classes will inherit. We are raising not 
implemented error to say that the methods by themselves are not doing 
anything until implemented by a child class.
'''        

ai = AbstractImage()
print ai
ai.read()


# In[4]:

class AbstractDicom():
    
    def read(self):
        raise NotImplementedError()
    def write(self):
        raise NotImplementedError()
    
class Dicom(AbstractDicom):
    def read(self):
        print "reading file in the child class"
        
d = Dicom()
print d
d.read() # Makes the call to Dicom child class
#d.write() 
'''
First makes the call to Dicom child class. But since this is not 
implemented in the child class the write method in the parent class 
will be called and 'NotImplementedError' will be raised.
'''


# In[3]:

class AbstractDicom():
    def read(self):
        raise NotImplementedError()
    def write(self):
        raise NotImplementedError()
    
class Dicom(AbstractDicom):
    def read(self):
        print "reading file"
    def write(self):
        print "writing file"
        
d = Dicom()
print d
d.read() # Makes the call to Dicom child class
d.write() # Makes the call to Dicom child class


# In[ ]:

'''
Create an abstract class called 'InterestCal'. Create a child class called 
'CICal'. The 'CICal' class will inherit the abstract class and implement 
compound interesst calculator. The formula is finalval = P(1+(r/n)^(years*n) 
where n is the number of times the amount is compounded annually.

This child class will have three methods:
1) __init__ method
2) a method called compcal that computes the compound interest 
3) a method called compout that prints the compounded value.


Once all classes have been defined, then call to calculate and print the amount. 
The user should pass the attributes Principal, years, interestrate, n when the 
class is instanstiated. 

Follow the code below:

c = CICal(1000,5,6,2) 
c.compcal()
print c.compout()

In the code below, the principal amount is 1000, the number of years is 5, the 
interest rate is 6%, and n = 2. 
'''


# In[ ]:



