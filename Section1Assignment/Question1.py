
from datetime import datetime

# Question 1
# Library for current date
from datetime import date

# Ask for name and age
name = input("What is your name? ")
age = int(input("What is your age in years? "))

# Get todays date
today = date.today()

# Math to calculate what year you wil turn 100 years old
x = today.year + (100 - age)

# Print sentence
print(name + ", you will be 100 years old in the year " + str(x))