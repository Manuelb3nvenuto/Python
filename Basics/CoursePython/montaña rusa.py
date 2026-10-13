#all this were copy and paste because i made them time ago, that's why there are not that many commits

print("Welcome to the rollarcoaster!")
height = int(input("What is your height in cm? "))
bill = 0 
if height >= 120:
  print("You can ride the mountain")  
  age =  int(input("What is your age? "))
  if age <= 12:
    bill = 5
    print("Please pay $5.")
  elif age <= 18:
    bill = 7
    print("Please pay $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to br ok. Hvae a free ride on us")
  else:
    bill = 12
    print("Please pay $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
      bill += 3

    print(f"Your final bill is {bill}. ")
else:
  print("Sorry , you have to be this tall (120+) to be able to ride the mountain.")