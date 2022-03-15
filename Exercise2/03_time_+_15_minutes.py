hours = int(input())
minutes = int(input())

all_time = (hours * 60) + minutes + 15
new_hours = all_time // 60
new_minutes = all_time % 60
if new_hours > 23:
    new_hours = 0
if new_minutes < 10:
    print(f"{new_hours}:0{new_minutes}")
else:
    print(f"{new_hours}:{new_minutes}")
