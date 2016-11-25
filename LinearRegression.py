#!usr/bin/python

import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

# Reading data
s1_data = pd.read_csv('Data/Mens_height_weight.csv')

# Plotting the data as a scatter plot
fig, ax = plt.subplots(1, 1)
ax.scatter(s1_data['Height'], s1_data['Weight'])
ax.set_xlabel('Height')
ax.set_ylabel('Weight')
plt.show()

# To check the Pearson correlation between the 2 variables 
print s1_data.corr()

# Generating a Linear Regression model with weight as the dependent and height as independent 
## Creating a Linear Regression model
lm = linear_model.LinearRegression()

## Training the model using the training set
lm.fit(s1_data.Height[:, np.newaxis], s1_data.Weight)

print "Intercept is {0}".format(lm.intercept_)
print "Coefficient value of the height is {0}".format(lm.coef_)
print pd.DataFrame(zip(s1_data.columns, lm.coef_),
					columns = ['features', 'estimatedCoefficients'])

# Plotting the graphical view
fig, ax = plt.subplots(1, 1)
ax.scatter(s1_data.Height, s1_data.Weight)
ax.plot(s1_data.Height, lm.predict(s1_data.Height[:, np.newaxis]), 
			color = 'red')
ax.set_xlabel('Height')
ax.set_ylabel('Weight')
plt.show()