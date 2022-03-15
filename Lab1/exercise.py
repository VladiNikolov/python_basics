# зад 1. Hello SoftUni
print("Hello SoftUni")

# зад 2. Numbers 1 to 10
for i in range(1, 10+1):
    print(i)

# зад 3. Rectangle Area
side_a = int(input())
side_b = int(input())

area = side_a * side_b
print(area)

# зад 4. Inches to Centimeters
inches = float(input())

centimeters = inches * 2.54
print(centimeters)

# зад 5. Greeting by Name
name = input()

print(f"Hello, {name}!") # решение с f-string форматиране
print("Hello, " + name + "!") # решение с конкатенация


# зад 6. Concatenate Data
first_name = input()
last_name = input()
age = int(input())
town = input()

print(f"You are {first_name} {last_name}, a {age}-years old person from {town}.") # решение с f-string форматиране
print("You are " + first_name + " " + last_name + ", a " + str(age) + "-years old person from" + " " + town + ".") # решение с конкатенация

#зад 7. Projects Creation
name_architect = input()
projects = int(input())

all_hours = projects * 3
print(f"The architect {name_architect} will need {all_hours} hours to complete {projects} project/s.")

#зад 8. Pet Shop
dog_food = int(input())
cat_food = int(input())

price_dog_food = 2.50
price_cat_food = 4

all_price_food = (dog_food * price_dog_food) + (cat_food * price_cat_food)
print(f"{all_price_food} lv.")

#зад 9. Yard Greening
square_meters = float(input())

all_price_square_meters = (square_meters * 7.61)
total_price = all_price_square_meters * 0.82
discount = all_price_square_meters - total_price

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")