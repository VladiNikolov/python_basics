#The architect {името на архитекта} will need {необходими часове} hours to complete {брой на проектите} project/s."

name = input()
count_projects = int(input())
all_hours = count_projects * 3
#print(all_hours)
print(f'The architect {name} will need {all_hours} hours to complete {count_projects} project/s.')
