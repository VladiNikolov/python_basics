number_bread = int(input())
number_eggshells = int(input())
kilogram_cookies = int(input())

all_price_bread = number_bread * 3.2
all_price_egg = number_eggshells * 4.35
all_price_cookies = kilogram_cookies * 5.40
paint_for_egg = (number_eggshells * 12) * 0.15
total = all_price_bread + all_price_egg + all_price_cookies + paint_for_egg
print(f'{total:.2f}')
