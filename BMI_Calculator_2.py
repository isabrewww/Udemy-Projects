height_M = float(input("Enter your height in meters: "))
weight_Kg = float(input("Enter your weight in kilograms: "))
bmi = float(round(weight_Kg / height_M ** 2, 2))

if bmi < 18.5:
    print(f"BMI: {bmi}\nYou are underweight.")
elif bmi < 25:
    print(f"BMI: {bmi}\nYou are a healthy weight.")
elif bmi < 30:
    print(f"BMI: {bmi}\nYou are overweight.")
elif bmi < 35:
    print(f"BMI: {bmi}\nYou are obese.")
else:
    print(f"BMI: {bmi}\nYou are clinically obese.")