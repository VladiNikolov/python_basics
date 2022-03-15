chicken_menus = int(input())
fish_menus = int(input())
vegan_menus = int(input())

all_price_chicken_menus = chicken_menus * 10.35
all_price_fish_menus = fish_menus * 12.40
all_price_vegan_menus = vegan_menus * 8.15
all_price =  all_price_vegan_menus + all_price_fish_menus + all_price_chicken_menus
decerts = all_price * 0.20
total_price = all_price + decerts + 2.5
print(total_price)