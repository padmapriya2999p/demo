# Time Comparison of Different Methods for DataFrame Iteration in Python

This script compares the execution time of different methods for iterating over a DataFrame in Python using pandas library.

## Purpose

The purpose of this script is to analyze and compare the performance of various iteration methods available in pandas for processing data in a DataFrame. These methods include:

- iterrows
- for loop with .loc or .iloc
- apply
- itertuples
- list comprehensions
- pandas vectorization
- NumPy vectorization

The script measures the time taken by each method to perform a given operation on each row of the DataFrame and visualizes the results using different types of plots.

## How to Use

1. **Prerequisites**:
   - Python 3 installed on your system
   - Required libraries: pandas, numpy, matplotlib
   
2. **Clone the Repository**:
    git clone https://github.com/padmapriya2999p/demo

The script will generate plots showing the time taken by each method in microseconds.
The plots will be saved as images in the same directory.
Additionally, you can customize the script to save the plots in different formats or modify the plot styles as per your requirements.