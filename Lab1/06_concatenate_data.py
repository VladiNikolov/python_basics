first_name = input()
last_name = input()
age = int(input())
town = input()

print(f"You are {first_name} {last_name}, a {age}-years old person from {town}.") # решение с f-string форматиране
print("You are " + first_name + " " + last_name + ", a " + str(age) + "-years old person from" + " " + town + ".") # решение с конкатенация
