# Assign variables to user input
userAge = int(input("How many years old are you? "))

# Calculate time approx time until 90 yrs
years = 90 - userAge
months = years * 12
weeks = years * 52
days = years * 365

print(f"You have approximately: \n{days} days, \n{weeks} weeks, or \n{months} months \nuntil you turn 90 years old.")