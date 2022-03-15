profit = float(input())
command = input()

total_price =  0
q
while command != "Party!" or total_price >= profit:
    price_coctails = len(command)
    number_coctails = int(input())
    total_price = price_coctails * number_coctails

    if total_price % 2 != 0:
        total_price += (total_price * 0.75)
    elif total_price % 2 != 1:
        total_price += total_price
    command = input()
difference = abs(profit - total_price)
print(f"We need {difference:.2f} leva more.")
print(f"Club income - {total_price:.2f} leva.")


#print(total_price)