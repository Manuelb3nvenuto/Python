#all this were copy and paste because i made them time ago, that's why there are not that many commits

for number in range(1,101):
  if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
  elif number % 5 == 0:
    print("Buzz")
  elif number % 3 == 0:
    print("Fizz")
  else:
    print(number)