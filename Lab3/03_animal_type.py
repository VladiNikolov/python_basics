# animal = input()
# animal_type = "unknown"
# if animal == "dog":
#     animal_type = "mammal"
# elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
#     animal_type = "reptile"
# print(animal_type)

animal = input()

if animal == "dog":
    print("mammal")
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    print("reptile")
else:
    print("unknown")