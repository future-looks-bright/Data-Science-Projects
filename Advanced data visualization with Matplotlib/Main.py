import os
import pandas as pd

# Folder where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# CSV file name
csv_file_name = "QueryResults.csv"

# Full path to the CSV file
csv_path = os.path.join(script_dir, csv_file_name)

# Check if the file exists
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"CSV file not found at: {csv_path}")

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_path, names=['DATE', 'TAG', 'POSTS'], header=0)

print(df.head())
print(df.tail())