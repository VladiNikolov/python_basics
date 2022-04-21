number_kilometers = int(input())
day_or_night = input()

if number_kilometers < 20 and day_or_night == "day":
    number_kilometers = (number_kilometers * 0.79) + 0.70
elif number_kilometers < 20 and day_or_night == "night":
    number_kilometers = (number_kilometers * 0.90) + 0.70
elif number_kilometers < 100:
    number_kilometers = (number_kilometers * 0.09)
else:
    number_kilometers = (number_kilometers * 0.06)
print(f"{number_kilometers:.2f}")