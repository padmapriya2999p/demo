import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# Load data from CSV file
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to perform some operation on each row
def operation(user_id, age, n):
    return len(str(user_id)) * sum(i**2 for i in range(1, n+1)) * age

# File path of the CSV file
file_path = "Netflix Userbase.csv"  # Replace "your_file.csv" with the actual file path

# Load data from CSV
df = load_data(file_path)

# Value for computation
n = 10000

# Time measurement for each method
methods = ['iterrows', 'for loop with .loc or .iloc', 'apply', 'itertuples', 'list comprehensions', 'pandas vectorization', 'NumPy vectorization']
times_micro = []

for method in methods:
    start_time = time.time()
    if method == 'iterrows':
        for index, row in df.iterrows():
            operation(row['User ID'], row['Age'], n)
    elif method == 'for loop with .loc or .iloc':
        for i in range(len(df)):
            operation(df.loc[i, 'User ID'], df.loc[i, 'Age'], n)
    elif method == 'apply':
        df.apply(lambda row: operation(row['User ID'], row['Age'], n), axis=1)
    elif method == 'itertuples':
        for row in df.itertuples(index=False):
            operation(row[0], row[6], n)
    elif method == 'list comprehensions':
        [operation(row[0], row[6], n) for row in df.itertuples(index=False)]
    elif method == 'pandas vectorization':
        df['User ID'].astype(str).apply(len) * sum(i**2 for i in range(1, n+1)) * df['Age']
    elif method == 'NumPy vectorization':
        operation(df['User ID'].values, df['Age'].values, n)
    times_micro.append((time.time() - start_time) * 1e6)  # Convert seconds to microseconds

# Plotting the graph
plt.figure(figsize=(12, 6))

# Scatter Plot
plt.subplot(1, 3, 1)
plt.scatter(methods, times_micro, color='skyblue')
plt.xlabel('Methods')
plt.ylabel('Time (microseconds)')
plt.title('Scatter Plot')
plt.xticks(rotation=45, ha='right')

# Line Plot
plt.subplot(1, 3, 2)
plt.plot(methods, times_micro, marker='o', color='orange')
plt.xlabel('Methods')
plt.ylabel('Time (microseconds)')
plt.title('Line Plot')
plt.xticks(rotation=45, ha='right')

# Bar Plot
plt.subplot(1, 3, 3)
plt.bar(methods, times_micro, color='green')
plt.xlabel('Methods')
plt.ylabel('Time (microseconds)')
plt.title('Bar Plot')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()

# Save the plot as an image
plt.savefig('time_comparison_all_plots_micro.png')

# Show the plot
plt.show()
