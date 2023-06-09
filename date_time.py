# Datetime Basics 1

# Python datetime module

# creating datetime objects in Python, including printing special string formatting of time

# Task 1

from datetime import datetime

current_datetime = datetime.now()
year = current_datetime.strftime("%Y")

print(year)

#-----------------------------------------------------------------

# Task 2

#  print out the current week day
from datetime import datetime

some_date = datetime(2023, 6, 9)
week = some_date.weekday()

print(week)

#-----------------------------------------------------------------

# Task 3

# determine whether the year 2021 is a leap year

import calendar

year = 2021

if calendar.isleap(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#---------------------------------------------------------------

# Task 4

# convert a user provided string into a datetime object

from datetime import datetime

date_as_string = "Feb 14 2021 8:30AM"
datetime_object = datetime.strptime(date_as_string, "%b %d %Y %I:%M%p")
formatted_date = datetime_object.strftime("%Y-%m-%d %H:%M:%S")

print(formatted_date)

#-----------------------------------------------------------------

# Task 5

# program that calculates the number of days between two given dates

from datetime import datetime

# Input the two dates from the user
date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")

# Convert the input strings to datetime objects
date1_convert = datetime.strptime(date1, "%Y-%m-%d")
date2_convert = datetime.strptime(date2, "%Y-%m-%d")

# Calculate the number of days between the two dates
delta = date2_convert - date1_convert
num_days = delta.days

# Display the result
print("The number of days between", date1, "and", date2, "is", num_days)

#-----------------------------------------------------------------

# Task 6

from datetime import datetime

# Input the hours of two dates from the user
date1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

# Convert the input strings to datetime objects
date1_convert = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
date2_convert = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

# Calculate the number of hours
delta = date2_convert - date1_convert
num_hours = delta.total_seconds() / 3600

# Display the result
print("The number of hours between", date2, "and", date1, "is:", num_hours, "hours")







