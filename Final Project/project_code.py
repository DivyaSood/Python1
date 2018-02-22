#importing of Python Modules Required
import csv
import matplotlib.pyplot as plt
#%matplotlib inline    
import numpy as np
from sklearn import linear_model
import re
#function
def predict_price(Matrix1,y,lst8,subplotInstance,titleInstance):
    lm=linear_model.LinearRegression()
    plt.subplot(2,1,subplotInstance)
    lm.fit(Matrix1,y)
    x_test=[[0],[200],[341],[365]]
    y_predict=lm.predict(x_test)
    x_test2=[[365]]
    y_predict2=lm.predict(x_test2)
    print "Predited value after 4 years in " +  titleInstance ,y_predict2
    plt.scatter(lst8,y,color='blue')
    plt.plot(x_test,y_predict,color='red',linewidth=1.5)
    plt.title('House price for ' +  titleInstance)
    plt.ylabel('House prices($)')
#Main Code
lst1=[]
lst2=[]
lst3=[]
input_file=csv.DictReader(open("HousepricesinCalifornia2.csv"))
for line in input_file:
    lst1.append(line['Alameda'])
    lst2.append(line['Mon-Yr'])
    lst3.append(line['Butte'])
#print "House prices in Alameda=",lst1
#print "House price in Butte=",lst3
#use of regular expression
lst5 = [re.sub("[a-zA-Z$,]", "", elem) for elem in lst1] #removing of all the variables and special chracters
lst6 = [re.sub("[a-zA-Z$,]", "", elem) for elem in lst3] #removing of all the variables and special chracters
print "Formated List of Prices in Alameda = ",lst5 

print "Formated List Pf Prices In Butte = ",lst6

y1=np.array(lst5).astype(np.float)
y2=np.array(lst6).astype(np.float)
#print y1,y2

#use of list comprehension
lst7=[x for x in range (len(lst2))]
#print "month-yr of Alameda",lst7
lst8=[lst7]
print "Month-Year varriation on x-axis for both counties",lst8

x1= np.asarray(lst8)
#print x1

Matrix1=np.matrix.transpose(x1)
#print "value of Matrix1= ",Matrix1
#call function to predict future price
predict_price(Matrix1,y1,lst8,1, 'Alameda')
predict_price(Matrix1,y2,lst8,2, 'Butte')
plt.xlabel('Mon-yr(1990-2016)')
plt.show()
