# Title: Second Strig
# Description: Solution to problem 6 - program that takes a user input string and outputs every second word.
# Context: Programming and Scripting, GMIT, 2019
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 10-03-2019
# Last update: 10-03-2019

###

# Prompt for the user; definition of a new variable "sentence" for the user's input

# Intermediate test of the program - predefined sentence
# sentence = "1abc 2def 3geh 4ijk 5lkm 6nop 7rst 8uwz"

sentence = input("Please enter a sentence: ")

# Intermediate test of the program - prints out the user's input
# print(type(sentence))
# print(sentence)

# Calls method split method in order to split the user input into single words, separated by a space
sentence.split()

# Assignment of number of words in the sentence to variable n
n = len(sentence.split())

# Intermediate test of the program - shows number of words in the sentence
# print(n)

# Joining the words by contanation - pre-definintion of empty (for now) variable, which will be subsequently updated as the program runs
result_line = ""

# Prints out odd words from the sentence
for i in range(n):
    # Separation of odd and even words
    if i % 2 == 0:
        # this was original command that returned words in separate lines
        # print(sentence.split()[i])
        result_line += (sentence.split()[i]) + " "
print(result_line)
