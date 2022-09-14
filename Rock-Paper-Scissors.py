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

user_choice = input("Choose 1 for ROCK, 2 for PAPER, or 3 for SCISSORS: ")
options = [rock, paper, scissors]
computer_choice = random.choice(options)

if user_choice == 1:
    user_choice = rock
elif user_choice == 2:
    user_choice = paper
elif user_choice == 3:
    user_choice = scissors

print("\nYou chose:\n")
print(user_choice)
print("")
print("Computer chose:\n")
print(computer_choice)
print("")

if user_choice == rock:
    if computer_choice == scissors:
        user_choice = 4
    else:
        user_choice = 1
elif user_choice == paper:
    user_choice = 2
elif user_choice == scissors:
    user_choice = 3

if computer_choice == rock:
    if user_choice == 3:
        computer_choice = 4
    else:
        computer_choice = 1
elif computer_choice == paper:
    computer_choice = 2
elif computer_choice == scissors:
    computer_choice = 3

if user_choice == computer_choice:
    print("IT'S A TIE!")
elif user_choice > computer_choice:
    print("YOU WIN!")
else:
    print("YOU LOSE...")