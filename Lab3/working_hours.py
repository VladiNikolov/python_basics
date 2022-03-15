# time = int(input())
# day = input()
#
# is_working_day = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday'\
#               or day == 'Thursday' or day == 'Friday' or day == 'Saturday'
# weekend_day = day == 'Sunday'
# if is_working_day:
#     if time >= 10 and time <= 18:
#         print('open')
#     #elif time < 10 and time > 18:
#         #print('closed')
#     else:
#          print('closed')
# if  weekend_day:
#     if time >= 10 and time <= 18:
#        print('closed')
#     else:
#         print('closed')

time = int(input())
day = input()

if day == 'Monday' and time >= 10 and time <= 18:
    print('open')
elif day == 'Tuesday' and time >= 10 and time <= 18:
        print('open')
elif day == 'Wednesday' and time >= 10 and time <= 18:
        print('open')
elif day == 'Thursday' and time >= 10 and time <= 18:
        print('open')
elif day == 'Friday' and time >= 10 and time <= 18:
        print('open')
elif day == 'Saturday' and time >= 10 and time <= 18:
        print('open')
else:
        print('closed')
#if day == 'Sunday' and time >= 10 and time <= 18:
   # print('closed')


# time = int(input())
# day = input()
#
# is_working_day = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday'\
#               or day == 'Thusday' or day == 'Friday' or day == 'Saturday'
# #weekend_day = day == 'Sunday'
# if is_working_day:
#     if time >= 10 and time <= 18:
#         print('open')
#     #elif time < 10 and time > 18:
#         #print('closed')
#     else:
#          print('closed')
# # if  weekend_day:
# #     if time >= 10 and time <= 18:
# #        print('closed')
# #     else:
# #         print('closed')
