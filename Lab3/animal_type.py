animal = input()

animal_type1 = animal == 'dog'
animal_type2 = animal == 'crocodile' or animal == 'tortoise' or animal == 'snake'

if animal_type1:
    print('mammal')
elif animal_type2:
    print('reptile')
else:
    print('unknown')