# Title: Collatz
# Description: Solution to problem 4 - program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.
# Context: Programming and Scripting, GMIT, 2019
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 24-02-2019
# Last update: 24-02-2019

###

number = int(input("Please enter a positive integer: "))

while number > 1:  # termination condition
    if number % 2 == 0:
        number = number // 2  # result remains as intiger
    else:
        number = number * 3 + 1
    print(number)
