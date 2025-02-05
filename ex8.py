import pandas as pd

# Get user input for CSV file path
file_path = input("Enter the CSV file path: ")

# Read the CSV file and display the first 5 rows
try:
    data = pd.read_csv(file_path)
    print(data.head())
except FileNotFoundError:
    print("The file was not found. Please check the path.")
