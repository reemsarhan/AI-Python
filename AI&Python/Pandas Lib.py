#What is Pandas Library??
#--> Pandas is a powerful data manipulation library in Python.
# It provides data structures and functions to work with structured data.


# Importing the Pandas library and aliasing it as pd for easier usage.
import pandas as pd

# Reading data from a CSV file into a DataFrame.
data = pd.read_csv('filepath.csv')

# Displaying the DataFrame, showing its contents.
print(data)

# Indexing: Extracting a single column from the DataFrame.
output = data['ColumnName']

# Indexing with iloc: Extracting a subset of rows and columns.
# Here, it selects all rows and the first three columns (0:3).
inputs = data.iloc[:, 0:3]

# Selecting specific columns from the DataFrame.
new_data = data[['ColumnName1', 'ColumnName2']]

# Performing an operation on a column and storing the result in a new column.
data['NewColumnName'] = data['ColumnName'] * 1.1

# Saving the modified DataFrame to a new CSV file.
data.to_csv('NewFile.csv')

# Replacing specific values in a column with new values.
data['ColumnName'] = data['ColumnName'].replace(to_replace=['val1', 'val2', 'val3'], value=[1, 2, 3])

# Defining a function to convert values in a column and applying it to the entire column.
def convert(c):
    if c == 'France':
        return 1
    elif c == 'Spain':
        return 2
    elif c == 'Germany':
        return 3

data['Country'] = data['Country'].apply(convert)

# Counting the occurrences of unique values in a column.
value_counts = data['ColumnName'].value_counts()

# Checking for missing values in the DataFrame and counting them.
missing_values = data.isnull().sum()
