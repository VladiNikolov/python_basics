rest_days = int(input())

work_days = 365 - rest_days
time_for_play = work_days * 63 + rest_days * 127
norm_to_play = 30000 - time_for_play
in_hours = abs(norm_to_play // 60)
in_minute = norm_to_play % 60

if norm_to_play >= 30000:
    print('Tom will run away')
    print(f'{in_hours} hours and {in_minute} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{in_hours} hours and {in_minute} minutes less for play')
