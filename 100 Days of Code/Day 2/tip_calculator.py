print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))/100
persons = int(input("How many people to split the bill? "))

final_bill = "{:.2f}".format(bill + (bill * tip_percentage))

print(f"Each person should pay ${final_bill}")