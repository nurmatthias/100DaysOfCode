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

choices = [rock, paper, scissors]

cpuInput = random.randint(1, 3)
cpuChoice = choices[cpuInput - 1]

playerInput = int(input("What do you choose? 1 for Rock, 2 for Paper or 3 for Scissors.\n"))
if playerInput <= 3 and playerInput >= 1:
    playerChoice = choices[playerInput - 1]

    print(f"You choose: \n{playerChoice}")
    print(f"CPU choose: \n{cpuChoice}")

    if playerInput == 1 and cpuInput == 3:
        print("You win!")
    elif cpuInput == 1 and playerInput == 3:
        print("You lose")
    elif cpuInput > playerInput:
        print("You lose")
    elif playerInput > cpuInput:
        print("You win!")
    elif cpuInput == playerInput:
        print("It's a draw")
else:
    print("Nope, invalid number, you lose!")