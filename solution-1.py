# Title: Solution to problem 1
# Description: program asks the user to input any positive integer and outputs the sum of all numbers between one and that number.
# Context: Programmin and Scripting, GMIT, 2019
# Author: Andrzej Kocielski
# Date of creation: 07-02-2019
# Last update: 09-02-2019

###

# Variables definition
input_number = 3 # Temporary value given
answer = 0
i = 1

# Asking for user's input
input_number = int(input("Give me a positive integer: ")) #assigns integer type to the input - why is it string by default? How can I check if the input is a numeral?

# Positive integer check
if (input_number < 1):
  print("You typed:", input_number, "Please give me a positive integer, e.g. 11.")

else:
  # Summing up
  while i <= input_number:
    answer = answer + i
    i += 1 # increments value of i by one (for some reasons i++ does not work)
  print ("The sum of all numbers between 1 and",input_number, "equals:",answer) # Prins answer on screen