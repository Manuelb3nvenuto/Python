#import random module
import random
import ModuleRockPaper

#Obtain the random name from the list
rock = ModuleRockPaper.rock
paper = ModuleRockPaper.paper
scissors = ModuleRockPaper.scissors

#Player Intro
player_choice = input("Welcome to the game, choose between rock, paper, scissors: ").lower()

random_computer_choice = random.choice([ModuleRockPaper.rock,ModuleRockPaper.paper,ModuleRockPaper.scissors])

#print(f"Computer choice againts human player is gonna be {random_computer_choice}")

#What happens if player choose something
if player_choice == "rock":
    print(f"Players choice is {rock} against {random_computer_choice}")
elif player_choice == "paper":
    print(f"Players choice is {paper} against {random_computer_choice}")
elif player_choice == "scissors":
    print(f"Players choice is {scissors} against {random_computer_choice}")
else:
    print("That was not a valid option")


#Who decides the winner?
if player_choice == "rock" and random_computer_choice == ModuleRockPaper.rock:
    print("Player and computer draws")
elif player_choice == "rock" and random_computer_choice == ModuleRockPaper.paper:
    print("Player loses")
elif player_choice == "rock" and random_computer_choice == ModuleRockPaper.scissors:
    print("Player wins")
elif player_choice == "paper" and random_computer_choice == ModuleRockPaper.rock:
    print("Player wins")
elif player_choice == "paper" and random_computer_choice == ModuleRockPaper.paper:
    print("Player and computer draws")
elif player_choice == "paper" and random_computer_choice == ModuleRockPaper.scissors:
    print("Player losses")
elif player_choice == "scissors" and random_computer_choice == ModuleRockPaper.rock:
    print("Player losses")
elif player_choice == "scissors" and random_computer_choice == ModuleRockPaper.paper:
    print("Player wins")
elif player_choice == "scissors" and random_computer_choice == ModuleRockPaper.scissors:
    print("Player and computer draws")

