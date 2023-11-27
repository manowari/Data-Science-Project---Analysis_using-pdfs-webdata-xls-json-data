
# Some Python Notes 

## Working with Files. 

- Converting windows file paths  to Normal use `os.path`
    1. If using `""` have double slash -windows_path = `"C:\\Users\\Username\\Documents\\file.txt"``
    2. If you want a single`\` - use a rawstring `r` eg  `windows_path = r"C:\Users\Username\Documents\file.txt"
    3. joining paths `full_path = os.path.join(path1, path2, filename)
`

```python
def convert_windows_path_to_python(windows_path):
    # Use os.path.normpath to convert the Windows path to Python format
    python_path = os.path.normpath(windows_path)
    return python_path
```


  **Using Data frames** `import pandas as pd
`
  - You can convert data to data frame using  `df = pd.DataFrame(data)
` assuming your usuing `{}` Dictionary or Set

  - Getting all columns `# Get a list of all column names
column_names = df.columns.tolist()`
 -  using `dtypes` to know the nature of the columns
     - Assign types to column
     ```python 
     # Get data types of all columns
    column_data_types = df.dtypes

     # Initialize lists to store column types
    numerical_columns = []
    categorical_columns = []
    other_columns = []

    # Iterate through columns and categorize them
    for column, data_type in column_data_types.items():
        if pd.api.types.is_numeric_dtype(data_type):
            numerical_columns.append(column)
        elif pd.api.types.is_categorical_dtype(data_type):
            categorical_columns.append(column)
        else:
            other_columns.append(column)
```

**Missing Data**
 -  Showing missing data 
    ````# Display the number of missing entries in each column
        missing_data = df.isnull().sum()
        print("Number of Missing Entries:\n", missing_data)
```
- Dealng with Missing Data 
        1. Dropping Rows or Columns:
          - ```python
        # Drop rows with any missing values
        df_cleaned_rows = df.dropna()

        # Drop columns with any missing values
        df_cleaned_columns = df.dropna(axis=1)```
        2. Filling:
        `# Fill missing values with the mean of the column
        df_filled_mean = df.fillna(df.mean())

`       3. Interpolation:
        `# Interpolate missing values 
        df_interpolated = df.interpolate()



`
 **Shape and General Analysis**

- DataFrame Shape:

Use the shape attribute to get the dimensions of the DataFrame.
 

`# Display the shape of the DataFrame
print("DataFrame Shape:", df.shape)`

- Summary Statistics:
Use the `describe()` method to get summary statistics for numerical columns.
 
`# Display summary statistics for numerical columns
print("Summary Statistics:\n", df.describe())`

- Value Counts:

Use the value_counts() method to get the count of unique values in a column.
 

`# Display value counts for a specific column
print("Value Counts:\n", df['ColumnName'].value_counts())`


** Saving Models **

Its good practice to save your models 








 