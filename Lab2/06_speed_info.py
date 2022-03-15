# speed = float(input())
#
# result = ""
# if speed <= 10:
#     result = "slow"
# elif speed <= 50:
#     result = "average"
# elif speed <= 150:
#     result = "fast"
# elif speed <= 1000:
#     result = "ultra fast"
# else:
#     result = "extremely fast"
# print(result)

speed = float(input())

if speed <= 10:
    print("slow")
elif speed <= 50:
    print("average")
elif speed <= 150:
    print("fast")
elif speed <= 1000:
    print("ultra fast")
elif speed > 1000:
    print("extremely fast")
