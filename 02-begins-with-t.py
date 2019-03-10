# Title: Begins with T
# Context: Programming and Scripting, GMIT, 2019
# Description: Solution to problem 2 - program outputs whether or not today is a day that begins with the letter T.
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 14-02-2019
# Last update: 14-02-2019

###

# External libraires
import datetime

# Check and output
if (datetime.datetime.today().weekday() == 1) or (datetime.datetime.today().weekday() == 3):
    print("Yes - today begins with a T.")
else:
    print("No - today does not begin with a T.")
