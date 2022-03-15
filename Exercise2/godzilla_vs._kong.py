budget = float(input())
number_of_statist = int(input())
one_dress_price = float(input())

decor = budget * 0.1  # decor = budget * 10/100
one_dress_price = number_of_statist * one_dress_price

if number_of_statist >150:
    one_dress_price *= 0.9   #one_dress_price = one_dress_price * 90 /100
all_needed_money = decor + one_dress_price
differens = abs(all_needed_money - budget)  #допълнителна променлива с функцията abs - която дава ->
                                                # разликата между две числа с положителен знак винаги
if all_needed_money > budget:
    print('Not enough money!')
    print(f'Wingard needs {differens:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {differens:.2f} leva left.')

