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
options=["rock","paper","scissor"]
computer_choice=random.choice(options)
player_choice=input("select rock or paper or scissor ")
if player_choice=="rock":
    print("players choice\n", rock)
    if computer_choice=="rock":
        print(f"computers choice is {computer_choice}\n{rock} , so it is a draw")
    elif computer_choice=="scissor":
        print(f"computers choice is {computer_choice}\n{scissors} , so player won")
    else:
        print(f"computers choice is {computer_choice}\n{paper} , so computer won")
elif player_choice=="paper":
    print("players choice\n", paper)
    if computer_choice=="paper":
        print(f"computers choice is {computer_choice}\n{paper} , so it is a draw")
    elif computer_choice=="rock":
        print(f"computers choice is {computer_choice}\n{rock} , so player won")
    else:
        print(f"computers choice is {computer_choice}\n{scissors} , so computer won")
else :
    print("Player choice\n", scissors)
    if computer_choice == "scissor":
        print(f"computers choice is {computer_choice}\n{scissors} , so it is a draw")
    elif computer_choice == "rock":
        print(f"computers choice is {computer_choice}\n {rock} , so computer won")
    else:
        print(f"computers choice is {computer_choice}\n{paper} , so player won")