product = input()
town = input()
quantity = float(input())

price = 0
if town == "Sofia" and product == "coffee":
    price = 0.50
elif town == "Sofia" and product == "water":
    price = 0.80
elif town == "Sofia" and product == "beer":
    price = 1.20
elif town == "Sofia" and product == "sweets":
    price = 1.45
elif town == "Sofia" and product == "peanuts":
    price = 1.60
elif town == "Plovdiv" and product == "coffee":
    price = 0.40
elif town == "Plovdiv" and product == "water":
    price = 0.70
elif town == "Plovdiv" and product == "beer":
    price = 1.15
elif town == "Plovdiv" and product == "sweets":
    price = 1.30
elif town == "Plovdiv" and product == "peanuts":
    price = 1.50
elif town == "Varna" and product == "coffee":
    price = 0.45
elif town == "Varna" and product == "water":
    price = 0.70
elif town == "Varna" and product == "beer":
    price = 1.10
elif town == "Varna" and product == "sweets":
    price = 1.35
elif town == "Varna" and product == "peanuts":
    price = 1.55
total_price = price * quantity
print(total_price)
