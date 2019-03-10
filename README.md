# Solutions to Problem Set, Programming and Scripting module, GMIT 2019

Author: Andrzej Kocielski
github login: andkoc001
Email: G00376291@gmit.ie

This repository containes my solutions to the Problem Set for the module Programming and Scripting course - GMIT 2019. See here for the Problem Set instructions: https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf

Note: For assignment, please use the programs with the names as suggested in the problem list, e.g. sumupto.py as an answer to problem 1.

Problems description:

1. Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.

$ python sumupto.py
Please enter a positive integer: 10
55

2. Write a program that outputs whether or not today is a day that begins with the letter T. An example of running this program on a Thursday is as follows.

$ python begins-with-t.py
Yes - today begins with a T.
An example of running it on a Wednesday is as follows.
$ python begins-with-t.py
No - today does not begin with a T.

3. Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

$ python divisors.py
1002
1014
1026
etc
9990

4. Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

$ python collatz.py
Please enter a positive integer: 10
10 5 16 8 4 2 1

5. Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.

$ python primes.py
Please enter a positive integer: 19
That is a prime.

6. Write a program that takes a user input string and outputs every second word.

$ python secondstring.py
Please enter a sentence: The quick brown fox jumps over the lazy dog.
The brown jumps the dog

7. Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.

8. Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.

$ python datetime.py
Monday, January 10th 2019 at 1:15pm

9. Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.

$ python second.py moby-dick.txt
Title: Moby Dick; or The Whale
CHAPTER 1
Call me Ishmael. Some years ago--never mind how long
particular to interest me on shore, I thought I would sail about a
...

10. Write a program that displays a plot of the functions x, x 2 and 2 x in the range [0, 4].
