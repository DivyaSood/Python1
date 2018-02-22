#importing of Python Modules Required
import csv
import matplotlib.pyplot as plt
'''%matplotlib inline''' #used to print graph in notebook    
import numpy as np
from sklearn import linear_model
import re
lm=linear_model.LinearRegression()
#Main Code
lst=[]
lst1=[]
lst4=[]
lst5=[]
input_file=csv.DictReader(open("HousepricesinCalifornia2.csv"))
for line in input_file:
    lst.append(line['Alameda'])
    lst1.append(line['Mon-Yr'])
    lst4.append(line['Butte'])
    lst5.append(line['Mon-Yr'])
    print line['Alameda']
    print line['Butte']
print lst
print lst1
print lst4
print lst5
lst2 = [re.sub("[a-zA-Z$,]", "", elem) for elem in lst]
lst6 = [re.sub("[a-zA-Z$,]", "", elem) for elem in lst4]
print lst2
print lst6
lst3=[]
lst7=[]
for x in range(len(lst1)):
    lst3.append(x)
print lst3
for x in range(len(lst5)):
    lst7.append(x)
print lst7
x= np.asarray(lst2)
y= np.asarray(lst3)
x= np.asarray(lst6)
y= np.asarray(lst7)
'''new_x = np.reshape(x, (1, len(x)))
print new_x
lm.fit(new_x,y)'''
print x
print y
#Plotting of Graph
plt.subplot(2,1,1)                   
plt.scatter(lst3,lst2, color='blue')
plt.title('House prices in Alameda ')
plt.xlabel('Mon-Yr(1990-2016)')
plt.ylabel('House prices($)')
plt.subplot(2,1,2)
plt.scatter(lst7,lst6,color='red')
plt.title('House prices in Butte ')
plt.xlabel('Mon-Yr(1990-2016)')
plt.ylabel('House prices ($)')
plt.show()