total_days = 365 * 90
total_weeks = 52 * 90
total_months = 12 * 90

current_age = int(input("What is your current age in years? \n"))
print(type(current_age))
print(f"You have {total_days - current_age * 365} days, {total_weeks - current_age * 52} weeks,"
      f" and {total_months - current_age * 12} months left to live")
