height = float(input("Enter your height in meters : "))
weight = float(input("Enter your weight in kgs : "))

bmi = weight / (height ** 2)
print("BMI :", bmi)

if bmi <= 18.4:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are healthy!")
elif bmi <= 29.9:
    print("You are over weight.")
elif bmi <= 34.9:
    print("You are severly overweight.")
else:
    print("You are obese.")