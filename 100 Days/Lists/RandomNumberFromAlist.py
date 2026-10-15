#Import the random module
import random
#Make a list
Names = ["Nailea","Bruno","Carlos","Fernanda","Alice","Eliza","Itzel","Merida","Juan","Julieta"]
#Obtain the random name from the list
RandomNames = random.choice(Names)

print(RandomNames)



#Solution from the course

random_index = random.randint(0,9)

print(Names[random_index])

