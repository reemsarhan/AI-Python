# What is matplotlib?
#-->Matplotlib is a comprehensive library for creating static, animated, 
#   and interactive visualizations in Python. 

#Example 1
import matplotlib.pyplot as plt

# Assuming 'data' is a DataFrame containing columns 'ColumnName1' and 'ColumnName2'

x = data['ColumnName1']
y = data['ColumnName2']

# Creating a scatter plot
plt.scatter(x, y)

# Adding labels and title
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('My First Graph')

# Displaying the plot
plt.show()

#Example 2
import matplotlib.pyplot as plt

# Assuming 'data' is a DataFrame containing columns 'ColumnName1' and 'ColumnName2'

x = data['ColumnName1']
y = data['ColumnName2']

# Creating a line plot
plt.plot(x, y)

# Adding labels and title
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Line Plot')

# Displaying the plot
plt.show()

#Example 3
import matplotlib.pyplot as plt

# Assuming 'data' is a DataFrame containing columns 'ColumnName1' and 'ColumnName2'

x = data['ColumnName1']
y = data['ColumnName2']

# Creating a bar chart
plt.bar(x, y)

# Adding labels and title
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Bar Chart')

# Displaying the plot
plt.show()


#Example 4
import matplotlib.pyplot as plt

# Assuming 'data' is a DataFrame containing a column 'ColumnName'

# Creating a histogram
plt.hist(data['ColumnName'], bins=10)

# Adding labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')

# Displaying the plot
plt.show()

#Example 5
import matplotlib.pyplot as plt

# Assuming 'data' is a DataFrame containing a column 'ColumnName'

# Creating a pie chart
plt.pie(data['ColumnName'], labels=data.index, autopct='%1.1f%%')

# Adding a title
plt.title('Pie Chart')

# Displaying the plot
plt.show()

