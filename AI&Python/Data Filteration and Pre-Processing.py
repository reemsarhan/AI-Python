#Data Filteration and Pre-Processing


#Our Aim to 
#1-Removemissing values
#2-Remove duplicates
#3-text values
#4-outliers
#5-split (features, labels)

# Normal Reading File Data
import pandas as pd

# Read the data from CSV file
data = pd.read_csv('FileName.csv')
data.head()

# Insights from the data
# Example: Calculate total spent
data['total_spent'] = data['DailySpent'] + data['MonthlySpent'] + data['YearlySpent']
# Check for the new added column
data.head()

# Visualize the insight using Matplotlib
import matplotlib.pyplot as plt
plt.scatter(data['Profit'], data['total_spent'])
plt.xlabel('Profit')
plt.ylabel('Total Spent')
plt.title('Profit vs Total Spent')
plt.show()

# Making new DataFrame and grouping by the category you want
new_df = data[['Profit', 'Company']]
# Example: Group by Company
new_df.groupby(data['Company']).mean()

# Data Preprocessing

# Check for Null Values to remove them
data.isnull().sum()

# Drop Nulls
data = data.dropna()

# Drop Duplicates
data = data.drop_duplicates()

# One-hot encoding for categorical variables
x = pd.get_dummies(data)

# Check for outliers  
from scipy import stats

# Assuming 'data' is your DataFrame and 'numeric_column' is the column with numerical values
z_scores = stats.zscore(data['numeric_column'])
abs_z_scores = abs(z_scores)
filtered_entries = (abs_z_scores < 3)  # Setting a threshold of 3 standard deviations
data = data[filtered_entries]



# Split (features(Inputs), labels(Outputs))
from sklearn.model_selection import train_test_split

# Assuming 'x' is your features and 'y' is your target variable
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# What is numpy Lib?
# -->NumPy (Numerical Python) is a powerful Python library used for numerical computing.

import numpy as np

# Replace NaN values with the average value of the data
data['time'] = data['time'].replace(np.nan, data['time'].mean())

# Drop nulls
data = data.dropna()

# Replace string with int
data['Gender'] = data['Gender'].replace(['Male', 'Female'], [1, 0])
