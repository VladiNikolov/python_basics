location = int(input())
sum_gold = 0
average = 0
total_average = 0

for i in range(location):
    average = float(input())
    number_of_days = int(input())
    total_average = 0
    sum_gold = 0
    for day in range(number_of_days):
        gold = float(input())
        sum_gold = sum_gold + gold
    total_average = (sum_gold / number_of_days)
    difference = abs(total_average - average)
    if average <= total_average:
        print(f"Good job! Average gold per day: {total_average:.2f}.")
    else:
        print(f"You need {difference:.2f} gold.")



