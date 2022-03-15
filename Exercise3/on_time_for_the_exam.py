hour_of_examine = int(input())
minutes_of_exsamine = int(input())
hour_of_arriving = int(input())
minutes_of_arriving = int(input())

time_of_exsamine = hour_of_examine * 60 + minutes_of_exsamine
time_of_arriving  = hour_of_arriving * 60 + minutes_of_arriving

if time_of_arriving > time_of_exsamine:
    print('Late')
elif time_of_exsamine - 30 <= time_of_arriving <= time_of_exsamine:
    print('On time')
else:
    print('Early')
difference = abs (time_of_arriving - time_of_exsamine)
hours = difference // 60
minutes = difference % 60
if time_of_exsamine -60 < time_of_arriving < time_of_exsamine:
    print(f"{minutes} minutes before the start")
elif time_of_arriving <= time_of_exsamine - 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif time_of_exsamine < time_of_arriving < time_of_exsamine + 60:
    print(f"{minutes} minutes after the start")
elif time_of_arriving >= time_of_exsamine + 60:
    print(f"{hours}:{minutes:02d} hours after the start")