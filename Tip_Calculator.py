# Assign variables with user input
print("Enter the following information to calculate your tip")
initialBill = float(input("Total bill: $"))
tipPercentage = (float(input("Tip %: ")) / 100)
numPeople = int(input("Number of people: "))

# Calculate tip
payPerPerson = "{:.2f}".format(initialBill * (tipPercentage + 1) / numPeople)
tipTotal = float(initialBill * tipPercentage)
finalBill = "{:.2f}".format(tipTotal + initialBill)

# Output
print(f"The tip total is: ${tipTotal:.2f}.")
print(f"The final bill is: ${finalBill}.")
print(f"Amount per person: ${payPerPerson}")