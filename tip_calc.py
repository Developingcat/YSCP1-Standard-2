# tip_calculator.py
# A simple tip calculator to compute tip amount and total bill
print("#############################")
print("#############################")
print("-----------------------------")
print("Welcome to the Tip Calculator!")
print("-----------------------------")
print("#############################")
print("#############################")

bill = float(input("Please enter the bill amount here:$ "))

percent = int(input("Please enter the tip percentage here (i.e 15 for 15%, etc!): "))

# ABOVE ALL WORKS, to the point things are accepted anyways, which is okay. Because that is better then nothing. 


tip_percent = percent / 100

total_tip = bill * tip_percent 

total_bill = bill + total_tip 


print("-######################-")
print("-----Your Summary-----")
print(f"Bill Amount:","$",bill)
print(f"Tip Amount:","$",total_tip)
print(f"Total Bill Amount:","$",total_bill)
print("#-----------------------#")
print("Thank you for using tip calculator!")