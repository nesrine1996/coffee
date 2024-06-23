from menu import MENU
from menu import resources


# TODO: 1. Print report of all coffee machine resources
resources["profit"] = 0


def ask_user():
    drink_dispensed = True
    machine_on = True
    while drink_dispensed and machine_on:
        prompt = input("What would you like? (espresso/latte/cappuccino):")
        if prompt == "off":
            machine_on = False
            quit()
        elif prompt == "report":
            print(f"Water: {resources['water']}ml")
            if prompt != "espresso":
                print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: $ {resources['profit']}")
        else:
            if not check_resources(prompt):
                sum_coins = process_coins()
                check_transaction(prompt, sum_coins)
                update_resources(prompt)


def check_resources(prompt):
    ingredients_list = ['water', 'milk', 'coffee']
    resources_insufficient = False
    for ingredient in ingredients_list:
        if MENU[prompt]["ingredients"][ingredient] > resources[ingredient]:
            resources_insufficient = True
            if resources_insufficient:
                print(f"Sorry there is not enough {ingredient}.")
        else:
            return resources_insufficient


def process_coins():
    quarters = int(input("Insert quarters: "))
    dimes = int(input("Insert dimes: "))
    nickels = int(input("Insert nickels: "))
    pennies = int(input("Insert pennies: "))
    # Ensure the values are not None and are numbers
    if quarters is None or dimes is None or nickels is None or pennies is None:
        raise ValueError("All coin counts must be initialized with numeric values.")

    if not all(isinstance(coin, (int, float)) for coin in [quarters, dimes, nickels, pennies]):
        raise TypeError("All coin counts must be numeric values (int or float).")

    sum_coins = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    print(sum_coins)
    return sum_coins


resources["profit"] = 0


def check_transaction(prompt, sum_coins):
    if MENU[prompt]["cost"] > sum_coins:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if sum_coins == MENU[prompt]["cost"]:
            resources["profit"] += sum_coins
            print(resources["profit"])
        else:
            change = sum_coins - MENU[prompt]["cost"]
            resources["profit"] += MENU[prompt]["cost"]
            print(resources["profit"])
    return


def update_resources(prompt):
    ingredients_list = ['water', 'milk', 'coffee']
    if prompt == "espresso":
        ingredients_list = ['water', 'coffee']
    for ingredient in ingredients_list:
        resources[ingredient] -= MENU[prompt]["ingredients"][ingredient]
    resources["profit"] += MENU[prompt]["cost"]
    return


ask_user()
