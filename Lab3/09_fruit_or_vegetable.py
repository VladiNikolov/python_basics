# product = input()
#
# if product == "banana" or product == "apple" or product == "kiwi"\
#         or product == "cherry" or product == "lemon" or product == "grapes":
#     print("fruit")
# elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
#     print("vegetable")
# else:
#     print("unknown")

product = input()

is_fruit = product == "banana" or product == "apple" or product == "kiwi"\
           or product == "cherry" or product == "lemon" or product == "grapes"
is_vegetable = product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot"

if is_fruit == True:
    print("fruit")
elif is_vegetable == True:
    print("vegetable")
else:
    print("unknown")