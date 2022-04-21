first_match = input()
second_match = input()
third_match = input()

first_team_wins = 0
first_team_loses = 0
first_team_draws = 0
first_index_first_match = first_match[0]
second_index_first_match = first_match[2]
first_index_second_match = second_match[0]
second_index_second_match = second_match[2]
first_index_third_match = third_match[0]
second_index_third_match = third_match[2]

if int(first_index_first_match) > int(second_index_first_match):
    first_team_wins += 1
elif int(first_index_first_match) < int(second_index_first_match):
    first_team_loses += 1
elif int(first_index_first_match) == int(second_index_first_match):
    first_team_draws += 1
if int(first_index_second_match) > int(second_index_second_match):
    first_team_wins += 1
elif int(first_index_second_match) < int(second_index_second_match):
    first_team_loses += 1
elif int(first_index_second_match) == int(second_index_second_match):
    first_team_draws += 1
if int(first_index_third_match) > int(second_index_third_match):
    first_team_wins += 1
elif int(first_index_third_match) < int(second_index_third_match):
    first_team_loses += 1
elif int(first_index_third_match) == int(second_index_third_match):
    first_team_draws += 1
print(f"Team won {first_team_wins} games.")
print(f"Team lost {first_team_loses} games.")
print(f"Drawn games: {first_team_draws}")
