from datetime import date

# datetime is a Python module for working with dates and times.
# date is a class inside datetime that represents a date (year, month, day).

# Set your birthday here (month and day)
birth_month = 7   # July
birth_day = 15    # 15th

today = date.today()

# Birthday this year
next_birthday = date(today.year, birth_month, birth_day)

# If birthday already passed this year, set for next year
if next_birthday < today:
    next_birthday = date(today.year + 1, birth_month, birth_day)

# Difference in days
days_left = (next_birthday - today).days

# Convert days into weeks and approximate months
weeks_left = days_left // 7
months_left = days_left // 30  # approximate

print("Time left until your next birthday:")
print("Days:", days_left)
print("Weeks:", weeks_left)
print("Months (approx):", months_left)