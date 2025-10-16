height = float(input("Height: "))
weight = float(input("Weight: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are normal.")
else:
    print("You are overweight.")
