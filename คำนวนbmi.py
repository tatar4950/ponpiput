weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"