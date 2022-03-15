months = input()
br_sleeping = int(input())

price_studio = 0
price_apartments = 0

if months == 'May' or months == 'October':
    price_studio = 50
    price_apartments = 65
    if 7 < br_sleeping < 14:
        price_studio = price_studio * 0.95
    elif br_sleeping > 14:
        price_studio = price_studio * 0.70
        price_apartments = price_apartments * 0.90
elif months == 'June' or months == 'September':
    price_studio = 75.20
    price_apartments = 68.70
    if br_sleeping > 14:
        price_studio = price_studio * 0.80
        price_apartments = price_apartments * 0.90
elif months == 'July' or months == 'August':
    price_studio = 76
    price_apartments = 77
    if br_sleeping > 14:
        price_apartments = price_apartments * 0.90
night_in_apartment = br_sleeping * price_apartments
night_in_studio = br_sleeping * price_studio

print(f'Apartment: {night_in_apartment:.2f} lv.')
print(f'Studio: {night_in_studio:.2f} lv.')





