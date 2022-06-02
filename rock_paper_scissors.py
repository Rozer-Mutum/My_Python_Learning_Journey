#***************
#creating rock paper scissors game in python
#***************
#taking ascii of rock, paper and scissors and assign in variable
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

print("Rock Paper Scissors Game")
data = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
#checking unwanted condition to discontinue the game if user provided invalid response
if (data>2 or data<0):
  print("Please provide a valid number to continue the game.")
#here the action for the game follows
else:
  print("You choose:")
  if (data==0):
    print(rock)
  elif (data==1):
    print(paper)
  else:
    print(scissors)
  #using random module to get random integer between 0 to 2
  computer = random.randint(0, 2)
  print("Computer choose:")
  if (computer==0):
    print(rock)
  elif (computer==1):
    print(paper)
  else:
    print(scissors)
  #here checking the user input and the randomly generated integer and checking user win or lose
  #rock beats scissors
  #scissors beats paper
  #paper beats rock
  if (data==computer):
    print("It is a Draw. Play again.")
  elif (data==0 and computer==1):
    print("You lose.")
  elif (data==0 and computer==2):
    print("You win!")
  elif (data==1 and computer==0):
    print("You win!")
  elif (data==1 and computer==2):
    print("You lose.")
  elif (data==2 and computer==0):
    print("You lose.")
  elif (data==2 and computer==1):
    print("You win!")