time_first_player = int(input())
time_second_player = int(input())
time_third_player = int(input())


all_time_players = time_first_player + time_second_player + time_third_player
minutes = all_time_players // 60
seconds = all_time_players % 60
if seconds < 10:
    print(f"{minutes}:0{seconds:}")
else:
    print(f"{minutes}:{seconds:}")

