# BMI Calculator with Category


weight = 70   # in kg
height = 1.75  # in meters

# Calculate BMI
bmi = weight / (height ** 2)
bmi_rounded = round(bmi, 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("Your BMI is:", bmi_rounded)
print("BMI Category:", category)