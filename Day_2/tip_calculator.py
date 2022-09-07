# Tip Calculator
# Ask for total bill
# Ask for number of people to split the bill with
# Ask for percentage of tip to include
# Display payment for an individual

print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill?\n"))
people_count = int(input("How many people to split the bill?\n"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12 or 15?\n"))

total_bill = bill + (tip_percent / 100 * bill)
individual_pay = total_bill / people_count

print(f"\nEach person should pay: {round(individual_pay, 2)}")
