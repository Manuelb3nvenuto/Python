#NESTED IF/ELSE statement, once the first condition it's past then you can have another statment in that condition
#print("Welcome to the rollercoaster: ")

#height = int(input("What is your height in cm: "))

#if height >= 120: 
    #print("You can ride the rollercoaster")
    #this is if else live inside the other one, this is a nested if 
    #age =  int(input("What is your age: "))
    #if age <= 18:
        #print("Please pay $7")
    #else:
        #print("Please pay $12")
#else:
    #print("Sorry you have to grow taller so you can ride")



#there are another possibility instead of only one condition we can use elif condition and do as many as we want

#print("Welcome to the rollercoaster: ")

#height = int(input("What is your height in cm: "))

#if height >= 120: 
    #print("You can ride the rollercoaster")
    #this is if else live inside the other one, this is a nested if 
    #age =  int(input("What is your age: "))
    #if age <= 12:
        #print("Please pay $5")
    #if the age its les than 12, the elif will catch the number, it can be use between the if and else as much as you want
    #elif age <=18:
        #print("Please pay $7")
    #else:#if tge elif it's not true the next it's gonna be the else, it's gonna depend on the total of elif you put on the code.
        #print("Please pay $12")
#else:
    #print("Sorry you have to grow taller so you can ride")




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
    else:#if tge elif it's not true the next it's gonna be the else, it's gonna depend on the total of elif you put on the code.
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