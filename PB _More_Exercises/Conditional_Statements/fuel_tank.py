# name_fuel = input()
# liters_fuel = float(input())
#
# if name_fuel == "Diesel":
#     if liters_fuel < 25:
#         print(f"Fill your tank with {str.lower(name_fuel)}!")
#     elif liters_fuel >= 25:
#         print(f"You have enough {str.lower(name_fuel)}.")
# elif name_fuel == "Gasoline":
#     if liters_fuel < 25:
#         print(f"Fill your tank with {str.lower(name_fuel)}!")
#     elif liters_fuel >= 25:
#         print(f"You have enough {str.lower(name_fuel)}.")
# elif name_fuel == "Gas":
#     if liters_fuel < 25:
#         print(f"Fill your tank with {str.lower(name_fuel)}!")
#     elif liters_fuel >= 25:
#         print(f"You have enough {str.lower(name_fuel)}.")
# else:
#     print(f"Invalid fuel!")

name_fuel = input()
liters_fuel = float(input())

if liters_fuel < 25 and (name_fuel == "Diesel" or name_fuel == "Gasoline" or name_fuel == "Gas"):
    print(f"Fill your tank with {str.lower(name_fuel)}!")
elif liters_fuel >= 25 and (name_fuel == "Diesel" or name_fuel == "Gasoline" or name_fuel == "Gas"):
        print(f"You have enough {str.lower(name_fuel)}.")
else:
    print(f"Invalid fuel!")