town = input()
sales = float(input())

commissions = 0
if town == "Sofia" and 0 <= sales <= 500:
    commissions = 0.05
elif town == "Sofia" and sales <= 1000:
    commissions = 0.07
elif town == "Sofia" and sales <= 10000:
    commissions = 0.08
elif town == "Sofia" and sales > 10000:
    commissions = 0.12
if town == "Varna" and 0 <= sales <= 500:
    commissions = 0.045
elif town == "Varna" and sales <= 1000:
    commissions = 0.075
elif town == "Varna" and sales <= 10000:
    commissions = 0.10
elif town == "Varna" and sales > 10000:
    commissions = 0.13
if town == "Plovdiv" and 0 <= sales <= 500:
    commissions = 0.055
elif town == "Plovdiv" and sales <= 1000:
    commissions = 0.08
elif town == "Plovdiv" and sales <= 10000:
    commissions = 0.12
elif town == "Plovdiv" and sales > 10000:
    commissions = 0.145
sum = sales * commissions

if sales < 0 or commissions == 0:
    print("error")
else:
    print(f"{sum:.2f}")