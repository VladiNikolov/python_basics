import math

number_of_tournaments = int(input())
initial_points = int(input())

sum_points = 0
count_wins = 0
for number in range(1, number_of_tournaments + 1):
    stage = input()
    if stage == "W":
        points = 2000
        sum_points += points
        count_wins += 1
    elif stage == "F":
        points = 1200
        sum_points += points
    elif stage == "SF":
        points = 720
        sum_points += points
average_points = sum_points / number_of_tournaments
all_points = initial_points + sum_points
percents_wins = count_wins / number_of_tournaments * 100

print(f"Final points: {all_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percents_wins:.2f}%")