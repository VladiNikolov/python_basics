number_of_groups = int(input())

musala = 0
monblan= 0
kilimandjaro = 0
k2 = 0
everest = 0
people_in_group = 0
for number in range(number_of_groups):
    people_in_group = int(input())
    if people_in_group <= 5:
        musala += people_in_group
    elif people_in_group <= 12:
        monblan += people_in_group
    elif people_in_group <= 25:
        kilimandjaro += people_in_group
    elif people_in_group <= 40:
        k2 += people_in_group
    elif people_in_group > 40:
        everest += people_in_group
all_people = musala + monblan + kilimandjaro + k2 + everest
print(f'{musala / all_people * 100:.2f}%')
print(f'{monblan / all_people * 100:.2f}%')
print(f'{kilimandjaro / all_people * 100:.2f}%')
print(f'{k2 / all_people * 100:.2f}%')
print(f'{everest / all_people * 100:.2f}%')

