# Snake Water Gun Game
# The snake drinks the water, the gun shoots the snake, and gun has no effect on water.

# using random.choice() function
import random

list = ["Snake", "Water", "Gun"]
# print("Number of Rounds: 5")
# 7 times to run the game and print the result    
computer = random.choice(list)
player = False
cpu_score = 0
player_score = 0
i = 0
while i <= 7:
    print("\nRound No.:",i)
    i +=1
    player = input("\nSnake, Water or Gun?").capitalize()
    # Conditions for Snake, Water and Gun
    if player == computer:
        print("\nTie!")
    elif player == "Snake":
        if computer == "Water":
            print("\nYou Win.")
            player_score +=1
        else:
            print("\nComputer Win.")
            cpu_score +=1
    elif player == "Water":
        if computer == "Gun":
            print("\nYou Win.")
            player_score += 1
        else:
            print("\nComputer Win.")
            cpu_score +=1
    elif player == "Gun":
        if computer == "Snake":
            print("\nYou win.")
            player_score +=1
        else:
            print("\nComputer Win.")
            cpu_score +=1
    else:
        print("\nInvalid play, Enter Your Choice Again")
        computer = random.choice(list)
    
    if player_score > cpu_score:
        print("Your Final Score is",player_score, "You won finally")
    else:
        print("Computer's Final Score is",cpu_score,"Computer won")