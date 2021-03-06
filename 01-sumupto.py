# Title: Sum up to
# Context: Solution to problem 1, Programming and Scripting, GMIT, 2019
# Description: program asks the user to input any positive integer and outputs the sum of all numbers between one and that number.
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 10-02-2019
# Last update: 10-02-2019

###

# Variables definition
input_number = 3  # Temporary value given
answer = 0
i = 1

# Asking for user's input
# assigns integer type to the input - why is it string by default? How can I check if the input is a numeral?
input_number = int(input("Give me a positive integer: "))

# Positive integer check
if (input_number < 1):
    print("You typed:", input_number,
          "Please give me a positive integer, e.g. 11.")

else:
    # Summing up
    while i <= input_number:
        answer = answer + i
        # increments value of i by one (for some reasons i++ does not work)
        i += 1
    print(answer)  # Prints answer on screen
