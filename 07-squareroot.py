# Title: Squre root
# Description: Solution to problem 7 - program that takes a positive floating point number as input and outputs an approximation of its square root.
# Context: Programming and Scripting, GMIT, 2019
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 10-03-2019
# Last update: 10-03-2019

###

# Asking for user's input and assigns float type to the input
number = float(input("Give enter a positive number: "))

# Calculate square root of the entered number
sqr = number**0.5

# Intermediate check - prints out square root
# print(sqr)

# Approximation to 1 precision digit after floating point
# Verbatim from https://stackoverflow.com/a/50038023
approx = float("%0.1f" % (sqr))

# Print out approxmate value of the square root
print("The square root of ", number, " is approx.", approx)
