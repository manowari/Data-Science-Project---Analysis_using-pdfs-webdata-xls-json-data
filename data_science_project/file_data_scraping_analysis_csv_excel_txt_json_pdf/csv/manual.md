# Working with CSV files 

## Importing Data 

1. Using `csv` module - simple but not suitable for complex manipulation


2. Using `panda's` `read_csv`

```python
import pandas as pd

# Specify the path to your CSV file
csv_file_path = 'path/to/your/file.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Now, you can access columns using column names
column_data = df['ColumnName']


```

**Saving a  df to CSV**
`df.to_csv(csv_file_path, index=False)
`


