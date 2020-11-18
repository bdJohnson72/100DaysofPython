import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print(rock)
choices = ["scissors", "rock", "paper"]
user_choice = input("What is your move?\n")

computer_choice = random.choice(choices)
print(computer_choice)

user_wins = "You Win!!!"
user_loses = "Too bad the computer won"
draw = "It is a draw"

if user_choice == computer_choice:
    print(draw)
elif user_choice == "rock" and computer_choice == "paper":
    print(user_loses)
elif user_choice == "paper" and computer_choice == "scissors":
    print(user_loses)
elif user_choice == "scissors" and computer_choice == "rock":
    print(user_loses)
else:
    print("You win")



