destination = input()
date = input()
number_of_sleeps = int(input())
price = 0

if destination == 'France' and date == '21-23':
    price = number_of_sleeps * 30
elif destination == 'France' and date == '24-27':
    price = number_of_sleeps * 35
elif destination == 'France' and date == '28-31':
    price = number_of_sleeps * 40
if destination == 'Italy' and date == '21-23':
    price = number_of_sleeps * 28
elif destination == 'Italy' and date == '24-27':
    price = number_of_sleeps * 32
elif destination == 'Italy' and date == '28-31':
    price = number_of_sleeps * 39
if destination == 'Germany' and date == '21-23':
    price = number_of_sleeps * 32
elif destination == 'Germany' and date == '24-27':
    price = number_of_sleeps * 37
elif destination == 'Germany' and date == '28-31':
    price = number_of_sleeps * 43
print(f"Easter trip to {destination} : {price:.2f} leva.")
