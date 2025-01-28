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
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors "))
comp_choice = random.randint(0,2)

images = [rock,paper,scissors]
if user_choice >= 0 and user_choice <= 2:
    print("You chose:")
    print(images[user_choice])

print("Computer chose:")
print(images[comp_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
if user_choice == 0 and comp_choice == 2:
    print("User wins!")
elif comp_choice == 0 and user_choice == 2:
    print("Computer wins!")
elif comp_choice > user_choice:
    print("Computer wins!")
elif user_choice > comp_choice:
    print("User wins!")
elif user_choice == comp_choice:
    print("Draw")
