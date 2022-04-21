name_film = input()
all_counts = 0
count_students = 0
count_standards = 0
count_kids = 0
while name_film != "Finish":

    movie = name_film
    capacity = int(input())
    count_current_movie = 0
    command = input()
    while command != "End":
        type_ticket = command
        if command == "student":
            count_students += 1
        elif command == "standard":
            count_standards += 1
        elif command == "kid":
            count_kids += 1
        count_current_movie += 1
        all_counts += 1
        if count_current_movie == capacity:
            break
        command = input()
    percent_full = count_current_movie / capacity * 100
    print(f"{movie} - {percent_full:.2f}% full.")

    name_film = input()
print(f"Total tickets: {all_counts}")
print(f"{count_students/ all_counts * 100:.2f}% student tickets.")
print(f"{count_standards/ all_counts * 100:.2f}% standard tickets.")
print(f"{count_kids/ all_counts * 100:.2f}% kids tickets.")


