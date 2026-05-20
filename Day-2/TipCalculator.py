print("Welcome to the tip calculator!")
tBill = int(input("What was the total bill? $"))
userTipPercent = int(
    input("How much tip would you like to give? 10, 12 or 15? "))
calculatedTbill = tBill + ((userTipPercent/100)*tBill)
peopleToSplit = int(input("How many people to split the bill?: "))
print(f"Each person has to pay: ${round(calculatedTbill/peopleToSplit, 2)}")
