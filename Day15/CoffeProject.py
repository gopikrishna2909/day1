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
}

money = 0



def report():
    print(f"water: {resources['water']}ml\n"
          f"milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money:{money}")

def coins():
    print('Please insert coins')
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.10
    total += int(input('How many nickles?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total



def is_resource_sufficient(order_ingredient):
    for key in MENU[order_ingredient]['ingredients']:
            if resources[key] < MENU[order_ingredient]['ingredients'][key]:
                print(f"Sorry there is no enough {key}")
                return False
    return True

def is_transaction_successful(money_received,drink_cost):
    global money
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}.")
        money += drink_cost
        return True
    else:
        print("Sorry that is not enough money, money refunded")
        return False


def make_coffee(drink_name,ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"Here is your {drink_name} enjoy!")




def coffee_machine():

    global money

    machine = True
    while machine:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == 'off':
            print('Switching off')
            machine = False
        elif user_choice == 'report':
            report()
        else:
            drink = MENU[user_choice]
            if is_resource_sufficient(user_choice):
                payment = coins()
                if is_transaction_successful(payment,drink['cost']):
                    make_coffee(user_choice,drink['ingredients'])





coffee_machine()


# change = coins()
#             if change < MENU[user_choice]['cost']:
#                 print("Sorry that is not enough money. money refunded.")
#                 continue
#             for key in MENU[user_choice]['ingredients']:
#                 resources[key] -= MENU[user_choice]['ingredients'][key]
#
#             if change == MENU[user_choice]['cost']:
#                 print(f"Here is your {user_choice} enjoy!")
#                 money += change
#             elif change > MENU[user_choice]['cost']:
#                 change -= MENU[user_choice]['cost']
#                 money += MENU[user_choice]['cost']
#                 print(f"Here is ${change:.2f} change.")
#                 print(f"Here is your {user_choice} enjoy!")
