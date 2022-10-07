import random


#choices for the game
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

game = [rock, paper, scissors]

#players choice options

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game[choice])
print("Player choice: \n")

#computer random
print("Computer choice: ")
comp_choice = random.randint(0, 2)
print(game[comp_choice])



if choice == 0 and comp_choice == 2:
    print("You win")
elif choice == 2 and comp_choice == 0:
    print("You lose")
elif comp_choice > choice:
    print("You lose")
elif choice > comp_choice:
    print("You win")
elif choice == comp_choice:
    print("It's a draw")





