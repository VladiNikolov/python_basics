needed_money = int(input())
sum_money = 0
money_cash = 0
money_card = 0
count_times_cash = 0
count_times_card = 0
count = -1
is_money_colection = False
command = input()
while command != "End":
    current_input = int(command)
    count += 1
    if count % 2 == 0:
        if 0 <= current_input <= 100:
            money_cash += current_input
            count_times_cash += 1
            sum_money += current_input
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:
        if current_input >= 10:
            money_card += current_input
            count_times_card += 1
            sum_money += current_input
            print("Product sold!")
        else:
            print("Error in transaction!")
    if sum_money >= needed_money:
        is_money_colection = True
        break
    command = input()
if is_money_colection:
    print(f"Average CS: {money_cash / count_times_cash:.2f}")
    print(f"Average CC: {money_card / count_times_card:.2f}")
else:
    print("Failed to collect required money for charity.")
