number_of_jury = int(input())
presentation_text = input()
total_average_sum = 0
count = 0
while presentation_text != "Finish":
    current_sum = 0

    for i in range(number_of_jury):
        current_point = float(input())
        current_sum += current_point
        count += 1

    average_sum = current_sum / number_of_jury
    total_average_sum += current_sum
    print(f"{presentation_text} - {average_sum:.2f}.")

    presentation_text = input()
all_avg = total_average_sum / count
print(f"Student's final assessment is {all_avg:.2f}." )