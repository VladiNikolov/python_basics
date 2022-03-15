#"The final price is: {крайна цена на услугата} lv."
#"The discount is: {отстъпка} lv."



square_meters = float(input())
all_price_work = square_meters * 7.61
discount = all_price_work * 0.18
final_price = all_price_work - discount


print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')
