seasons = input()
type_of_group = input()
count_students = int(input())
count_nights = int(input())
sports = ""
price = 0

if seasons == "Winter" and type_of_group == "girls":
    sports = "Gymnastics"
    price = 9.60
elif seasons == "Winter" and type_of_group == "boys":
    sports = "Judo"
    price = 9.60
elif seasons == "Winter" and type_of_group == "mixed":
    sports = "Ski"
    price = 10
elif seasons == "Spring" and type_of_group == "girls":
    sports = "Athletics"
    price = 7.20
elif seasons == "Spring" and type_of_group == "boys":
    sports = "Tennis"
    price = 7.20
elif seasons == "Spring" and type_of_group == "mixed":
    sports = "Cycling"
    price = 9.50
elif seasons == "Summer" and type_of_group == "girls":
    sports = "Volleyball"
    price = 15
elif seasons == "Summer" and type_of_group == "boys":
    sports = "Football"
    price = 15
elif seasons == "Summer" and type_of_group == "mixed":
    sports = "Swimming"
    price = 20
all_price = price * count_nights * count_students

if 10 <= count_students < 20:
    all_price = all_price * 0.95
elif 20 <= count_students < 50:
    all_price = all_price * 0.85
elif count_students >= 50:
    all_price = all_price / 2
print(f"{sports} {all_price:.2f} lv.")


