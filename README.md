# Problem set solutions - pands-problem-set 2019


#### Author: Andrzej Kocielski  
#### Github login: andkoc001  
#### Email: G00376291@gmit.ie
Created: 07-02-2019,
Last update: 23-03-2019  

___

This repository containes my solutions to the Problem Set for the Programming and Scripting module, Galway-Mayo Institute of Technology, 2019.  
Lecturer: dr Ian McLoughlin

The detailed Problem Set instructions:  
https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf


Disclaimer: As it is my first contact with Python, my codes are naturally imperfect. However, some comments or redundant pices of code, etc.  are left as is for the purpose of learning, testing and future reference. 
____

## Problems research and solution


### [Problem 01 - Sum Up To](../blob/master/01-sumupto.py)
Task description:
 >_Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number._

Solution: https://github.com/andkoc001/pands-problem-set/blob/master/01-sumupto.py



$ python sumupto.py

Please enter a positive integer: 10

55


___
### [Problem 02 - Begins With T](../master/02-begins-with-t.py)
Task description:
 >_Write a program that outputs whether or not today is a day that begins with the letter T. An example of running this program on a Thursday is as follows._

Solution: https://github.com/andkoc001/pands-problem-set/blob/master/02-begins-with-t.py


An example of running it on a Wednesday is as follows.

$ python begins-with-t.py

No - today does not begin with a T.


___
### [Problem 03 - Divisors](../master/03-divisors.py)
Task description:
 >_Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12._

Solution: https://github.com/andkoc001/pands-problem-set/blob/master/03-divisors.py

$ python divisors.py

1002
1014
1026
etc
9990


___
### [Problem 04 - Collatz](../master/04-collatz.py)
Task description:
 >_Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one._


Solution: https://github.com/andkoc001/pands-problem-set/blob/master/04-collatz.py

$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1


___
### [Problem 05 - Primes](../master/05-primes.py)
Task description:
 >_Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime._

Solution: https://github.com/andkoc001/pands-problem-set/blob/master/05-primes.py

$ python primes.py

Please enter a positive integer: 19

That is a prime.


___
### [Problem 06 - Second String](../master/06-secondstring.py)
Task description:
 >_Write a program that takes a user input string and outputs every second word._

Solution: https://github.com/andkoc001/pands-problem-set/blob/master/06-secondstring.py

$ python secondstring.py

Please enter a sentence: The quick brown fox jumps over the lazy dog.

The brown jumps the dog


___
### [Problem 07 - Square Root](../master/07-squareroot.py)
Task description:
 >_Write a program that that takes a positive floating point number as input and outputs an approximation of its square root._


Solution: https://github.com/andkoc001/pands-problem-set/blob/master/07-squareroot.py

$ python squareroot.py

Please enter a positive number: 14.5

The square root of 14.5 is approx. 3.8.


___
### [Problem 08 - Date Time](../master/08-datetime.py)
Task description:
 >_Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”._


Solution: https://github.com/andkoc001/pands-problem-set/blob/master/08-datetime.py

$ python datetime.py

Monday, January 10th 2019 at 1:15pm


___
### [Problem 09 - Second](../master/09-second.py)
Task description:
 >_Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line._


Solution: https://github.com/andkoc001/pands-problem-set/blob/master/09-second.py

$ python second.py moby-dick.txt

Title: Moby Dick; or The Whale

CHAPTER 1

Call me Ishmael. Some years ago--never mind how long

particular to interest me on shore, I thought I would sail about a

...


___
### [Problem 10 - Plot](../master/10-plot.py)
Task description:
 >_Write a program that displays a plot of the functions x, x 2 and 2 x in the range [0, 4]._


Solution: https://github.com/andkoc001/pands-problem-set/blob/master/10-plot.py


___
### References

https://learnonline.gmit.ie/course/view.php?id=1588#section-0
https://docs.python.org/3/tutorial/