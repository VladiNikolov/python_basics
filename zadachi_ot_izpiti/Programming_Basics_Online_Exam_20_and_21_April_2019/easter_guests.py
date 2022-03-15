import math

guests = int(input())
budget = int(input())

kozunak = math.ceil(guests / 3)
eggs = guests * 2
price_kozunak = kozunak * 4
price_eggs = eggs * 0.45
total_price = price_eggs + price_kozunak
difference = abs(budget - total_price)
if budget >= total_price:
    print(f"Lyubo bought {kozunak} Easter bread and {eggs} eggs.")
    print(f'He has {difference:.2f} lv. left.')
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")