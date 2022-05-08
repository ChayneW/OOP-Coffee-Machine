from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects:
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_access = Menu()
# menu_description = MenuItem()


# MAIN PROGRAM STARTS HERE:
is_on = True

while is_on:
    choice = input(f"What would you like?: {menu_access.get_items()}\n>").lower()
    
    if choice == 'off':
        is_on = False  
    
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        drink_name = menu_access.find_drink(choice)
        if drink_name == None:
            print("Please choose from drinks provided\n")
            pass
        
        else:
                # Data check:
            # print(drink_name.name, drink_name, type)
            # print(drink_name.cost)

            cost = drink_name.cost

                # Data check:
            # print(drink_name.ingredients)
            # print(f" coffee ingred. bank = {coffee_maker.resources}")

            is_enough = coffee_maker.is_resource_sufficient(drink_name)
            # print(is_enough)
            
            if is_enough:

                #Money logic:
                money_machine.make_payment(cost)

                # Make drink:
                make_drink = coffee_maker.make_coffee(drink_name)
                
                    # Data check:
                # print(coffee_maker.resources)
    
            else:
                pass








         
