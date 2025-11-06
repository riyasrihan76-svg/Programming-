days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month = int(input("Enter the month number (1-12): "))

if month >= 1 and month <= 12:
    print("Number of days: " + str(days_in_month[month]))
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
