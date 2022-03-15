town = input()
package = input()
vip_discount = input()
stay_days = int(input())
price = 0

if town != "Bansko" and town != "Borovets" and town != "Varna" and town != "Burgas":
    print("Invalid input!")
    exit()
if package != "withEquipment" and package != "noEquipment" and package != "withBreakfast" and package != "noBreakfast":
    print("Invalid input!")
    exit()
if stay_days <= 0:
    print("Days must be positive number!")
    exit()
if stay_days > 7:
    stay_days = stay_days - 1
    exit()
if town == "Bansko" or town == "Borovets":
    if package == "withEquipment":
        price = 100
        if vip_discount == "yes":
            price = price * 0.90
    elif package == "noEquipment":
        price = 80
        if vip_discount == "yes":
            price = price * 0.95
elif town == "Varna" or town == "Burgas":
    if package == "withBreakfast":
        price = 130
        if vip_discount == "yes":
            price = price * 0.88
    elif package == "noBreakfast":
        price = 100
        if vip_discount == "yes":
            price = price * 0.93

total_price = price * stay_days
print(f"The price is {total_price:.2f}lv! Have a nice time!")

