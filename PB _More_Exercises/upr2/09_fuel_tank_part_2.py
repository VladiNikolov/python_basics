# fuel_name = input()
# quantity_fuel = float(input())
# club_card = input()
#
# price_gas = 0.93
# price_gasoline = 2.22
# price_diesel = 2.33
# all_price = 0
# if fuel_name == "Gas":
#     if club_card == "Yes":
#         price_gas = price_gas - 0.08
#         all_price = quantity_fuel * price_gas
#     elif club_card == "No":
#         all_price = quantity_fuel * price_gas
# elif fuel_name == "Gasoline":
#     if club_card == "Yes":
#         price_gasoline = price_gasoline - 0.18
#         all_price = quantity_fuel * price_gasoline
#     elif club_card == "No":
#         all_price = quantity_fuel * price_gasoline
# elif fuel_name == "Diesel":
#     if club_card == "Yes":
#         price_diesel = price_diesel - 0.12
#         all_price = quantity_fuel * price_diesel
#     elif club_card == "No":
#         all_price = quantity_fuel * price_diesel
# if 20 < quantity_fuel <= 25:
#     all_price = all_price * 0.92
# elif quantity_fuel > 25:
#     all_price = all_price * 0.90
# print(f"{all_price:.2f} lv.")

fuel_name = input()
quantity_fuel = float(input())
club_card = input()

price_gas = 0.93
price_gasoline = 2.22
price_diesel = 2.33
all_price = 0

if club_card == "Yes":
    if fuel_name == "Gas":
        price_gas = price_gas - 0.08
        if 20 < quantity_fuel <= 25:
            all_price = (price_gas * quantity_fuel) * 0.92
        elif quantity_fuel > 25:
            all_price = (price_gas * quantity_fuel) * 0.90
        else:
            all_price = price_gas * quantity_fuel
    elif fuel_name == "Gasoline":
        price_gasoline = price_gasoline - 0.18
        if 20 < quantity_fuel <= 25:
            all_price = (price_gasoline * quantity_fuel) * 0.92
        elif quantity_fuel > 25:
            all_price = (price_gasoline * quantity_fuel) * 0.90
        else:
            all_price = price_gasoline * quantity_fuel
    elif fuel_name == "Diesel":
        price_diesel = price_diesel - 0.12
        if 20 < quantity_fuel <= 25:
            all_price = (price_diesel * quantity_fuel) * 0.92
        elif quantity_fuel > 25:
            all_price = (price_diesel * quantity_fuel) * 0.90
        else:
            all_price = price_diesel * quantity_fuel
if club_card == "No":
    if fuel_name == "Gas":
        price_gas = 0.93
        if 20 < quantity_fuel <= 25:
            all_price = (price_gas * quantity_fuel) * 0.92
        elif quantity_fuel > 25:
            all_price = (price_gas * quantity_fuel) * 0.90
        else:
            all_price = price_gas * quantity_fuel
    elif fuel_name == "Gasoline":
        price_gasoline = 2.22
        if 20 < quantity_fuel <= 25:
            all_price = (price_gasoline * quantity_fuel) * 0.92
        elif quantity_fuel > 25:
            all_price = (price_gasoline * quantity_fuel) * 0.90
        else:
            all_price = price_gasoline * quantity_fuel
    elif fuel_name == "Diesel":
        price_diesel = 2.33
        if 20 < quantity_fuel <= 25:
            all_price = (price_diesel * quantity_fuel) * 0.92
        elif quantity_fuel > 25:
            all_price = (price_diesel * quantity_fuel) * 0.90
        else:
            all_price = price_diesel * quantity_fuel
print(f"{all_price:.2f} lv.")\