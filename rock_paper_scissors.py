# -*- coding: utf-8 -*-
"""Rock Paper Scissors.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kdRRoqkQNZstahd7vD6JE3NPxz6OPz1E
"""

import random

name = str(input("Please enter your name: "))
print("\nHello "+ name.capitalize() + ", Welcome to Rock-Paper-Scissors game!")

playerMove = input("\nPlease enter your move.\n\nRock?\nPaper?\nScissors?\n\n")
user_point = 0
computer_point = 0

def print_scores(cp, up):
  print("Computer Score: ", cp)
  print("Your Score: ", up)

while True:
  
  if playerMove.lower() == "rock" or playerMove.lower() == "paper" or playerMove.lower() == "scissors":
  
    possible_actions = ["rock", "paper", "scissors"]
    computerMove = random.choice(possible_actions)

    if playerMove.lower() == computerMove:
      print("\nIt's a tie!\n")
      print_scores(computer_point, user_point)

    elif playerMove.lower() == "rock":

      if computerMove == "paper":
        print("\nPaper beats Rock. You LOST!\n")
        computer_point += 1
        print_scores(computer_point, user_point)

      else:
        print("\nRock beats Scissors. You WON!\n")
        user_point += 1
        print_scores(computer_point, user_point)

    elif playerMove.lower() == "paper":

      if computerMove == "rock":
        print("\nPaper beats Rock. You WON!\n")
        user_point += 1
        print_scores(computer_point, user_point)

      else:
        print("\nScissors beats Paper. You LOST!\n")
        computer_point += 1
        print_scores(computer_point, user_point)

    elif playerMove.lower() == "scissors":

      if computerMove == "rock":
        print("\nRock beats Scissors. You LOST!\n")
        computer_point += 1
        print_scores(computer_point, user_point)

      else:
        print("\nScissors beats Paper. You WON!\n")
        user_point += 1
        print_scores(computer_point, user_point)

    answer = input("\nDo you want to play again?\nYES or NO?\n\n")

    while (answer.lower() != "yes" and answer.lower() != "no"):
      print("\nInvalid choice!")
      answer = input("\nDo you want to play again?\nYES or NO?\n\n")
      
    if answer.lower() == "no":
      print("\nOkay, GOODBYE!")
      break
    else:
      playerMove = input("GREAT:) Please enter your move.\n\nRock?\nPaper?\nScissors?\n\n")
    

  else:
    print("\nInvalid choice!")
    playerMove = input("\nPlease enter your move.\n\nRock?\nPaper?\nScissors?\n\n")