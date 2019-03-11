# Title: Date time
# Description: Solution to problem 8 - program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.
# Context: Programming and Scripting, GMIT, 2019
# Author: Andrzej Kocielski
# Email: G00376291@gmit.ie
# Date of creation: 10-03-2019
# Last update: 10-03-2019

###

# External libraires
import datetime as dt

# Weekday - assigns day name (week_day_name) to day number (week_day)
week_day = dt.datetime.today().weekday()
if week_day == 0:
    week_day_name = "Monday"
elif week_day == 1:
    week_day_name = "Tuesday"
elif week_day == 2:
    week_day_name = "Wednesday"
elif week_day == 3:
    week_day_name = "Thursday"
elif week_day == 4:
    week_day_name = "Friday"
elif week_day == 5:
    week_day_name = "Saturday"
elif week_day == 6:
    week_day_name = "Sunday"
# print(week_day_name) # intermediate test


# Weekday - assigns month name (month_name) to month number (mn)
mn = dt.datetime.today().month
if mn == 1:
    month_name = "January"
elif mn == 2:
    month_name = "February"
elif mn == 3:
    month_name = "March"
elif mn == 4:
    month_name = "April"
elif mn == 5:
    month_name = "May"
elif mn == 6:
    month_name = "June"
elif mn == 7:
    month_name = "July"
elif mn == 8:
    month_name = "August"
elif mn == 9:
    month_name = "September"
elif mn == 10:
    month_name = "October"
elif mn == 11:
    month_name = "November"
elif mn == 12:
    month_name = "December"
# print(month_name) # intermediate test

# test
# print(week_day_name, month_name)

# definition of today's day as ordinal number
today_day = dt.datetime.today().day

if today_day == 1 or today_day == 21 or today_day == 31:
    today_ordinal = str(today_day) + "st"
elif today_day == 2 or today_day == 22:
    today_ordinal = str(today_day) + "nd"
elif today_day == 3 or today_day == 23:
    today_ordinal = str(today_day) + "rd"
else:
    today_ordinal = str(today_day) + "th"

# print(today_ordinal) # intermediate test

# definition of a new variable holding the day and time in requested format
# formatting with the use of f"{}" notation
full = f"{week_day_name}, {month_name} {today_ordinal}"
print(full)

# print(dt.datetime.now())
