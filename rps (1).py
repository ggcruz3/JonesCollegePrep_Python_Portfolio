#Grecia
#In this programming assignment, you will create a simple Python program that allows the player to play the classic game of "Rock-Paper-Scissors" against the computer. The game involves selecting either rock, paper, or scissors and comparing the choices to determine the winner. The program should also keep track of the score and give the player the option to play again.

#Init
print("Hello welome to this Rock-Paper-Scissors game")
import random

player_score = 0
computer_score = 0
tie_score=0

#Func
def PScore():
    global player_score
    print(f"Players score: {player_score}")
def comp_score():
    global computer_score
    print(f"Computers score: {computer_score}")
def Tscore():
    global tie_score
    print(f"Tie score: {tie_score}")

def all():
    PScore()
    comp_score()
    Tscore()

def rps():
    computer = random.randint(1,1)
    if computer == 1:
        computer = "Rock"
    elif computer == 2:
        computer = "Paper"
    elif computer == 3:
        computer = "Scissors"

    while True:
        player = input("What would you like to pick: Rock, Paper, or Scissors: ")
        if computer == "Rock" and player == "Paper":
            global player_score
            global computer_score
            global tie_score
            print(f"{player} beats {computer} One point to the player! ")
            player_score = player_score + 1
            all()
            play = (input("Would you like to keep playing?: "))
            if play == "yes":
                print("Goodluck!")
            elif play == "no":
                print("Thank you for playing goodbye!")
                break

        elif computer == "Rock" and player == "Scissors":
            global computer_score
            global tie_score
            print(f"{computer} beats {player} One point to the Computer!")
            computer_score = computer_score + 1
            all()
            play = (input("Would you like to keep playing?: "))
            if play == "yes":
                print("Goodluck!")
            elif play == "no":
                print("Thank you for playing goodbye!")
                break


        elif computer == "Rock" and player == "Rock":
            global tie_score
            print(f"It is a tie, no one gets a point")
            tie_score = tie_score + 1
            all()
            play = (input("Would you like to keep playing?: "))
            if play == "yes":
               print("Goodluck!")

            elif play == "no":
                print("Thank you for playing goodbye!")
                break




#Main
rps()
