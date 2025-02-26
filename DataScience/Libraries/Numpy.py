### ! NumPy (numpy is a short form of Numerical Python it is a library in Python used for working with arrays and matrices)
""" 
- Pre-requisite: CS Terminology (Arrays vs Lists) and Python Syntax for Lists

🔍 Whats the Problem with Python Lists?
You already know Python lists are flexible—they can hold any type of data and can mix different types. You can change, add, and remove elements easily.

But heres the catch:
When working with large datasets (common in data science), you often want to perform operations on entire collections of numbers at once. Lists can't handle this efficiently.

Example:
If you have two lists:
"""
height = [1.73, 1.68, 1.71, 1.89, 1.79]  # heights in meters  
weight = [65.4, 59.2, 63.6, 88.4, 68.7]  # weights in kilograms  

# * Trying to calculate the Body Mass Index (BMI) like this:
# bmi = weight / (height ** 2)  # ❌ This will throw an error!
# * Python doesn’t know how to perform element-wise operations on lists

""" 
💡 Solution: Enter NumPy!
NumPy (Numerical Python) is a game-changer—it brings in the array structure, which is faster and allows element-wise operations directly.
"""
# pip install numpy
import numpy as np
# Now, turn those lists into arrays:
np_height = np.array(height)  
np_weight = np.array(weight)  
# Calculating BMI becomes super simple and efficient:
bmi = np_weight / np_height ** 2  
print(bmi)  # Outputs BMI for all elements in one go!

# ! ------------------------------------ #

""" 
⚖️ Why NumPy Over Lists?
✅ Element-wise operations (e.g., addition, subtraction, multiplication)
✅ Performance boost (arrays are much faster than lists)
✅ Memory efficient (stores data more compactly)
"""
# Ex of lists vs numpy operations 
# Using lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # ➡️ [1, 2, 3, 4, 5, 6] (Concatenation)

# Using NumPy arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(array1 + array2)  # ➡️ [5, 7, 9] (Element-wise addition)

# ! ------------------------------------ #

""" 
⚠️ Important Notes About NumPy Arrays
Single Data Type:
Arrays can only hold one data type.
Mixing types forces all elements to convert to the same type.
Array-Specific Methods:
NumPy arrays come with their own methods—some behave differently from standard lists.
"""
# Example:
mixed_array = np.array([True, 1.5, "Data"])  
print(mixed_array)  # All elements will be converted to strings

# ! ------------------------------------ #

""" 
🎯 Subsetting in NumPy (Getting Specific Data), NOTE: the bmi is a np array not a list 
Standard Subsetting:
Just like lists, you can use square brackets:
"""
print(bmi[1])  # Gets BMI for the second person
""" 
Boolean Subsetting:
This is powerful for filtering data based on conditions.
"""
# Find all BMI values greater than 23
bmi_over_23 = bmi[bmi > 23]
print(bmi_over_23)  # Only returns values above 23

# ! ------------------------------------ #

""" 
🔥 Quick Bonus Tip: Vectorization vs. Looping
NumPy is vectorized, meaning it applies operations across entire arrays simultaneously—way faster than looping through elements.
With a loop (inefficient):
""" 
bmi_list = []
for i in range(len(weight)):
    bmi_list.append(weight[i] / (height[i] ** 2))    
"""
With NumPy (efficient):
"""
bmi = (
    np_weight / np_height**2
)  # One-liner!, bmi is a array so its faster than list and more compact

# ! ------------------------------------ #

"""  
🔍 What You Need to Know About 2D NumPy Arrays
Type Check
Every NumPy array is of type numpy.ndarray, regardless of dimensions.
You can check the shape of an array with .shape, which returns a tuple like (rows, columns).
Creating a 2D Array
A 2D array is made from a list of lists:
"""
# ex:
np_2d = np.array([[1.73, 65.4], [1.68, 59.2], [1.80, 72.5]])

""" 
Arithmatic 
element wise operations
"""
# Two 2D arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = a + b  # [[6, 8], [10, 12]]

""" 
Subsetting
Access individual elements:
"""
# accsess indivisual elements 
np_2d[0][2]  # First row, third element
np_2d[0, 2]  # Same as above, more intuitive
# select multiple elements
np_2d[:, 1:3]  # All rows, columns 1 to 2 (excluding 3)
np_2d[1, :]    # Second row, all columns
# element wise operation
bmi = np_2d[:, 1] / np_2d[:, 0]**2  # Calculate BMI for each person

""" 
Array brodcasting with NumPy
arithmatic with arrays of different dimentions
"""
c = np.array([1, 2])  # 1D array
# Add c to every row of a
result = a + c  # [[2, 4], [4, 6]] # a is a 2d array = a's subarrays hence the operations is preformed on indivisual 1d arrays i.e a's subarrays and c

# ! ------------------------------------ #

""" 
🔍 Basic Statistical Functions
Assuming you have a 2D array from a city-wide survey:
"""
# * Simulating city survey data (5000 people, height in meters, weight in kg)
# In NumPy, np.random.seed(0) sets the seed for the random number generator. 
# This ensures that whenever you run your code, you get the same sequence of random numbers every time.
# EX: np.random.rand(3) will generate the same sequence of random numbers every time you run the code after setting seed to 0 = [0.5488135  0.71518937 0.60276338]
np.random.seed(0)  # For consistent results, use in a team where everyone has the same seed so everyone has the same number to test with insead of random numbers
# The function np.random.normal(mean, std_dev, size) generates random numbers from a normal (Gaussian) distribution.
# Normal Distribution (Bell Curve)
# Most values are around the mean (center).
# The standard deviation (std_dev) controls the spread of values.
# It's widely used in real-world data like heights, weights, IQ scores, etc. 
# EX heights = np.random.normal(1.75, 0.15, 10)  # Mean=1.75m, std=0.15m, 10 samples, Each time, you’ll get random values centered around 1.75, with most values within ±0.15.
height = np.random.normal(1.75, 0.20, 5000)  # Mean height 1.75m, std dev 0.20m
weight = np.random.normal(70, 10, 5000)      # Mean weight 70kg, std dev 10kg
# Combine height and weight into a 2D array
np_city = np.column_stack((height, weight)) # a column stack is a 2d array that combines height and weight into a 2D array
# height and weight are both 1D arrays repersenting the height for each person at index i and the weight for each person at index i
# combining then looks something like :
# np_city = [[height[0], weight[0]], 
#           [height[1], weight[1]], 
#           [height[2], weight[2]], 
#                               ...]

# ! ------------------------------------ #

""" 
📈 Exploring Your Data
"""
# * Mean
avg_height = np.mean(np_city[:, 0])  # Mean height, colomn 0 = height
avg_weight = np.mean(np_city[:, 1])  # Mean weight, colomn 1 = weight
# * median 
median_height = np.median(np_city[:, 0])  # Median height
median_weight = np.median(np_city[:, 1])  # Median weight
#  *Standerd Deviation (how spred out the data is )
std_height = np.std(np_city[:, 0])  # Height spread
std_weight = np.std(np_city[:, 1])  # Weight spread
# * Sum and sort 
total_weight = np.sum(np_city[:, 1])  # Total weight of the population
sorted_heights = np.sort(np_city[:, 0])  # Sorted list of heights

# ! ------------------------------------ #

""" 
Correlation
Want to see if height and weight are related? Use the correlation coefficient:
"""
# * This returns a matrix where correlation[0, 1] shows how height and weight are related (closer to 1 = strong positive correlation).
correlation = np.corrcoef(np_city[:, 0], np_city[:, 1])

""" 
🎲 Generating Random Data
You can simulate more data using random distributions:
"""
# Random heights and weights for 1000 people
random_heights = np.random.normal(1.75, 0.15, 1000)
random_weights = np.random.normal(70, 15, 1000)
# Combine into a 2D array
random_city = np.column_stack((random_heights, random_weights))

# ! ------------------------------------ #
""" 
✅ Key Takeaways
Use NumPy arrays for efficient numeric operations.
Arrays only hold one data type.
Perform element-wise calculations easily.
Use boolean subsetting for filtering data quickly.
"""
