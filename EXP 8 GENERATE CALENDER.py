# Program to generate a calendar for the given month and year

import calendar

# Input month and year from user
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# Display the calendar
print("\nHere is the calendar:\n")
print(calendar.month(year, month))
