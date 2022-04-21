capacity_of_stadium = int(input())
number_fans = int(input())
count_sector_A = 0
count_sector_B = 0
count_sector_V = 0
count_sector_G = 0
for number in range(number_fans):
    current_sector = input()
    if current_sector == "A":
        count_sector_A += 1
    elif current_sector == "B":
        count_sector_B += 1
    elif current_sector == "V":
        count_sector_V += 1
    elif current_sector == "G":
        count_sector_G += 1
print(f"{count_sector_A / number_fans * 100:.2f}%")
print(f"{count_sector_B / number_fans * 100:.2f}%")
print(f"{count_sector_V / number_fans * 100:.2f}%")
print(f"{count_sector_G / number_fans * 100:.2f}%")
print(f"{number_fans / capacity_of_stadium * 100:.2f}%")
