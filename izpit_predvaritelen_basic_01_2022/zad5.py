command = input()
start_meters = 5364
targer_meters = 8848
days = 1
sum_meters = start_meters
while command != "END":
    meters = int(input())
    if command == "Yes":
        days += 1
        if days > 5:
            print("Failed!")
            print(f"{sum_meters}")
            break
        sum_meters = sum_meters + meters
        if sum_meters >= targer_meters:
            print(f"Goal reached for {days} days!")
            break

    elif command == "No":
        sum_meters = sum_meters + meters
        if sum_meters >= targer_meters:
            print(f"Goal reached for {days} days!")
            break
        elif days >= 5:
            if sum_meters >= targer_meters:
                print(f"Goal reached for {days} days!")
                break
            else:
                print("Failed!")
                print(f"{sum_meters}")
                break

    command = input()

if command == "END":
    if sum_meters >= targer_meters:
        print(f"Goal reached for {days} days!")
    else:
        print("Failed!")
        print(f"{sum_meters}")