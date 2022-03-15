stay_days = int(input())
room = input()
rating = input()

sleeping_days = stay_days - 1
all_price = 0
price = 0
if room == 'room for one person':
    price = 18 * sleeping_days
elif room == 'apartment':
    price = 25
    if sleeping_days < 10:
        price = price * sleeping_days * 0.70
    elif 10 < sleeping_days <= 15:
        price = price * sleeping_days * 0.65
    elif sleeping_days > 15:
        price = price * sleeping_days * 0.50
elif room == 'president apartment':
    price = 35
    if sleeping_days < 10:
        price = price * sleeping_days * 0.90
    elif 10 < sleeping_days <= 15:
        price = price * sleeping_days * 0.85
    elif sleeping_days > 15:
        price = price * sleeping_days * 0.80
if rating == 'positive':
    all_price = price * 1.25
elif rating == 'negative':
    all_price = price * 0.90
print(f'{all_price:.2f}')