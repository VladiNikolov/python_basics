dancers = int(input())
points = float(input())
season = input()
place = input()

salary = 0
charity_percent = 0.75
charity = 0
if place == "Bulgaria":
    sum = dancers * points
    if season == "summer":
        sum = sum * 0.95
        charity = sum * charity_percent
        final_sum = sum - charity
        salary = final_sum / dancers
    elif season == "winter":
        sum = sum * 0.92
        charity = sum * charity_percent
        final_sum = sum - charity
        salary = final_sum / dancers
elif place == "Abroad":
    sum = (dancers * points) * 1.5
    if season == "summer":
        sum = sum * 0.90
        charity = sum * charity_percent
        final_sum = sum - charity
        salary = final_sum / dancers
    elif season == "winter":
        sum = sum * 0.85
        charity = sum * charity_percent
        final_sum = sum - charity
        salary = final_sum / dancers
print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {salary:.2f}")
