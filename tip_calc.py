# tip_calculator.py
# A simple tip calculator to compute tip amount and total bill

# Opening message 

print("#############################")
print("#############################")
print("-----------------------------")
print("Welcome to the Tip Calculator!")
print("-----------------------------")
print("#############################")
print("#############################")
print("\n")

# Variables / inputs 

bill = float(input("Please enter the bill amount here:$ "))

percent = int(input("Please enter the tip percentage here (i.e 15 for 15%, etc!): "))

# Math stuff, right from the pseudotext.

tip_percent = percent / 100

total_tip = bill * tip_percent 

total_bill = bill + total_tip 

# Display Summary

print("\n")
print("-######################-")
print("#------Your Summary------#")
print("#------------------------#")
print(f"Bill Amount:","$",bill)
print(f"Tip Amount:","$",total_tip)
print(f"Total Bill Amount:","$",total_bill)
print("#------------------------#")
print("#------------------------#")
print("\nThank you for using the tip calculator!")

