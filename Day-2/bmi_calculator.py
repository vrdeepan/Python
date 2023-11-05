height = float(input("Enter your height in meters?\n"))
weight = float(input("Enter your weight in kgs?\n"))

# we can add // as to convert to int instead of float
bmi = weight/height ** height

# round function to round of values
bmi = round(bmi, 2)

print ("Your BMI is " + str(bmi))