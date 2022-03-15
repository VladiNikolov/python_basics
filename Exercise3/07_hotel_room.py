month = input()
count_nights = int(input())
all_price_studio = 0
all_price_apartment = 0
studio = 0
apartment = 0
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    all_price_studio = studio * count_nights
    all_price_apartment = apartment * count_nights
    if 7 < count_nights <= 14:
        all_price_studio = all_price_studio * 0.95
    elif count_nights > 14:
        all_price_studio = all_price_studio * 0.70
        all_price_apartment = all_price_apartment * 0.90
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    all_price_studio = studio * count_nights
    all_price_apartment = apartment * count_nights
    if count_nights > 14:
        all_price_studio = all_price_studio * 0.80
        all_price_apartment = all_price_apartment * 0.90
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    all_price_studio = studio * count_nights
    all_price_apartment = apartment * count_nights
    if count_nights > 14:
        all_price_apartment = all_price_apartment * 0.90
print(f"Apartment: {all_price_apartment:.2f} lv.")
print(f"Studio: {all_price_studio:.2f} lv.")