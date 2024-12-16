def inserted_coins():
    print("please insert coins.")
    quarters=float(input("how many quarters?: "))*0.25
    dimes=float(input("how many dimes?: "))*0.1
    pennies=float(input("how many pennies?: "))*0.01
    nickels=float(input("how many nickels?: "))*0.05
    global total
    total=quarters+dimes+pennies+nickels
    return total
resources={
"milk":500,
"water":500,
"coffee":500}
menu={"espresso":{"ingredients":{"water":50,"coffee":18,},"price":1.5},
      "latte":{"ingredients":{"water":200,"coffee":24,"milk":150},"price":2.5},
      "cappuccino":{"ingredients":{"water":250,"coffee":24,"milk":100},"price":3.0}}
def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
             print(f"sorry, there is not enough {item}")
             return False
    return True
def transcation(money_recieved, drink_cost):
    if money_recieved<drink_cost:
        print("sorry, money not sufficient, Money refunded.")
        return False
    else:
        change=money_recieved-drink_cost
        global profit
        profit=money_recieved-change
        print(f"here is your {change} in change.")
        return True
    return profit
earnings=0
flag=True
while flag:
    choice=input("what would you like to have?(espresso/latte/cappuccino): ")
    if choice=='report':
        print(resources)
        print(f"earnings: {earnings}")
    elif choice=='off':
        flag=False
    else:
        print(menu[choice])
        if is_resources_sufficient(menu[choice]["ingredients"]):
            inserted_coins()
            if transcation(money_recieved=total, drink_cost=menu[choice]["price"]):
                earnings+=profit
                for item in menu[choice]["ingredients"]:
                    resources[item]-=menu[choice]["ingredients"][item]
                print(f"here is your {choice}. Enjoy")
            
        
