import random
from ART import logo,vs
from game_data import data
import os

def random_account ():
    return random.choice(data)

def format (account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f" {name}, a {description}, from {country}."

def compare(a,b):
    if a > b:
        return "A"
    else:
        return "B"
def clear_console():
    os.system('cls')

def game():
    ran_A = random_account()

    ran_B = random_account()
    flag= 0
    score = 0

    while not flag:

        print(logo)
        if score >0:
            print(f"yor are right! current score: {score}")

        print(f" compare A :{format(ran_A)}")

        print(vs)

        print(f" Against B :{format(ran_B)}")

        A = ran_A.get("follower_count")
        B = ran_B.get("follower_count")
        calc_follwers = compare(A,B)
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if choice == calc_follwers:
            score+=1
            ran_A=ran_B
            ran_B = random_account()
            clear_console()
        else:
            clear_console()
            print(logo)
            print(f"sorry that's wrong you're Final Score is {score}")
            flag =1
game()