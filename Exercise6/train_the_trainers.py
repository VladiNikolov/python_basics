number_of_jury = int(input())
command = input()
total_average = 0
presentations_count = 0

while command != "Finish":

    presentations_count +=1
    current_assessment_sum = 0

    for person in range(number_of_jury):
        current_assessment = float(input())
        current_assessment_sum += current_assessment

    current_average = current_assessment_sum / number_of_jury
    print(f"{command} - {current_average:.2f}.")

    total_average += current_average

    command = input()
average_assessment = total_average / presentations_count
print(f"Student's final assessment is {average_assessment:.2f}." )
