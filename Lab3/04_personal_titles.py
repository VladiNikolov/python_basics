# age = float(input())
# sex = input()
#
# if age < 16:
#     if sex == "m":
#         print("Master")
#     elif sex == "f":
#         print("Miss")
# elif age >= 16:
#     if sex == "m":
#         print("Mr.")
#     elif sex == "f":
#         print("Ms.")

# age = float(input())
# sex = input()
# address = ""
# if age < 16:
#     if sex == "m":
#         address = "Master"
#     elif sex == "f":
#         address = "Miss"
# elif age >= 16:
#     if sex == "m":
#         address = "Mr."
#     elif sex == "f":
#         address = "Ms."
# print(address)

age = float(input())
sex = input()
address = ""
if age < 16 and sex == "m":
        address = "Master"
elif age < 16 and sex == "f":
        address = "Miss"
elif age >= 16 and sex == "m":
        address = "Mr."
elif age >= 16 and sex == "f":
        address = "Ms."
print(address)

