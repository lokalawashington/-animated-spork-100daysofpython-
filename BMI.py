height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

height_new = float(height)
weight_new = int(weight)

BMI = (weight_new/(height_new * height_new))
print(BMI)

BMI_as_int = int(BMI)
print(BMI_as_int)

