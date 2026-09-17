


#To greet the client
print("Welcome to the tipo calculator !")
#to insert the total of the bill
bill = float(input("What was the total bill: "))
#How much tip is gonna be delivered to the waiter
tip = float(input("How much tip would you like to give? 10, 12 , 15: "))
simplify_tip = (tip * .10) * (.10)
tip_amount = bill * simplify_tip
bill_tip = bill + tip_amount
#how many people is gonna be split the bill into
split = float(input("How many people to split the bill: "))
per_person = bill_tip / split
print(f"The total incluiding tip per person it's gonna be {per_person}")