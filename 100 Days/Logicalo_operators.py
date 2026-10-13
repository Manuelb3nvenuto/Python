#when you combine two A AND B both have to be true in order to this to be correct/True
#here's another example with identations
print("Welcome to the rollercoaster: ")

height = int(input("What is your height in cm: "))
bill = 0

if height >= 120: 
    print("You can ride the rollercoaster")
    #this is if else live inside the other one, this is a nested if 
    age =  int(input("What is your age: "))
    if age <= 12:
        bill = 5
        print("Please pay $5")
    #if the age its les than 12, the elif will catch the number, it can be use between the if and else as much as you want
    elif age <=18:
        bill = 7
        print("Please pay $7")
    elif age == 45 and 55:
        bill = 0
        print("Please pay $0, you are going to a rough path")

    else: #if tge elif it's not true the next it's gonna be the else, it's gonna depend on the total of elif you put on the code.
        bill = 12
        print("Please pay $12")

    wants_photo = (input("Do you want a photo taken ? Type Y for Yes and N for no: "))

    if wants_photo == "Y":
        #print(str(f"You will be added $3 more dolar to your account, so it will be a total of {bill}"))
        bill += 3
        print(str(f"You will be added $3 more dolar to your account, so it will be a total of {bill}"))

    else:
        print(f"Your final bill will be {bill} dollars")
else:
    print("Sorry you have to grow taller so you can ride")