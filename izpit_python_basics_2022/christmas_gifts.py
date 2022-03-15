#years = int(input())
command = input()

kids_counter = 0
adults_counter = 0


while command != "Christmas":
    current_number = int(command)
    if 0 <= current_number <= 16:
        kids_counter += 1
    elif current_number > 16:
        adults_counter += 1

    command = input()
print(f"Number of adults: {adults_counter}")
print(f"Number of kids: {kids_counter}")
print(f"Money for toys: {kids_counter * 5}")
print(f"Money for sweaters: {adults_counter * 15}")





