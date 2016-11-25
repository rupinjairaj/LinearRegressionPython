#!usr/bin/python

import numpy as numpy
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
s1_data = pd.read_csv('Data/Mens_height_weight.csv')
fig, ax = plt.subplots(1, 1)
ax.scatter(s1_data['Height'], s1_data['Weight'])
ax.set_xlabel('Height')
ax.set_ylabel('Weight')
plt.show()