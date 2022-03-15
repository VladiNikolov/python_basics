students = int(input())
#grade = float(input())
average = 0
count_fail = 0
count_middle = 0
count_good = 0
count_best = 0
grade_sum = 0

for i in range(0, students):
    grade = float(input())
    grade_sum = grade_sum + grade
    if 2.00 <= grade <= 2.99:
        count_fail += 1
    elif grade <= 3.99:
        count_middle += 1
    elif grade <= 4.99:
        count_good += 1
    elif grade <= 6.00:
        count_best += 1

    average = grade_sum / students
print(f"Top students: {(count_best / students) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(count_good / students) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(count_middle / students) * 100:.2f}%")
print(f"Fail: {(count_fail / students) * 100:.2f}%")
print(f"Average: {average:.2f}")
