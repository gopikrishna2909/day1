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


quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
money = 0



def report():
    print(f'water: {resources["water"]}ml\n'
          f'milk: {resources['milk']}ml\n'
          f'Coffee: {resources['coffee']}g\n'
          f'Money:{money}')

def coins():
    print('Please insert coins')
    quarter = int(input('How many quarters?: '))
    dime = int(input('How many dimes?: '))
    nickle = int(input('How many nickles?: '))
    penny = int(input('How many pennies?: '))
    total = (quarters*quarter) + (dimes*dime) + (nickles*nickle) + (pennies*penny)
    return total





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
        elif user_choice == "espresso" or "latte" or 'cappuccino':

            for key in MENU[user_choice]['ingredients']:
                if key in resources:
                    if resources[key] >= MENU[user_choice]['ingredients'][key]:
                        resources[key] -= MENU[user_choice]['ingredients'][key]
                    else:
                        print(f'Sorry there is no enough {key}')
                        return
            change = coins()
            if change == MENU[user_choice]['cost']:
                print(f"Here is your {user_choice} enjoy!")
                money += change
            elif change > MENU[user_choice]['cost']:
                change -= MENU[user_choice]['cost']
                money += MENU[user_choice]['cost']
                print(f"Here is ${change:.2f} change.")
                print(f"Here is your {user_choice} enjoy!")
            else:
                print('Sorry that is no enough money')
                return
coffee_machine()