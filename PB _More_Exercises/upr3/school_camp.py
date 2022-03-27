seasons = input()
type_of_group = input()
count_students = int(input())
count_nights = int(input())
sports = ""
price = 0
all_price = 0

if type_of_group == "girls":
    if seasons == "Winter":
        sports = "Gymnastics"
        price = 9.60
        all_price = price * count_students * count_nights
    elif seasons == "Spring":
        sports = "Athletics"
        price = 7.20
        all_price = price * count_students * count_nights
    elif seasons == "Summer":
        sports = "Volleyball"
        price = 15
        all_price = price * count_students * count_nights
elif type_of_group == "boys":
    if seasons == "Winter":
        sports = "Judo"
        price = 9.60
        all_price = price * count_students * count_nights
    elif seasons == "Spring":
        sports = "Tennis"
        price = 7.20
        all_price = price * count_students * count_nights
    elif seasons == "Summer":
        sports = "Football"
        price = 15
        all_price = price * count_students * count_nights
elif type_of_group == "mixed":
    if seasons == "Winter":
        sports = "Ski"
        price = 10
        all_price = price * count_students * count_nights
    elif seasons == "Spring":
        sports = "Cycling"
        price = 9.50
        all_price = price * count_students * count_nights
    elif seasons == "Summer":
        sports = "Swimming"
        price = 20
        all_price = price * count_students * count_nights
if 10 <= count_students < 20:
    all_price = all_price * 0.95
elif 20 <= count_students < 50:
    all_price = all_price * 0.85
elif count_students >= 50:
    all_price = all_price / 2
print(f"{sports} {all_price:.2f} lv.")
