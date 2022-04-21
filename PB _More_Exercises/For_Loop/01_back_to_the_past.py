saved_money = float(input())

year_to_leave = int(input())

money = 0
for current_year in range(1800, year_to_leave + 1):
    if current_year % 2 == 0:
        money = saved_money - 12000
    else:
        current_year = current_year + 18 - 1800
        money = saved_money - 12000 + (50 * current_year)
difference = abs(saved_money - money)
if saved_money >= money:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {difference:.2f} dollars to survive." )