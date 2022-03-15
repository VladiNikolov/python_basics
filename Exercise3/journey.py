budget = float(input())
seasons = input()

destination = ''
nastanqvane = ''
if budget <= 100:
    destination = 'Bulgaria'
    nastanqvane = 'Camp'
    if seasons == 'summer':
        budget = budget * 0.30
    elif seasons == 'winter':
        nastanqvane = 'Hotel'
        budget = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    nastanqvane = 'Camp'
    if seasons == 'summer':
        budget = budget * 0.40
    elif seasons == 'winter':
        nastanqvane = 'Hotel'
        budget = budget * 0.80
elif budget >= 1000:
   nastanqvane = 'Hotel'
   destination = 'Europe'
   budget = budget * 0.90
print(f"Somewhere in {destination}")
print(f"{nastanqvane} - {budget:.2f}")


