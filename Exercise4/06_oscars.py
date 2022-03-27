# name_actor = input()
# points_from_academy = float(input())
# number_evaluators = int(input())
# all_points = 0
# total_point = 0
# for i in range(number_evaluators):
#     name_evaluator = input()
#     points_from_evaluator = float(input())
#     all_points = len(name_evaluator) * points_from_evaluator / 2
#     total_point = total_point + all_points
#
#     if total_point + points_from_academy > 1250.5:
#         break
# difference = abs((total_point + points_from_academy) - 1250.5)
# if total_point + points_from_academy > 1250.5:
#     print(f"Congratulations, {name_actor} got a nominee for leading role with {total_point + points_from_academy:.1f}!")
# else:
#     print(f"Sorry, {name_actor} you need {difference:.1f} more!")

name_actor = input()
points_from_academy = float(input())
number_evaluators = int(input())
all_points = 0
total_point = 0
current_points = 0
for i in range(number_evaluators):
    name_evaluator = input()
    points_from_evaluator = float(input())
    all_points = len(name_evaluator) * points_from_evaluator / 2
    points_from_academy = points_from_academy + all_points
    current_points = points_from_academy
    if current_points > 1250.5:
        break
difference = abs(current_points - 1250.5)
if current_points > 1250.5:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {current_points:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {difference:.1f} more!")

