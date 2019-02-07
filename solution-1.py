# Title: Solution to problem 1
# Context: Programmin and Scripting, GMIT, 2019
# Author: Andrzej Kocielski
# Date of creation: 07-02-2019
# Last update: 07-02-2019

# Description: program asks the user to input any positive integer and outputs the sum of all numbers between one and that number.

###

# Variables definition
input_number = 3 # Temporary value given
answer = 0
i = 1

# Asking for user's input
input_number = int(input("Give me a positive integer: ")) # is it right way to convert string (which is default type of input) into integer?

# Positive integer check -----unfinished yet
print ("You typed: ", input_number)

# Summing up
while i <= input_number:
  answer = answer + i
  i += 1 # increments value of i by one (for some reasons i++ does not work)

# Prins answer on screen
print ("The sum of all numbers between 1 and",input_number, "equals:",answer)
