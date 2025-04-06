MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def reduction(choice):
    for i in MENU[choice]["ingredients"]:
        resources[i] -= MENU[choice]["ingredients"][i]
    print(f"Here is your {choice} ☕️. Enjoy!")
def cash(choice):
    global profit
    print("please insert coins.")
    quaters = int(input("how many quaters?: "))*0.25
    dimes = int(input("how many dimes?: "))*0.10
    nickles = int(input("how many nickles?: "))*0.05
    pennies = int(input("how many pennies?: "))*0.01
    total = round(quaters+dimes+nickles+pennies,2)
    return total

def check_sufficient(choice):
    for i in MENU[choice]["ingredients"]:
        if resources[i] < MENU[choice]["ingredients"][i]:
            print(f"Sorry there is not enough {i}.")
            return False
        else:
            return True



flag = 0
while not flag:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif choice == "off":
       flag=1
    else:
        if check_sufficient(choice):
            total = cash(choice)

            if total < MENU[choice]["cost"]:
                print ("sorry that's not enough. Money refunded.")
            else:
                balance = total - MENU[choice]["cost"]
                profit += MENU[choice]["cost"]
                print(f"here is your ${balance} change")
                reduction(choice)