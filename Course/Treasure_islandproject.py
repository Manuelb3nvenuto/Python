#Title
print(r'''
     _                                     _     _                 _ 
    | |                                   (_)   | |               | |
    | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
    | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
    | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
     \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
 

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')



print("Welcome to the treasure island, your mission it's to find the treasure")

answer = input("Let's test your luck, choose between left or right to know your future, so what would it be Right or Left: ").lower()

if answer == "right":
    print("Game Over, you have choose poorly")
else:
    print("You can continue with your path")

answer2 = input("We shall continue where we left it, now you have the option to swim or wait, choose wisely Swim or Wait: ").lower()

if answer2 == "wait":
    print("You have made it, you made the right decision, we will continue playing to find the treasure")
else:
    print("Game Over, you have choose death do your impatience")

answer3 = input("Now the options are right in front of you, you have a Red door and Blue one, what would it be your next move, Red or Blue or Yellow: ").lower()

if answer3 == "red":
    print("Game Over, it's looks good on the door, but not enough to let you win")
elif answer3 == "blue":
    print("Game Over, blue as the sky, blue as the ocean, so blue that you cannot play anymore, you choke your opportunity")
else:
    print("You have made it, by chossing the less popular (between those, in my opinion), you have made it, win win chicken winner, congrats on chossing the yellow one")
