# Title: Divisors
# Description: Solution to problem 3 - program prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.
# Context: Programming and Scripting, GMIT, 2019
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 17-02-2019
# Last update: 17-02-2019

###

lower_limit = 1000
upper_limit = 10000

for n in range(lower_limit, upper_limit):
    if n % 6 == 0:  # first level that filters numbers divisible by 6
        if n % 12 != 0:  # second levevl filter for numbers _not divisible by 12
            print(n)
