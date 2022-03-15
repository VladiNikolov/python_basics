number_of_stydents = int(input())

grade1 = 0
grade2 = 0
grade3 = 0
grade4 = 0
all_grade_of_exam = 0
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
for i in range(number_of_stydents):
    grade_of_exam = float(input())
    all_grade_of_exam += grade_of_exam
    if 2 <= grade_of_exam <= 2.99:
        grade1 += grade_of_exam
        sum1 += 1
    elif 3 <= grade_of_exam <= 3.99:
        grade2 += grade_of_exam
        sum2 += 1
    elif 4 <= grade_of_exam <= 4.99:
        grade3 += grade_of_exam
        sum3 += 1
    else:
        grade4 += grade_of_exam
        sum4 += 1
print(f'Top students: {sum4 / number_of_stydents * 100:.2f}%')
print(f'Between 4.00 and 4.99: {sum3 / number_of_stydents * 100:.2f}%')
print(f'Between 3.00 and 3.99: {sum2 / number_of_stydents * 100:.2f}%')
print(f'Fail: {sum1 / number_of_stydents * 100:.2f}%')
print(f'Average: {all_grade_of_exam / number_of_stydents:.2f}')
