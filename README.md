# Problem set solutions - pands-problem-set 2019

>Author: **Andrzej Kocielski**  
>Github: [andkoc001](https://github.com/andkoc001/)  
>Email: G00376291@gmit.ie

Created: 07-02-2019,
Last update: 25-03-2019  

___

This repository contains my solutions to the Problem Set for the Programming and Scripting module, Galway-Mayo Institute of Technology, 2019.  
Lecturer: dr Ian McLoughlin

The detailed Problem Set instructions:  
<https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf>  

Note: As this course is my first contact with Python, my codes are naturally imperfect. However, some comments, redundant pieces of code, etc. are left intentionally for the purpose of learning, testing and future reference.

___

## Problems research and solution

### Problem 01 - [Sum Up To](../master/01-sumupto.py)

Task description:
 >_Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number._

Solution: <https://github.com/andkoc001/pands-problem-set/blob/master/01-sumupto.py>

This is an iterative repetition problem. It can be solved taking advantages of loop and conditions. The very problem was used in the lecture video as an example for demonstration how to control the flow of the program with the help of `while` operator.

I took the same approach my solution, but additionally I predefined some variables (`input_numner = 3`, `answer = 0` and `i = 1`). I also included a check whether the user-entered number is positive - when condition `if (input_number < 1)` is `True`, the program quits with an appropriate error message.

When the number is input by the user the program changes its type from default `str` to `int`.

Example (examples verbatim from Problem Set instructions):

```txt
$ python 01-sumupto.py
Please enter a positive integer: 10
55
```

___

### Problem 02 - [Begins With T](../master/02-begins-with-t.py)

Task description:
 >_Write a program that outputs whether or not today is a day that begins with the letter T. An example of running this program on a Thursday is as follows._

Solution: <https://github.com/andkoc001/pands-problem-set/blob/master/02-begins-with-t.py>

This problem required importing `datetime` module from standard Python library and application of `today()` and `weekday()` methods. One of the difficulties of solving the problem was the realisation of the fact that the weekdays numbering begins with 0 (Monday) and goes up to 6 (Sunday).

The solution required also conditional check. I performed a single 'if' check for two conditions using boolean `and` operator.

An example of running it on a Wednesday is as follows.

```txt
$ python begins-with-t.py
No - today does not begin with a T.
```

___

### Problem 03 - [Divisors](../master/03-divisors.py)

Task description:
 >_Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12._

Solution: <https://github.com/andkoc001/pands-problem-set/blob/master/03-divisors.py>

Further practice with loops, and boolean checks. This time the conditional checks were nested one inside the other. In the first level the program verifies whether the currently processed number inside `for` loop `is` divisible by 6, by checking whether modulo of the division equals 0 (`n % 6 == 0`). If so, another check is performed - whether the number `is not` divisible by 12 (whether modulo of the division is different from 0, `n % 12 != 0`). In such a case the number is printed out and the `for` loop moves to the next number in the predefined range.

Example:

```txt
$ python divisors.py
1002
1014
1026
etc
9990
```

___

### Problem 04 - [Collatz](../master/04-collatz.py)

Task description:
 >_Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one._

Solution: <https://github.com/andkoc001/pands-problem-set/blob/master/04-collatz.py>

To solve this problem, user's input is first converted to `integer` type. Next, through iteration process the input number is processed as per algorithm in the task description as long as the current value of the number reaches `1` - this is termination condition for the program. This is governed by the `while` loop. Inside the loop, the program checks logical condition (`number % 2 == 0`) and depending on the result, performs different computation. This is done with the help of `if - else` operators. After each cycle, the current value is printed out, so it is easy to track the progress of the algorithm.

Example:

```txt
$ python collatz.py
Please enter a positive integer: 10
10 5 16 8 4 2 1
```

___

### Problem 05 - [Primes](../master/05-primes.py)

Task description:
 >_Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime._

Solution: <https://github.com/andkoc001/pands-problem-set/blob/master/05-primes.py>

In addition to solution to the previous problems, this one utilises the `break` functionality, which allows for escape from the loop. For each integer number `i` incremented from 2 up to `n` (entered by the user), the program checks whether the input number is divisible by the current `i` without reminder. If so, the value of initially predefined variable `x = 0` is changed `1`. In my solution this is the 'break' condition for the loop.

Example:

```txt
$ python primes.py
Please enter a positive integer: 19
That is a prime.
```

___

### Problem 06 - [Second String](../master/06-secondstring.py)

Task description:
 >_Write a program that takes a user input string and outputs every second word._

Solution: <https://github.com/andkoc001/pands-problem-set/blob/master/06-secondstring.py>

This problem focuses on string manipulation. After many trials and errors and reading about Python, I finally reached an expected result. What I did to solve it was to split the user input sentence into single words using `split()` method. I used the default separator, i.e. a whitespace. Next, I assigned the number of words to variable `n`.

Following that, I defined another `string` variable, temporarily empty `result_line = ""`. This variable would subsequently be used to overcome the situation whereby the program returns the result in new lines for each word.

Moving on, I created a `for` loop in range of `n`. In each loop, the program checks whether the current iteration is divisible by 2. If so, the corresponding word is added at the end of the `result_line`, using `+=` notation, and moves on to the next iteration cycle.

Finally, the end result - every second word of the entered sentence - is printed out on the screen.

Example:

```txt
$ python secondstring.py
Please enter a sentence: The quick brown fox jumps over the lazy dog.
The brown jumps the dog
```

___

### Problem 07 - [Square Root](../master/07-squareroot.py)

Task description:
 >_Write a program that that takes a positive floating point number as input and outputs an approximation of its square root._

Solution: <https://github.com/andkoc001/pands-problem-set/blob/master/07-squareroot.py>

This problem introduces to `float` type and some of the related methods. My program asks user to enter a positive number and straight after that converts it into a `float` type.

The square root of the entered number is computed by taking the number to the power of `0.5`, and then rounded to single digit after the floating point, using the following syntax: `float("%0.1f" % (number**0.5))`.

Example:

```txt
$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.
```

___

### Problem 08 - [Date Time](../master/08-datetime.py)

Task description:
 >_Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”._

Solution: <https://github.com/andkoc001/pands-problem-set/blob/master/08-datetime.py>

Solution to this problem again requires import of `datetime` module. Subsequently, the date and time obtained with `datetime.today()` method is formatted to requested form, using the `f"{}"` notation.

My approach to the problem is a bit labours, as some sections of the code are repeated several times. This could be surely refined and the entire code could be shortened. On the other hand, I can follow the syntax.

First, I run loops where for each week day number the day name was assigned, as per example below.

```Python
if week_day == 0:
    week_day_name = "Monday"
```

Similarly, month name was assigned to the month number.

Next, I added ordinal number ending to today's calendar day. Again, I used `if, elif, else` conditional check for all the possible scenarios.

After that, I converted current hour to 12-hour time notation with either 'am' or 'pm' postfix (hour changed to `str` type). That was done by checking whether the current hour is lesser or equal to 12, if not, the current hour was lessen by 12.

Example:

```txt
$ python datetime.py
Monday, January 10th 2019 at 1:15pm
```

___

### Problem 09 - [Second](../master/09-second.py)

Task description:
 >_Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line._

Solution: <https://github.com/andkoc001/pands-problem-set/blob/master/09-second.py>

The challenge of solving this problem was to open an external text file in the command line. That was possible with help of `sys` module imported in the top of the code.

My program performs so, by using one of the `sys` methods: `.argv` with attribute `1`.

Subsequently, I opened the file by calling the `open()` method and assigned it to variable `f`. Then, I defined a variable which value was a line content: `verse = f.readline()`, and another variable that counts the lines. I used loop `while` to check if the current line is even - if so its content is printed on screen, and the loop moves on the the next iteration.

At the end of the program I closed the file with `close()` method.

Example:

```txt
$ python second.py moby-dick.txt
Title: Moby Dick; or The Whale
CHAPTER 1
Call me Ishmael. Some years ago--never mind how long
particular to interest me on shore, I thought I would sail about a
...
```

___

### Problem 10 - [Plot](../master/10-plot.py)

Task description:
 >_Write a program that displays a plot of the functions x, x 2 and 2 x in the range [0, 4]._

Solution: <https://github.com/andkoc001/pands-problem-set/blob/master/10-plot.py>

To solve this problem, I used an external library `matplotlib` and its subset `pyplot`.

I also defined a method, with two parameters: `x` and `y`. My method calls the `.plot` method with `x` and `y` arguments, and also the `.show` method to print the result on graph.

In the program body, the plotting range was assumed (as per task description). For each requested function (y=x, y=x^2, y=2^x), I run two loops - for each x value, corresponding y value was calculated.

The results are shown in the screens below.

| Function | Graph                       |
| -------- | --------------------------- |
| y = x    | ![y = x](/10-plot-x.png)    |
| y = x^2  | ![y = x^2](/10-plot-x2.png) |
| y = 2^x  | ![y = 2^x](/10-plot-2x.png) |

___

## References

- Module materials: <https://learnonline.gmit.ie/course/view.php?id=1588#section-0>
- Python 3 tutorial documentation: <https://docs.python.org/3/tutorial/>
- A Whirlpool Tour of Python by Jake VanderPlas: <https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf>
- The Coder's Apprentice by Pieter Spronock: <http://spronck.net/pythonbook/pythonbook.pdf>
- Python reference: <https://www.w3schools.com/python/python_reference.asp>
- Modules vs Packages vs Libraries in Python: <https://knowpapa.com/modpaclib-py/>
- Anaconda User Guide: <https://docs.anaconda.com/anaconda/user-guide/>
- Matplotlib documentation: <https://matplotlib.org/contents.html>
- 10 Minutes to Pandas: <https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html>
- Pyplot Tutorial: <https://matplotlib.org/users/pyplot_tutorial.html>
- Data visuaisation in Python: <https://medium.com/python-pandemonium/data-visualization-in-python-line-graph-in-matplotlib-9dfd0016d180>
- Stack Overflow forum: <https://stackoverflow.com>
- Python puzzles: <https://blog.finxter.com/>
- An Introduction to Version Control Using GitHub Desktop: <https://programminghistorian.org/en/lessons/getting-started-with-github-desktop>
- Mastering Markdown: <https://guides.github.com/features/mastering-markdown/>
- Markdownlint Rules: <https://github.com/DavidAnson/markdownlint/blob/v0.12.0/doc/Rules.md>