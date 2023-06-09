[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/2fFT7_wO)
# Datetime Basics 1

## Python datetime module

In this exercise, we will focus on creating datetime objects in Python, including printing special string formating of time.

- create a variable that stores the current time
- print out current year
- Print the weekday of the week
- Write a program to determine if a provided date is a leap year
- Convert a string into a datetime object

##

## Usage

A datetime module can be used to represent a time, we shall use the `.now()` method to get the current year.

```
from datetime import datetime
current_datetime = datetime.now()
```

To see what you can possibly do with the instance of datetime, experiment with the existing methods.

```
dir(current_datetime)
```

##

## Tasks

###

### Task 1

Using the variable called `current_datetime`, print out the current year

- Your result should look like this :

```
2014
```

###

### Task 2

Using the variable called `some_date`, print out the current week day

`some_date = datetime(2021, 7, 14)`

- Your result should look like this - (a number between 0 and 6)

```
2
```

###

### Task 3

Write a Python program to determine whether the year 2021 is a leap year.

- Your result should look like this:

```
2021 is not a leap year
```

###

### Task 4

Your task is to convert a user provided string into a datetime object.

Our test input looks like this:

```
from datetime import datetime
date_as_string = "Feb 14 2021 8:30AM"
```

- Your result should look like this:

```
2021-02-14 08:30:00
```

### Task 5 
Write a Python program that calculates the number of days between two given dates. You can ask the user to input the two dates and then display the number of days between them.
- Your result should look like this

```
The number of days between 2023-06-01 and 2023-06-08 is 7
```

### Task 6 
Write a Python program that calculates the number of hours between two given datetimes. You can ask the user to input the two dates and then display the number of hours between them.

- Your result should look like this

```
The number of hours between 2023-06-09 10:00:00 and 2023-06-09 15:30:00 is: 5.5 hours
```
