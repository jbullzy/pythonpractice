# Tip Calculator

bill = int(input("How much was the bill? "))
tip_percentage = (int(input("And how much do you want to tip? ")) / 100)

tip = bill * tip_percentage
total = tip + bill

print(f"So the tip would be {tip}.")
print(f"And the total bill would be {total}.")