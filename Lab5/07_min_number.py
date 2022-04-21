import sys

min_number = sys.maxsize
command = input()
while command != "Stop":
    concurrent_number = int(command)
    if concurrent_number < min_number:
        min_number = concurrent_number
    command = input()
print(min_number)