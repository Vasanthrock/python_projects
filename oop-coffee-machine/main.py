import coffee_maker
from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
menu1 = Menu()
machine = MoneyMachine()
flag= 1
while flag:
    choice = input(f"What would you like? {menu1.get_items()}:")

    if choice=="report":
        maker.report()
        machine.report()
    elif choice== "off":
        flag=0
    else:
        drink = menu1.find_drink(choice)
        if maker.is_resource_sufficient(drink):
            if machine.make_payment(drink.cost):
                if maker.make_coffee(drink):
                    print("finish")
