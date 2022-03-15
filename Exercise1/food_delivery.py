count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegan_menu = int(input())

price_chicken_menu = count_chicken_menu * 10.35
price_fish_menu = count_fish_menu * 12.40
price_vegan_menu = count_vegan_menu * 8.15

order = price_chicken_menu + price_fish_menu + price_vegan_menu
desert = order * 0.20
all_order = price_chicken_menu + price_fish_menu + price_vegan_menu + desert + 2.5
print(all_order)
