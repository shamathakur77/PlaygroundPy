# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

#from subprocess import check_output
#print(check_output(["ls", "../Downloads/GitHub/PlaygroundPy/reported.csv"]).decode("utf8"))

data=pd.read_csv('../Downloads/GitHub/PlaygroundPy/reported.csv')

data.info()

data.corr()

#correlation map
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()

data.head(10)

data.columns
#Index(['Year', 'crimes.total', 'crimes.penal.code', 'crimes.person', 'murder',
 #      'assault', 'sexual.offenses', 'rape', 'stealing.general', 'burglary',
  #     'house.theft', 'vehicle.theft', 'out.of.vehicle.theft', 'shop.theft',
   #    'robbery', 'fraud', 'criminal.damage', 'other.penal.crimes',
    #   'narcotics', 'drunk.driving', 'population'],
     # dtype='object')

#matplotlib
# Line Plot
# color = color, label = label, linewidth = width of line, 
#alpha = opacity, grid = grid, linestyle = sytle of line

data.Year.plot(kind = 'line', color = 'g', label = 'Year', linewidth=1, alpha = 0.5, grid = True, linestyle = ':')


data.fraud.plot(kind = 'line', color = 'g', label = 'Fraud', linewidth=1, alpha = 0.5, grid = True, linestyle = ':')


data.assault.plot(kind = 'line', color = 'b', label = 'assault', linewidth=1, alpha = 0.5, grid = True, linestyle = ':')


data.rape.plot(color = 'r',label = 'rape',linewidth=1, alpha = 0.5,grid = True,linestyle = '-.')

plt.legend(loc='upper right')

plt.xlabel('x axis')

plt.ylabel('y axis')

plt.title('Line Plot of crimes in Sweden over the years')

plt.show()

# Scatter Plot -- population and assault
# x = attack, y = defense
data.plot(kind='scatter', x='population', y='assault',alpha = 0.5,color = 'red')
plt.xlabel('population')              # label = name of label
plt.ylabel('assault')
plt.title('Sweden Crime Scatter Plot')            # title = title of plot
Text(0.5,1,'Sweden Crime Scatter Plot')


# Scatter Plot -- year and assault
# x = attack, y = defense
data.plot(kind='scatter', x='Year', y='assault',alpha = 0.5,color = 'red')
plt.xlabel('Year')              # label = name of label
plt.ylabel('assault')
plt.title('Sweden Crime Scatter Plot')            # title = title of plot
Text(0.5,1,'Sweden Crime Scatter Plot')

data.columns

# Histogram
# bins = number of bar in figure
data.assault.plot(kind = 'hist',bins = 50,figsize = (12,12))
plt.show()

# clf() = cleans it up again you can start a fresh
data.Speed.plot(kind = 'hist',bins = 50)
plt.clf()
# We cannot see plot due to clf()
