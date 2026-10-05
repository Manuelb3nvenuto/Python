print("Welcome to Python Milkshakes Deliveries!")

size = input("What size do you want the milshake to be S, M, L: ")

foam = input("Do you want foam in your milshake? Y or N: ")

extra_sparkles = input("Would you want extra sparkles Y or N: ")

bill = 0

# todo: work out how much they need to pay based on their size choice
if size == "S":
    bill = 15
    print("The size it's gonna be small for your milkshake")

elif size == "M":
    bill = 20
    print("The size it's gonna be medium for your milkshake")

else:
    bill = 25 
    print("The size it's gonna be large for your milkshake")


# todo: work out how much to add to their bill based on their foam choice
if foam == "Y":
    bill += 2
    print("It will be added to your milshake and it will be charge 2 more dollars")

else:
    bill += 0
    print("It won't be added nothing to your beverage")

# todo: work out their final amount wether if they want extra sparkles 
if extra_sparkles == "Y":
    bill += 1
    print("Ok, the orden it's gonna have extra spakles $1 dollar will be added to the final bill")
else:
    print("We understand you don't wanna get extra sparkles so nothing will be added to the final bill")

#At the end of the code you will a summary of what and how much the client spend on the order and what was the order

print(f"The final amount it's gonna be around {bill}, of the total of the order.")