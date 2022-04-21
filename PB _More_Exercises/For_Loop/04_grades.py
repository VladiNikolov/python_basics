count_students = int(input())
all_sum_grades = 0
number_middle_grades = 0
number_good_grades = 0
number_very_good_grades = 0
number_excellent_grades = 0
for i in range(1, count_students + 1):
    exam_grade = float(input())
    all_sum_grades += exam_grade
    if 2 <= exam_grade <= 2.99:
        number_middle_grades += 1
    elif 3 <= exam_grade <= 3.99:
        number_good_grades += 1
    elif 4 <= exam_grade <= 4.99:
        number_very_good_grades += 1
    else:
        number_excellent_grades += 1
print(f"Top students: {number_excellent_grades / count_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {number_very_good_grades / count_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {number_good_grades / count_students * 100:.2f}%")
print(f"Fail: {number_middle_grades / count_students * 100:.2f}%")
print(f"Average: {all_sum_grades / count_students:.2f}")

