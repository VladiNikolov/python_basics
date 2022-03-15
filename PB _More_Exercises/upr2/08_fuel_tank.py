# fuel_name = input()
# liter_fuel = float(input())
#
# if liter_fuel >= 25 and (fuel_name == "Diesel" or fuel_name == "Gasoline" or fuel_name == "Gas"):
#     print(f"You have enough {(fuel_name.lower())}.")
# elif liter_fuel < 25 and (fuel_name == "Diesel" or fuel_name == "Gasoline" or fuel_name == "Gas"):
#     print(f"Fill your tank with {(fuel_name.lower())}!")
# else:
#     print("Invalid fuel!")

fuel_name = input()
liter_fuel = float(input())

if fuel_name == "Diesel":
    if liter_fuel >= 25:
        print(f"You have enough {(fuel_name.lower())}.")
    elif liter_fuel < 25:
        print(f"Fill your tank with {(fuel_name.lower())}!")
elif fuel_name == "Gasoline":
    if liter_fuel >= 25:
        print(f"You have enough {(fuel_name.lower())}.")
    elif liter_fuel < 25:
        print(f"Fill your tank with {(fuel_name.lower())}!")
elif fuel_name == "Gas":
    if liter_fuel >= 25:
        print(f"You have enough {(fuel_name.lower())}.")
    elif liter_fuel < 25:
        print(f"Fill your tank with {(fuel_name.lower())}!")
else:
    print("Invalid fuel!")
