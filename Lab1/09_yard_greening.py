square_meters = float(input())

all_price_square_meters = (square_meters * 7.61)
total_price = all_price_square_meters * 0.82
discount = all_price_square_meters - total_price

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")