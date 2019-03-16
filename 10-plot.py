# Title: Plot of funtions
# Description: Solution to problem 10 - program that displays a plot of the functions x, x^2 and 2^x in the range [0, 4].
# Context: Programming and Scripting, GMIT, 2019
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 15-03-2019
# Last update: 15-03-2019

###

# Importing libraries
# Reference: https://medium.com/python-pandemonium/data-visualization-in-python-line-graph-in-matplotlib-9dfd0016d180
import matplotlib.pyplot as plt

# test data for my better understanting, taken verbatim from https://medium.com/python-pandemonium/data-visualization-in-python-line-graph-in-matplotlib-9dfd0016d180
# x = [0, 1, 2]
# y = [0, 1, 4]
# plt.plot(x, y)
# plt.show()

# Funtion definition


def func_plot(x, y):
    plt.plot(x, y)
    plt.show()


# Plotting range definition
plotting_range = range(0, 5)

# assign values of x in range
# https://youtu.be/CuuvojEKHWo

# y = x
x = [i for i in plotting_range]
y1 = [i for i in x]

# y = x^2
x = [i for i in plotting_range]
y2 = [i**2 for i in x]

# y = 2^x
x = [i for i in plotting_range]
y3 = [2**i for i in x]

# Calling the above defined method 'func_plot' to plot the funtion's chart
func_plot(plotting_range, y1)
func_plot(plotting_range, y2)
func_plot(plotting_range, y3)
