print("Welcome to the tip calculator")
totalBillStr = input("What was the total bill?\n")
totalBill = float(totalBillStr)
numPeopleStr = input("How many people are splitting the bill?\n")
numPeople = int(numPeopleStr)
percentageTipStr = input("What percentage tip would you like to give? 10%, 12%, or 15%\n")
percentageTip = int(percentageTipStr)
totalTip = (percentageTip/100) + 1
totalPayment = totalBill*totalTip
eachPerson = totalPayment/numPeople
eachPersonStr = str(eachPerson)
print("Each person should pay: $" + eachPersonStr)
