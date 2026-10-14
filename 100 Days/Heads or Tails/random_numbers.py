#import random
#import my_module
#random_integer = random.randint(1, 10)

#print(random_integer)

#print(my_module.my_favourite_number)

#functions use the () in order to carry out the action they need to preform

#random_number0_to_1 = int(random.random() * 10)

#print(random_number0_to_1)


#other function ramdom numbers between a range

#random_float = random.uniform(1,10)

#print(random_float)

#Head or tails exercise my solution

#import random

#import Headstails

#random_result_headstails = random.choice([Headstails.Heads, Headstails.Tails])

#print(random_result_headstails)



#Other type of solution from the course

import random

random_result_with_if = random.randint(0, 1)

if random_result_with_if == 0:
    print("Heads")
else:
    print("Tails")