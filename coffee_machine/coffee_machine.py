#TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):”


#TODO Turn off the Coffee Machine by entering “off” to the prompt

#TODO Print report

#TODO Check resources sufficient?

#TODO Process coins

#TODO Check transaction successful?

#TODO Make Coffee

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




def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = profit
    return (f'Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}')

def check(order_ingredients):
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print('Not enough {item}')
            return False
    return True

def processcoins():
    q = int(input('Please submit quarters\n')) * 0.25
    d = int(input('Please submit dimes\n')) * 0.10
    n = int(input('Please submit nickels\n')) * 0.05
    p = int(input('Please submit pennies\n')) * 0.01
    return (q+d+n+p)

def transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f'Here is {change} in change')
        global profit
        profit += drink_cost
        return True
    else:
        print('sorry you do not have enough money')
        return False

def make_coffee(drink_name, order_ingredients):
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f'Here is your {drink_name}')




ON = True
while ON:
    choice = input("What would you like? (espresso/latte/cappuccino)\n").lower()
    if choice == 'report':
        print(report())
    
    elif choice == 'off':
        print('shutting down')
        ON = False

    else:
        drink = MENU[choice]
        if check(drink['ingredients']):
            payment = processcoins()
            if transaction(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])

