# Pandas is a library that provides data structures and data analysis tools for Python programming language.
import pandas as pd # import the pandas library

# * Introduction to Pandas
"""
Pandas is a powerful data manipulation library built on top of NumPy. It provides two primary data structures:
- Series: A one-dimensional labeled array.
- DataFrame: A two-dimensional labeled data structure, similar to a table.

DataFrames allow for easy manipulation, indexing, and analysis of data, making them a fundamental tool in data science.
"""
# ! ------------------------------------ #
# * Creating a Series
cars_per_cap = pd.Series([809, 18, 200, 591, 588, 173, 479, 249])
# Display the Series
print(cars_per_cap)
# Output
# 0    809
# 1     18
# n ......
# dtype: int64

# * Creating a Series with custom row (index) labels
countries = ['US', 'IN', 'RU', 'JP', 'DE', 'CN', 'FR', 'BR']
cars_per_cap = pd.Series([809, 18, 200, 591, 588, 173, 479, 249], index=countries)
print(cars_per_cap)
# Output
# US    809
# IN     18
# n ......
# dtype: int64

# ! ------------------------------------ #
#  * Creating a DataFrame from a dictionary
data = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.1, 3.286, 9.597, 1.221],
    "population": [211, 144, 1380, 1439, 59]
}
brics = pd.DataFrame(data)
print(brics)
# Output
#       country    capital    area  population
# 0      Brazil   Brasilia   8.516        211
# 1      Russia      Moscow  17.100        144
# ...
# Assigning custom row labels
brics.index = ["BR", "RU", "IN", "CN", "ZA"]
print(brics)
# Output
#         country    capital    area  population
# BR      Brazil   Brasilia   8.516        211
# RU      Russia      Moscow  17.100        144
# ...

# ! ------------------------------------ #
# Sample CSV data as a Python docstring, CVS is a comma-separated values file in csv apps its put in a table with rows and columns
# spaces can cause issues in csv files
cars_csv = """
country,cars_per_cap,drives_right,population
US,809,True,331002651
IN,18,False,1380004385
RU,200,True,145912025
JP,591,False,126476461
DE,588,True,83783942
CN,173,False,1439323776
FR,479,True,65273511
BR,249,False,212559417
"""
# * Loading a DataFrame from a CSV file
# Assume 'cars.csv' exists in the working directory
cars = pd.read_csv("DataScience/Libraries/cars.csv", index_col=0) # index_col=0 means the first column (row label) is the index and will always be there in the output
print(cars)
# Output
#         cars_per_cap  drives_right  population 
# country 
# US              809         True  331002651
# IN               18        False 1380004385
# ...
# ! NOTE NOTE NOTE NOTE NOTE NOTE NOTE:
""" 
The Countries column is the index column, which is a special column that contains the row labels.
The index column is not a real column with values, but rather a row label. IT CANNOT BE IGNORED OR SELECTED INDIVIDUALLY
this means that even if we get the cars csv from cols 2-3 the index column will still be there as the first column
BUT the first row with the lables is not a special row, its just like any other row meaning it can be ig for EX if we take csv from row 2-3 etc
BUt the index column will always be there

As seen in the brics ex vs the csv example. the index column dose not need its own column name, its just the first column
"""

# ! ------------------------------------ #
# * Square Brackets (used for indexing)

# * Accessing columns using square brackets for a Series, series has only 1 column exluding the index column which is the first column
# * so we access values by index or name of the row, we canot just select the index column as thats not a real column with values
print(cars_per_cap['IN'])  # Output: 18
# Accessing by position
print(cars_per_cap[1])  # Output: 18, you should use .iloc for position-based indexing but this works
# Selecting multiple elements
print(cars_per_cap[['IN', 'RU', 'JP']]) # Output: IN 18 RU 200 JP 591, each separated by a new line

# * Accessing columns using square brackets for a DataFrame, essentially insted of [row][column] we do [[colums]]
country_column = brics["country"]  # Returns a Series
print(country_column) # BR Brazil, RU Russia, IN India, CN China, ZA South Africa
print(country_column[1])  # Output: Russia
subset = brics[["country", "capital"]]  # Returns a DataFrame as we have more than 1 column and rows so its 2D = DataFrame
print(subset)
# output
#         country    capital
# BR      Brazil   Brasilia
# RU      Russia      Moscow
# ...
# * Accessing rows using square brackets
print(cars[1:4])  # Selects rows 1 to 3 (excluding 4)
# Output
#      country  cars_per_cap  drives_right  population
# IN        IN            18         False  1380004385
# RU        RU           200          True   145912025
# JP        JP           591         False   126476461
# * Accessing rows and columns using square brackets
print(cars[2:4]["cars_per_cap"])  # Selects rows 2 to 3 (excluding 4), list slicing) and only 'cars_per_cap' column
# Output
# country
# RU    200
# JP    591
# Name: cars_per_cap, dtype: int64 3 ignore this info
# NOTE: see how the first row is not included its beacuse its not a index column, its a row label whci his just like any otehr row

# ! ------------------------------------ #
# * Accessing Series using loc and iloc for row indexing to be consistent with DataFrame indexing you can optinally use .loc and .iloc
# * series are 1d they only have one column, exluding the index column which is the first column so we only have 1 column to access so we can only access by index or name of the row
# using loc for label-based indexing, based on the value of the index
print(cars_per_cap.loc[['IN', 'RU', 'JP']]) # Output: IN 18, RU 200, JP 591
# using iloc for position-based indexing, based on the position of the index
print(cars_per_cap.iloc[[1, 2, 3]]) # Output: IN 18, RU 200, JP 591

# * Accessing DataFrame rows using loc and iloc, since DF are 2d we have both rows and columns to access
# loc is label-based indexing where you must give the name of the row or column
russia_data = brics.loc["RU"]  # Label-based indexing
print(russia_data) # Output: country        Russia, capital        Moscow, area           17.1, population       144
populations_data = brics.loc[:, "population"]  # Selects all rows for 'population' column
print(populations_data) # Output: BR     211, RU     144, IN    1380, CN    1439, ZA      59
print(cars.loc['IN', 'cars_per_cap'] ) # Selects 'cars_per_cap' value for 'IN' # Output: 18
print(cars.loc[['IN', 'RU'], 'cars_per_cap'])  # Selects 'cars_per_cap' for 'IN' and 'RU' # Output: IN 18, RU 200
print(cars.loc[['IN', 'RU'], :])  # Selects all columns for 'IN' and 'RU'
# Output
#      country  cars_per_cap  drives_right  population
# IN        IN            18         False  1380004385
# RU        RU           200          True   145912025
print(cars.loc[:, 'cars_per_cap':'drives_right'])  # Selects columns from 'cars_per_cap' to 'drives_right'
# Output
#      cars_per_cap  drives_right
# BR            809         False
# RU            200          True
# ...
print(cars.loc[:, ~cars.columns.isin(['drives_right'])])  # Selects all columns except 'drives_right'
# Output
#      country  cars_per_cap  population
# BR      Brazil           809        211
# RU      Russia           200        144
# ...

# iloc is integer-based indexing where you have to specify rows and columns by their integer index
first_row = brics.iloc[0]  # Position-based indexing
print(first_row) # Output: country        Brazil, capital        Brasilia, area           8.516, population       211
print(cars.iloc[[3, 4], [0, 1]])  # NOTE: Selects values from row 3 and 4, columns 0 and 1 ****not including the index column
# Output
#      country  cars_per_cap drives_right
# JP        JP           591        False
# DE        DE           588         True

print(cars.iloc[:, [1, 2]])  # Selects all rows for columns 1 and 2 ****not including the index column
# Output
# country  drives_right population
# US          True      331002651
# IN         False     1380004385
# ...
print(cars.iloc[1:5:2, :])  # Selects rows 1, 3 from all columns *including the index column*
# Output
#      country  cars_per_cap  drives_right  population
# IN        IN            18         False  1380004385
# JP        JP           591         False   126476461
