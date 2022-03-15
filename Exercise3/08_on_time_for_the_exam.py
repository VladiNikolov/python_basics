hours_exam = int(input())
minutes_exam = int(input())
hours_arrival = int(input())
minutes_arrival = int(input())

all_minutes_exam = (hours_exam * 60) + minutes_exam
all_minutes_arrival = (hours_arrival * 60) + minutes_arrival

if all_minutes_arrival > all_minutes_exam:
    print("Late")
elif all_minutes_exam - 30 <= all_minutes_arrival <= all_minutes_exam:
    print("On time")
else:
    print("Early")

difference = abs(all_minutes_arrival- all_minutes_exam)
hours = difference // 60
minutes = difference % 60
if all_minutes_exam - 60 <= all_minutes_arrival <= all_minutes_exam:
    print(f"{minutes} minutes before the start")
elif all_minutes_arrival <= all_minutes_exam - 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif all_minutes_exam < all_minutes_arrival < all_minutes_exam + 60:
    print(f"{minutes} minutes after the start")
elif all_minutes_arrival >= all_minutes_exam + 60:
    print(f"{hours}:{minutes:02d} hours after the start")