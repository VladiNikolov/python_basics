money = float(input())
year_to_live = int(input())

for year in range(1800, year_to_live + 1):

    if year % 2 == 0:
        money -= 12000
    else:
        year = year + 18 - 1800
        money -= 12000 + (50 * year)
    year += 1
if money >= 0:
    print(f'Yes! He will live a carefree life and will have {money:.2f} dollars left.' )
else:
    print(f'He will need {abs(money):.2f} dollars to survive.')