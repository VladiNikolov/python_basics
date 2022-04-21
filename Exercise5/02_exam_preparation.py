# bad_grades = int(input())
#
# sum_grades = 0
# count_grades = 0
# last_task_name = ""
# count_bad_grades = 0
# is_failed = False
# task_name = input()
# while task_name != "Enough":
#     rating = int(input())
#     if rating <= 4:
#         count_bad_grades += 1
#
#     last_task_name = task_name
#     sum_grades += rating
#     count_grades += 1
#
#     if bad_grades == count_bad_grades:
#         is_failed = True
#         break
#     task_name = input()
# if is_failed:
#     print(f"You need a break, {count_bad_grades} poor grades.")
# else:
#     print(f"Average score: {sum_grades / count_grades:.2f}")
#     print(f"Number of problems: {count_grades}")
#     print(f"Last problem: {last_task_name}")
#
bad_grades = int(input())

sum_grades = 0
count_grades = 0
last_task_name = ""
count_bad_grades = 0
task_name = input()
while task_name != "Enough":
    rating = int(input())
    if rating <= 4:
        count_bad_grades += 1

    last_task_name = task_name
    sum_grades += rating
    count_grades += 1

    if bad_grades == count_bad_grades:
        bad_grades = count_bad_grades
        break
    task_name = input()
if bad_grades == count_bad_grades:
    print(f"You need a break, {count_bad_grades} poor grades.")
else:
    print(f"Average score: {sum_grades / count_grades:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_task_name}")

