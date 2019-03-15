# Title: Second
# Description: Solution to problem 9 - program that reads in a text file and outputs every second line.
# The program should take the filename from an argument on the command line.
# Context: Programming and Scripting, GMIT, 2019
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 13-03-2019
# Last update: 15-03-2019

###

# Importing sys module to open a txt file from command line.
# Reference: https://docs.python.org/3/library/sys.html, https://stackoverflow.com/a/7439152
import sys

# the argument given in the command line is the name of the file to be read, eg. "pythin 09-second.py textfile.txt"
file_name = sys.argv[1]

# assigns the variable "f" to funtion opening the file (file name given as argument)
f = open(file_name)

# reads and print out the content of the file
# file_content = f.read()
# print(file_content) # for intermediate check

# mechanism to read and print every second line (called here as verse for my better understanding)
# adapted from https://stackabuse.com/read-a-file-line-by-line-in-python/
verse = f.readline()
verse_number = 1  # counter set at 1

# loop is performed as long as line (verse) exists
# still do not quite understand how the lines (variable verse) are incremented
while verse:
    if verse_number % 2 != 0:
        print(verse.strip())
    verse = f.readline()
    verse_number += 1

# closes the file to release the computational resources
f.close()
