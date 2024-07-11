import random

computer_choice = random.choice(["scissors", "paper", "rock"])
user_choice = input("rock, paper or scissors?\n")

if computer_choice == user_choice:
    print('TIE, computer chose ' + computer_choice)
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('WIN, computer chose ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN, computer chose ' + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('WIN, computer chose ' + computer_choice)
else:
    print('LOSE, computer chose ' + computer_choice)