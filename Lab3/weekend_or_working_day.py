day = input()

is_working_day = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday'
is_weekend = day == 'Saturday' or day == 'Sunday'

if is_working_day:
    print('Working day')
elif is_weekend:
    print('Weekend')
else:
    print('Error')
