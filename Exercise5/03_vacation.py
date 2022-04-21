needed_money = float(input())
available_money = float(input())

days = 0
count_spend = 0
count_save = 0
while available_money < needed_money:
    action = input()
    current_sum = float(input())
    days += 1
    if action == "spend":
        available_money -= current_sum
        count_spend += 1
        if count_spend == 5:
            count_spend = count_spend
            break
    elif action == "save":
        available_money += current_sum
        count_save += 1
        count_spend = 0
    if available_money < 0:
        available_money = 0

if available_money < needed_money:
    print("You can't save the money.")
    print(f"{days}")
else:
    print(f"You saved the money for {days} days.")