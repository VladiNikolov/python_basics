amount_paper = int(input())
amount_fabric = int(input())
amount_glue = float(input())
discount = int(input())

price_paper = amount_paper * 5.80
price_fabric = amount_fabric * 7.20
price_glue = amount_glue * 1.20

total_price = price_paper + price_fabric + price_glue
final_price = total_price - (total_price * discount / 100)
print(f"{final_price:.3f}")

