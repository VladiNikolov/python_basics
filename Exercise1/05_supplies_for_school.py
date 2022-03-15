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