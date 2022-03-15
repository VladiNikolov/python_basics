price_flour = float(input())
kilograms_flour = float(input())
kilograms_shugar = float(input())
number_eggshells = int(input())
package_maya = int(input())

price_sugar = price_flour * 0.75
price_number_eggshells = price_flour * 1.1
price_package_maya = price_sugar * 0.20
total_price_flour = price_flour * kilograms_flour
total_price_sugar = kilograms_shugar * price_sugar
total_price_eggshells = number_eggshells * price_number_eggshells
total_price_maya = package_maya * price_package_maya
all_price_needed = total_price_flour + total_price_sugar + total_price_eggshells + total_price_maya
print(f'{all_price_needed}')