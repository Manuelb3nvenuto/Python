#all this were copy and paste because i made them time ago, that's why there are not that many commits

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round( weight / height ** 2)

if bmi < 18.5:
  print(f"You are bmi is {bmi}, you are underweight.")  
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you have a overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")