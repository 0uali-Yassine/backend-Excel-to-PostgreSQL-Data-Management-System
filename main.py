import pandas as pd
from database import DB

DB.get_connect()


file_path = input("Enter the file path (CSV or Excel): ")

# Check file type and load into Pandas
if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
elif file_path.endswith(".xlsx"):
    df = pd.read_excel(file_path)
else:
    print("Unsupported file format. Please upload a CSV or Excel file.")
    exit()

print("Data Preview:")
print(df.head())  # Show first 5 rows
