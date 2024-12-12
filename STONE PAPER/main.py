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

#Write your code below this line 👇
import random
store = [rock, paper, scissors]
ran_num = random.randint(0,(len(store))-1)
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_input >=3 or user_input < 0:
  print("You typed an invalid number, you lose!")
else:
 print(store[user_input])
 print(f"computer chose: \n {store[ran_num]}")

 if user_input ==0 and ran_num ==1:
    print("You lose")
 elif user_input ==1 and ran_num ==2:
    print("You lose")
 elif user_input ==2 and ran_num ==0:
    print("You lose")
 elif user_input == ran_num:
    print("Draw")
 else:
    print("you win")
    
