# Title: Second
# Description: Solution to problem 9 - program that reads in a text file and outputs every second line.
# The program should take the filename from an argument on the command line.
# Context: Programming and Scripting, GMIT, 2019
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 13-03-2019
# Last update: 14-03-2019

###

# Importing sys module to open a txt file from command line.
# Reference: https://docs.python.org/3/library/sys.html, https://stackoverflow.com/a/7439152
import sys

# the argument given in the command line is the name of the file to be read, eg. "pythin 09-second.py textfile.txt"
file_name = sys.argv[1]

# assigns the file name to the variable "f"
f = open(file_name)

# reads and print out the content of the file
file_content = f.read()
print(file_content)

# closes the file to release the computational resources
f.close()
