


#To greet the client
#print("Welcome to the tipo calculator !")
#to insert the total of the bill
#bill = float(input("What was the total bill: "))
#How much tip is gonna be delivered to the waiter
#tip = float(input("How much tip would you like to give? 10, 12 , 15: "))
#simplify_tip = (tip * .10) * (.10)
#tip_amount = bill * simplify_tip
#bill_tip = bill + tip_amount
#how many people is gonna be split the bill into
#split = float(input("How many people to split the bill: "))
#per_person = bill_tip / split
#print(f"The total incluiding tip per person it's gonna be {per_person}")






#Second try of the calculator
print("Welcome to the tip calculator!")

bill_amount = float(input("What was the total bill: "))

tip_total = float(input("How much percentage of tip are you gonna give 10, 12, 15: "))

calulation_tip_percentage = (bill_amount * .10) #good

bill_and_cal_tip_percentage = (bill_amount + calulation_tip_percentage) #good

split_total = float(input("In how many people it's gonna be split into: "))

calculation_bill_tip_person = (calulation_tip_percentage  / split_total)

tip_per_person_singular = (bill_and_cal_tip_percentage / split_total)

print(f"The total for each person gonna be {tip_per_person_singular} per person with tip added, and if you prefer what was the tip given by each is { calculation_bill_tip_person} , thanks for been with us in this beautiful evening")
