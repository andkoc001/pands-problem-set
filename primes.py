# Title: Primes
# Description: Solution to problem 5 - program that asks the user to input a positive integer and tells the user whether or not the number is a prime.
# Context: Programming and Scripting, GMIT, 2019
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 25-02-2019
# Last update: 25-02-2019

###

n = int(input("Please input a positive integer: "))

x = 0  # answer condition

if n < 0:
    print("This is not a positive integer.")
elif n == 1 or n == 0:
    print("That is not a prime.")
else:

    for i in range(2, n):
        # print(i)
        if n % i == 0:
            x = 1
            # print("That is not a prime.")
            break
        # else:
            # print("That is a prime.")
    if x == 0:
        print("That is a prime.")
    else:
        print("That is not a prime.")
