import numpy as np
import pandas as pd

# Specify the number of row entries (rows) and columns (cols)
rows = 10

# Specify column names
column_names = ['H', 'A', 'Date', 'Column4', 'Column5']
cols = len(column_names)



# Specify the desired data type (float or double)
dtype = 'float'  # or dtype = 'double'

# Specify limits for the generated data
lower_limit = 0
upper_limit = 1

# Generate random floats or doubles within the specified limits for Column1
column1_data = np.random.uniform(lower_limit, upper_limit, size=(rows, 1))

# Set Column2 elements to be 1 minus the corresponding Column1 elements
column2_data = 1 - column1_data

# Concatenate Column1 and Column2 data to form the final data array
data = np.concatenate((column1_data, column2_data, np.random.uniform(lower_limit, upper_limit, size=(rows, cols-2))), axis=1)

# Round the data to a specific number of decimal points
decimal_points = 3  # Change this to the desired number of decimal points
data = np.round(data, decimal_points)

# Convert data to the desired data type (float or double)
if dtype == 'float':
    data = data.astype(np.float32)
elif dtype == 'double':
    data = data.astype(np.float64)
else:
    raise ValueError(f"Invalid data type '{dtype}'. Supported data types: 'float', 'double'")

# Create a DataFrame with the generated data and column names
df = pd.DataFrame(data, columns=column_names)

print(df)
