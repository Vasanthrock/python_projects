from replit import clear

#HINT: You can call clear() to clear the output in the console.
from art import logo
  

person = False
while not person:
  print(logo)
  print("Welcome to the secret auction program.")
  Name = input("What is your name?: ")
  Bid = int(input("What's your bid?: $"))
  Name_list ={}
  Name_list[Name] = Bid
  remains=input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if remains == "no":
    person = True
    clear()
    large =0   
    winner =""
    for i in Name_list:
      if Name_list[i] > large:
        large = Name_list[i]
        winner = i  
    print(f"The winner is {winner} with a bid of ${large}")
  else:
    clear()
    

  