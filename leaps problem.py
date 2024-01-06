#all this were copy and paste because i made them time ago, that's why there are not that many commits
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print ("Leap year.")
        else:
            print("Not leap.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")