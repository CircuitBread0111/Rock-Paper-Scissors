#////////////////////////////
#   Rock_Paper_Scissors.py
# Author: Jerrin C. Redmon
# Date: May 22, 2022
#////////////////////////////

# Description: A game of rock, paper, scissors against the computer

#Imports
import sys
import random as ran
import time

#Main function
def main():
    user_choice = user_input()
    computer_choice = computer_input()
    game_logic(user_choice,computer_choice)
    game = True
    while game == True:

        ask = input("Do you want to play again? [y/n]")
        if ask == "y":
            main()
        else:
            break


#Function for setting up the game
def game_setup():
    yes = input("Would you like to play Rock, Paper, Scissors [y/n] : ")
    if yes == "y":
        print("Let's Play!")
    else:
        sys.exit("Ok, maybe next time")
game_setup()


#Function for the user input for the game
def user_input():
    user_choice = input("Player![Pick Rock, Paper, or Scissors]:  ")
    if user_choice == "Rock":
        print("User picks", user_choice)
        return user_choice
    if user_choice == "Paper":
        print("User picks", user_choice)
        return user_choice
    if user_choice == "Scissors":
        print("User picks", user_choice)
        return user_choice
    else:
        print("Try again")


#Function for the computer's input of the game
def computer_input():
    print("Computer Thinking...")
    time.sleep(1)
    game_choices = ("Rock", "Paper", "Scissors")
    computer_choice = ran.choice(game_choices)
    print("Computer picks", computer_choice)
    if computer_choice == "Rock":
        return computer_choice
    if computer_choice == "Paper":
        return computer_choice
    if computer_choice == "Scissors":
        return computer_choice


#Function of game logic to determine a winner or tie
def game_logic(user_choice,computer_choice):
        if user_choice == "Rock" and computer_choice == "Scissors":
            print("You win the round")
        elif user_choice == "Rock" and computer_choice == "Paper":
            print("Computer wins the round")
        elif user_choice == "Rock" and computer_choice == "Rock":
            print("Tie! Try Again")

        elif user_choice == "Paper" and computer_choice == "Scissors":
            print("Computer wins the round")
        elif user_choice == "Paper" and computer_choice == "Paper":
            print("Tie! Try Again")
        elif user_choice == "Paper" and computer_choice == "Rock":
            print("You win the round")

        elif user_choice == "Scissors" and computer_choice == "Scissors":
            print("Tie! Try Again")
        elif user_choice == "Scissors" and computer_choice == "Paper":
            print("You win the round")
        elif user_choice == "Scissors" and computer_choice == "Rock":
            print("Computer wins the round")

main() #Program Execution
