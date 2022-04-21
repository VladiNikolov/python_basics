period = int(input())
doctors = 7
reviewed = 0
not_reviewed = 0

for days in range(1, period + 1):
    current_patients = int(input())
    if days % 3 == 0:
        if not_reviewed > reviewed:
            doctors += 1
    if current_patients <= 7:
        reviewed += current_patients
    else:
        not_reviewed += current_patients - doctors
        reviewed += doctors

print(f"Treated patients: {reviewed}.")
print(f"Untreated patients: {not_reviewed}.")

