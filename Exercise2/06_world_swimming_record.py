from math import floor
records_in_sec = float(input())
distance = float(input())
time_in_sec_per_1m = float(input())

all_time = distance * time_in_sec_per_1m
delay = floor(distance / 15)
delay = (delay * 12.5)
total_time = all_time + delay
difference = abs(records_in_sec - total_time)
if total_time < records_in_sec:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")