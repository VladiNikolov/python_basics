first_team_wins = 0
first_team_loses = 0
first_team_draws = 0
for result in range(3):
    current_input = input()
    first_team_result = current_input[0]
    second_team_result = current_input[2]

    if int(first_team_result) > int(second_team_result):
        first_team_wins += 1
    elif int(first_team_result) < int(second_team_result):
        first_team_loses += 1
    else:
        first_team_draws += 1
print(f"Team won {first_team_wins} games.")
print(f"Team lost {first_team_loses} games.")
print(f"Drawn games: {first_team_draws}")
