
import os
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def change(beverage_chosen, choice):
    """calculates how much change the user puts in the machine"""
    print("Please insert coins.")
    quarters_input = int(input("How many quarters?: "))
    total_quarters = quarters_input * 0.25
    dimes_input = int(input("How many dimes?: "))
    total_dimes = dimes_input * 0.1
    nickles_input = int(input("How many nickles?: "))
    total_nickels = nickles_input * 0.05
    pennies_input = int(input("How many pennies?: "))
    total_pennies = pennies_input * 0.01
    total_change = total_quarters + total_dimes + total_nickels + total_pennies
    resources["money"] += beverage_chosen["cost"]
    if beverage_chosen["cost"] < total_change:
        change = total_change - beverage_chosen["cost"]
        print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {choice} ☕. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
        start()


def ingredients(beverage_chosen, choice):
    """checks if there's enough ingredients"""
    if resources["water"] >= beverage_chosen["ingredients"]["water"]:
        resources["water"] -= beverage_chosen["ingredients"]["water"]
    else:
        print("Sorry there is no enough water.")
        start()

    if resources["coffee"] >= beverage_chosen["ingredients"]["coffee"]:
        resources["coffee"] -= beverage_chosen["ingredients"]["coffee"]
    else:
        print("Sorry there is no enough coffee.")
        start()

    if choice == "latte" or choice == "cappuccino":
        if resources["milk"] >= beverage_chosen["ingredients"]["milk"]:
            resources["milk"] -= beverage_chosen["ingredients"]["milk"]
        else:
            print("Sorry there is no enough milk.")
            start()


def start():
    on = True
    while on:
        choice = input(
            "Espresso: $1.5 \nLatte: $2.5 \nCappuccino: $3\nPick your drink:  ")
        if choice in MENU:
            beverage_chosen = (MENU[choice])
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
            start()
        elif choice == "off":
            on = False
            quit()

        ingredients(beverage_chosen, choice)
        change(beverage_chosen, choice)


start()
