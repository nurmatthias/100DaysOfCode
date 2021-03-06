from coffe_machine_menu import MENU, resources


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffe: {resources['coffee']}g")
    print(f"Money: ${'{:.2f}'.format(fond)}")

def check_receipt(receipt):
    receipt_to_make = MENU[receipt]

    for ingredien in receipt_to_make["ingredients"]:
        if resources[ingredien] < receipt_to_make["ingredients"][ingredien]:
            return ingredien

def collect_coins(receipt):
    receipt_to_make = MENU[receipt]
    cost = receipt_to_make["cost"]

    print(f"Please insert coins for ${'{:.2f}'.format(cost)}. We accept quarters, dimes, nickles and pennies")
    quarters = int(input("How many quarters? ") or "0")
    dimes = int(input("How many dimes? ") or "0")
    nickles = int(input("How many nickles? ") or "0")
    pennies = int(input("How many pennies? ") or "0")

    inserted = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    print(f"you inserted ${'{:.2f}'.format(inserted)}")

    overpay = inserted - cost

    if overpay > 0:
         print(f"Here is ${'{:.2f}'.format(overpay)} in change")

    if overpay >= 0:
        global fond
        fond += cost
        return True
    else:
        print("​Sorry that's not enough money. Money refunded")
        return False



def make_receipt(receipt):
    receipt_to_make = MENU[receipt]

    open_ressource = check_receipt(receipt)
    if open_ressource:
        print(f"Sorry there is not enough {open_ressource.capitalize()}")
    
    elif collect_coins(receipt):
        for ingredien in receipt_to_make["ingredients"]:
            resources[ingredien] -= receipt_to_make["ingredients"][ingredien]
        
        print(f"Here is your {receipt.capitalize()}. Enjoy!")
    


machine_runs = True
fond = 0

while machine_runs:

    choice = input("What would you like? ((e)espresso/(l)atte/(c)appucino): ").lower()

    if choice == "report":
        print_report()
    elif choice == "e":
        make_receipt("espresso")
    elif choice == "l":
        make_receipt("latte")
    elif choice == "c":
        make_receipt("cappuccino")
    elif choice == "off":
        print("Shutingdown...")
        machine_runs = False