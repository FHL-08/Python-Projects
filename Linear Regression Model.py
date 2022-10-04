# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:50:27 2021

@author: HP
"""
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit([[3],
               [4],
               [5],
               [6],
               [7],
               [8]] ,  [[5],
                        [6],
                        [7],
                        [8],
                        [9],
                        [10]])
                        
y_pred=regressor.predict([[15]])

from matplotlib import pyplot as plt
plt.figure("linear regression model")
plt.clf()
plt.plot([3,4,5,6,7,8],[5,6,7,8,9,10],"k-",label="linear")
plt.ylabel("dependent variable")
plt.xlabel("independent variable")
plt.legend(loc="upper left")


