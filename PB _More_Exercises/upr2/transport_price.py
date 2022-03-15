number_of_kilometers = int(input())
day_or_night = input()
price = 0
if number_of_kilometers < 20 and day_or_night == "day":
    price = (number_of_kilometers * 0.79) + 0.70
elif number_of_kilometers < 20 and day_or_night == "night":
    price = (number_of_kilometers * 0.90) + 0.70
elif number_of_kilometers < 100 and (day_or_night == "day" or day_or_night == "night"):
    price = number_of_kilometers * 0.09
elif number_of_kilometers >= 100 and (day_or_night == "day" or day_or_night == "night"):
    price = number_of_kilometers * 0.06
print(f"{price:.2f}")