depozirana_suma = float(input()) #200
srok_depozit = int(input()) #3
godishen_procent = float(input()) #5.7

suma_zagodina = depozirana_suma * (godishen_procent / 100)
suma_zamesec = suma_zagodina / 12

total = depozirana_suma + (srok_depozit * suma_zamesec)
print(total)

#suma = depozirana_suma  + srok_depozit * ((depozirana_suma * godishen_procent) / 12)
#print(suma)