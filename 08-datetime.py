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

# Weekday - assigns day name to day number
week_day = dt.datetime.today().weekday()
if week_day == 0:
    week_day_name = "Monday,"
elif week_day == 1:
    week_day_name = "Tuesday,"
elif week_day == 2:
    week_day_name = "Wednesday,"
elif week_day == 3:
    week_day_name = "Thursday,"
elif week_day == 4:
    week_day_name = "Friday,"
elif week_day == 5:
    week_day_name = "Saturday,"
elif week_day == 6:
    week_day_name = "Sunday,"
# print(week_day_name)


# Weekday - assigns day name to day number
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
# print(month_name)

# test
print(week_day_name, month_name)

print(dt.datetime.now())
