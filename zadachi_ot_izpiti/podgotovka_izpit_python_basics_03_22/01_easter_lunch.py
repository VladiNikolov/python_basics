number_easter_bread = int(input())
number_box_with_eggs = int(input())
kilo_of_cookies = int(input())

price_easter_bread = 3.20
price_number_box_whit_eggs = 4.35
price_per_kilo_cookies = 5.40
price_per_one_egg_paint = 0.15

all_price_easter_bread = number_easter_bread * price_easter_bread
all_price_eggs = (number_box_with_eggs * price_number_box_whit_eggs) + (number_box_with_eggs * 12) * 0.15
all_price_cookies = kilo_of_cookies * price_per_kilo_cookies

total_price = all_price_eggs + all_price_easter_bread + all_price_cookies
print(f"{total_price:.2f}")