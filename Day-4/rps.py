import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print(
    "Welcome to Rock Paper Scissors!\n\nType 0 for rock, 1 for paper and 2 for scissors."
)
player_choice = int(input())
comp_choice = random.randint(0, 2)
choices = [rock, paper, scissors]

if player_choice == comp_choice:
    print("You chose:")
    print(choices[player_choice])
    print("Computer chose:")
    print(choices[comp_choice])
    print("It's a tie.\nPlease try again.")
elif (player_choice - comp_choice) % 3 == 1:
    print("You chose:")
    print(choices[player_choice])
    print("Computer chose:")
    print(choices[comp_choice])
    print("You win.")
else:
    print("You chose:")
    print(choices[player_choice])
    print("Computer chose:")
    print(choices[comp_choice])
    print("Computer wins.")
