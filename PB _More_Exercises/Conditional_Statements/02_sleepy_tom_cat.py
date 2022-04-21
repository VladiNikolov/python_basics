days_off = int(input())

norm = 30000
worked_days = 365 - days_off
all_played_minutes = (worked_days * 63) + (days_off * 127)
total_played = abs(30000 - all_played_minutes)
hours = total_played // 60
minutes = total_played % 60
if all_played_minutes > norm:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")