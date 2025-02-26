# Matplotlib is the foundation of data visualization in Python. The pyplot module (plt) is used to create different types of plots.
import matplotlib.pyplot as plt   # import the pyplot module
# Data
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]  
population = [2.5, 3.0, 3.7, 4.4, 5.3, 6.1, 7.0]  
# ! ------------------------------------ #
""" 
Line Plot
A line plot connects data points with a line, useful for showing trends over time.
"""
# Create line plot
plt.plot(years, population)  
# Show the plot
plt.show()  
# ! ------------------------------------ #
""" 
Scatter Plot
A scatter plot displays individual data points without connecting them, making it great for identifying patterns.
"""
# Scatter plot
plt.scatter(years, population)  
# Show the plot
plt.show()  
# ! ------------------------------------ #
""" 
Histogram
A histogram shows the distribution of numerical data by grouping values into bins.
"""
# Generate random data
import numpy as np  
data = np.random.randn(1000)  
# Create histogram
plt.hist(data, bins=20)  
# Show the plot
plt.show()  
# ! ------------------------------------ #
""" 
Plot Customization
We can customize labels, titles, colors, and tick marks.
"""
plt.plot(years, population, color='red', linestyle='--', marker='o')  
plt.xlabel("Year")  
plt.ylabel("Population (Billions)")  
plt.title("World Population Over Time")  
plt.grid(True)  
plt.show()  
# ! ------------------------------------ #
""" 
Key Takeaways:

plot() → Line plots
scatter() → Scatter plots
hist() → Histograms
Customization → Labels, colors, grid, markers
Matplotlib is powerful for visualizing data quickly and effectively!
"""