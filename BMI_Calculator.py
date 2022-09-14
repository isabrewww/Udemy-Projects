# Create variables and assign them with user input
# This calculator uses meter and kilograms
height = float(input("Enter height in m: "))
weight = float(input("Enter weight in kgs: "))

# Calculate BMI
bmi = weight / height ** 2

# Print output
print("Your BMI is:", int(bmi))