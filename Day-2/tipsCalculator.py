print("Welcome to Tips calculator")
bill_value = float(input("Enter the final bill: "))
tip_percent = int(input("Enter the percent of tip to calculate: "))
split = int(input("Enter the number of people to split this: "))

tip_value = (bill_value * tip_percent)/100

total_bill = bill_value + tip_value

print(f"The final bill is {total_bill}")

print(f"Split for each person is {total_bill/split}")