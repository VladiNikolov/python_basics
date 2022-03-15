#zad 1. USD to BGN
usd = float(input())

bgn = usd * 1.79549
print(bgn)

#zad 2. Radians to Degrees
import math
radians = float(input())

degrees = (radians * 180) / math.pi
print(degrees)

#zad 3. Deposit Calculator
sum = float(input())
mounth = int(input())
percent = float(input())

percent_per_mount = ((sum * percent) / 12) /100
total_sum = sum + (percent_per_mount * mounth)
print(total_sum)

#zad 4. Vacation books list
all_pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_pages = all_pages / pages_per_hour
all_hours = total_pages / days
print(round(all_hours))

#zad 5. Supplies for School
pens = int(input())
markers = int(input())
detergent = int(input())
percents = int(input())

price_pens = 5.80
price_markers = 7.20
price_detergent = 1.20

all_price_pens = price_pens * pens
all_price_markers = price_markers * markers
all_price_detergent = price_detergent * detergent

total_price = all_price_pens + all_price_markers + all_price_detergent
total_price = total_price - (total_price * (percents / 100))
print(total_price)

#zad 6. Repainting
nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

all_nylon = (2 + nylon) * 1.50
all_paint = (paint * 14.50) * 1.1
all_thinner = thinner * 5
sum_total = all_nylon + all_paint + all_thinner + 0.40
all_sum = (sum_total * 0.30) * hours
total = all_sum + sum_total
print(f"{total}")

#zad 7. Food Delivery
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

#zad 8. Basketball Equipment
tax = int(input())

basketball_sneakers = tax * 0.60
basketball_team = basketball_sneakers * 0.80
basketball_ball = basketball_team * 0.25
basketball_accessories = basketball_ball  * 0.20
all_price = basketball_accessories + basketball_ball + basketball_sneakers + basketball_team + tax
print(all_price)

#zad 9. Fish Tank
length = int(input())
width = int(input())
hight = int(input())
percent = float(input())

volume_aquarium = length * width * hight
volume_liters = volume_aquarium * 0.001 # volume_liters = volume_aquarium / 1000
percent = percent / 100
needed_liters = volume_liters * (1 - percent)
print(needed_liters)









