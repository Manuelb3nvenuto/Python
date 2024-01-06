#all this were copy and paste because i made them time ago, that's why there are not that many commits


import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


import random
 
random_name = random.randrange(len(names))
print(f"{names[random_name]} is going to buy the meal today!")