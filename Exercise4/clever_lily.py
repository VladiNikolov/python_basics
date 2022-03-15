age_lili = int(input())
price_laundry = float(input())
price_toy = int(input())

count_toy = 0
total_money = 0
birthday_money = 0
for current_age in range(1, age_lili+1):  #range(ages)
    if current_age % 2 != 0: #if current_age % 2 == 1 нечетно число, нечетна година
        count_toy += 1
    else:
        birthday_money += 10  #birthday_money = birthday_money + 10
        total_money += birthday_money - 1  #total_money = total_money + birthday_money -1
total_money += count_toy * price_toy
difference = abs(total_money - price_laundry)
if total_money >= price_laundry:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')