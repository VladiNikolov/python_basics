groups_of_climbers = int(input())

count_musala = 0
count_monblan = 0
count_kilimandjaro = 0
count_k2 = 0
count_everest = 0

for number in range(groups_of_climbers):
    number_of_climbers = int(input())
    if number_of_climbers <= 5:
        count_musala += number_of_climbers
    elif number_of_climbers <= 12:
        count_monblan += number_of_climbers
    elif number_of_climbers <= 25:
        count_kilimandjaro += number_of_climbers
    elif number_of_climbers <= 40:
        count_k2 += number_of_climbers
    elif number_of_climbers >= 41:
        count_everest += number_of_climbers
all_climbers = count_everest + count_k2 + count_monblan + count_musala + count_kilimandjaro
percents_musala = (count_musala / all_climbers) * 100
percents_monblan = (count_monblan / all_climbers) * 100
percents_kilimanjaro = (count_kilimandjaro / all_climbers) * 100
percents_k2 = (count_k2 / all_climbers) * 100
percents_everest = (count_everest / all_climbers) * 100
print(f"{percents_musala:.2f}%")
print(f"{percents_monblan:.2f}%")
print(f"{percents_kilimanjaro:.2f}%")
print(f"{percents_k2:.2f}%")
print(f"{percents_everest:.2f}%")


