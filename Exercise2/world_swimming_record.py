record = float(input())
distance = float(input())
time_in_sec = float(input())

ivan_distance = distance * time_in_sec
nakazatelno_vreme = distance // 15 * 12.5

all_distance = ivan_distance + nakazatelno_vreme
difference = abs(record - all_distance)

if all_distance < record:
    print(f'Yes, he succeeded! The new world record is {all_distance:.2f} seconds.')
else:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')