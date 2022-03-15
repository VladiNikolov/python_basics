shirt = float(input())
target = float(input())
discount = 0.15
price_shorts = shirt * 0.75
price_socks = price_shorts * 0.20
price_kalevri = 2 * (price_shorts + shirt)

total_price = shirt + price_shorts + price_socks + price_kalevri
final_price = total_price * 0.85
difference = abs(target - final_price)
if final_price >= target:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {final_price:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference:.2f} lv. more.")
