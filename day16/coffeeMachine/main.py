from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine = CoffeeMaker()
moneyBox = MoneyMachine()
menu = Menu()

machine_running = True

while machine_running:

    choice = input(f"Our menu: {menu.get_items()} \nWhat would you like? ").lower()

    if choice == "off":
        machine_running = False
        print("Shutingdown...")
    elif choice == "report":
        machine.report()
        moneyBox.report()
    else:
        drink = menu.find_drink(choice)
        if machine.is_resource_sufficient(drink) and moneyBox.make_payment(drink.cost):
            machine.make_coffee(drink)
            