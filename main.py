import pandas as pd
from database import DB  

# Step 1: Connect to the database
conn = DB.get_connect()
cur = conn.cursor()

# Step 2: Read file from user input
file_path = input("Enter the file path (CSV or Excel): ")

# Step 3: Load the file into a Pandas DataFrame
if file_path.endswith(".csv"):
    df = pd.read_csv(file_path) 
elif file_path.endswith(".xlsx"):
    df = pd.read_excel(file_path)
else:
    print("Unsupported file format. Please upload a CSV or Excel file.")
    exit()

print("\nData Preview:")
print(df.head())

# Step 4: Get table name from the user
table_name = input("Enter the table name: ")

# Step 5: # When we load an Excel/CSV file into Pandas, 
# each "column" has a specific Pandas data type (like int64, float64, object, etc.).
# But PostgreSQL does not use Pandas data types. It has its own SQL types (INTEGER, TEXT, BOOLEAN, etc.).
dtype_mapping = {
    'int64': 'INTEGER',
    'float64': 'FLOAT',
    'object': 'TEXT',
    'bool': 'BOOLEAN',
    'datetime64[ns]': 'TIMESTAMP'
}

# Step 6: Generate column definitions for SQL
columns = []
for col, dtype in df.dtypes.items(): #  df.dtypes.items() gives us the column name and its Pandas type.
    pg_type = dtype_mapping.get(str(dtype), 'TEXT')  # default to TEXT if unknown type
    columns.append(f'"{col}" {pg_type}')  # ensure column names are in double quotes === PostgreSQL converts 'unquoted' column names to lowercase automatically.

# Step 7: Create table query
create_table_query = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({", ".join(columns)});'

print("\nGenerated SQL Query:")
print(create_table_query)  # Just for debugging

# Step 8: Execute the query
try:
    cur.execute(create_table_query)
    conn.commit()
    print(f"✅ Table '{table_name}' created successfully!")
except Exception as e:
    print(f"❌ Error creating table: {e}")
finally:
    cur.close()
    conn.close()
