# Title: Second Strig
# Description: Solution to problem 6 - program that takes a user input string and outputs every second word.
# Context: Programming and Scripting, GMIT, 2019
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 10-03-2019
# Last update: 10-03-2019

###

# Prompt for the user; definition of a new variable for the user's input
sentence = print("Please enter a sentence: ")

# intermediate test of the program - prints out the user's input
print(sentence)

# calls method split of "str" library in order to split the user input into single words, separated by a space
str.split(sentence)

# intermediate test of the program - prints out the divided sentence
print(sentence)[:]
