from datetime import datetime
from datetime import date

# Define the target date
target_date = date(2025, 7, 8)

# Get the current date
current_date = date.today()

# Calculate the difference between the two dates
difference = target_date - current_date

# Print the number of days until the target date
print(f"There are {difference.days} days until July 8th, 2025.")

