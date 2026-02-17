from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = 'on'

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on == 'on':
    order = input(f'What would you like to drink?\n{menu.get_items()}\n')

    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        is_on = 'off'
    else:
        ordered_item = menu.find_drink(order)

        coffee_valid = isinstance(ordered_item, MenuItem) and coffee_maker.is_resource_sufficient(ordered_item)

        if coffee_valid:
            payment_valid = money_machine.make_payment(ordered_item.cost)

            if payment_valid:
                coffee_maker.make_coffee(ordered_item)

print(f'Coffee Machine is {is_on}. Total day:')
coffee_maker.report()
money_machine.report()