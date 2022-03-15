# budget = float(input())
# destination = input()
# season = input()
# days = int(input())
#
# if destination == "Dubai":
#     if season == "Winter":
#         price_per_day = 45000
#         all_price = (days * price_per_day) * 0.70
#     elif season == "Summer":
#         price_per_day = 40000
#         all_price = (days * price_per_day) * 0.70
# elif destination == "Sofia":
#     if season == "Winter":
#         price_per_day = 17000
#         all_price = (days * price_per_day) * 1.25
#     elif season == "Summer":
#         price_per_day = 12500
#         all_price = (days * price_per_day) * 1.25
# elif destination == "London":
#     if season == "Winter":
#         price_per_day = 24000
#         all_price = (days * price_per_day)
#     elif season == "Summer":
#         price_per_day = 20250
#         all_price = (days * price_per_day)
# difference = abs(budget - all_price)
# if budget >= all_price:
#     print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
# else:
#     print(f"The director needs {difference:.2f} leva more!")

budget = float(input())
destination = input()
season = input()
days = int(input())

if destination == "Dubai" and season == "Winter":
    all_price = days * 45000
    all_price = all_price * 0.70
elif destination == "Dubai" and season == "Summer":
    all_price = days * 40000
    all_price = all_price * 0.70
elif destination == "Sofia" and season == "Winter":
    all_price = days * 17000
    all_price = all_price * 1.25
elif destination == "Sofia" and season == "Summer":
    all_price = days * 12500
    all_price = all_price * 1.25
elif destination == "London" and season == "Winter":
    all_price = days * 24000
elif destination == "London" and season == "Summer":
     all_price = days * 20250

difference = abs(budget - all_price)
if budget >= all_price:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")