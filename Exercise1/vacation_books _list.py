br_stranici = int(input())
stranici_chas = int(input())
dni = int(input())

obshto_str = br_stranici / stranici_chas
total_str = obshto_str / dni
print(round(total_str, 0))