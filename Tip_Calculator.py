# Tip calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? £"))
tip = int(input("What percentage tip would you like to give? e.g. 10 12 15 "))
people = int(input("How many people to split the bill? "))
# Equation to calculate the total bill including tip, based on values input above
total_bill = bill * (tip / 100) + bill
# Calculate amount per person based on total bill
final_amount = total_bill / people
print(f"The total bill is: £{total_bill}")
print(f"Each person needs to pay: £{final_amount}")