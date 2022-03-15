number_tournaments = int(input())
number_of_points  = int(input())

wins = 0
points_for_w = 0
points_for_f = 0
points_for_sf = 0
for number in range(number_tournaments):
    etap_in_tournaments = input()
    if etap_in_tournaments == 'W':
        points_for_w += 2000
        wins += 1
    elif etap_in_tournaments == 'F':
        points_for_f += 1200
    elif etap_in_tournaments == 'SF':
        points_for_sf += 720
all_points = points_for_w + points_for_f + points_for_sf + number_of_points
average_points = (points_for_w + points_for_f + points_for_sf) // number_tournaments
procent_win_tournaments = (wins / number_tournaments) * 100
print(f"Final points: {all_points:.0f}")
print(f"Average points: {average_points:.0f}")
print(f"{procent_win_tournaments:.2f}%")
