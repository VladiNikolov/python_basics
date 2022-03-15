# •	Първият ред – отбор – текст с възможности: "Argentina", "Brazil", "Croatia", "Denmark"
# •	Вторият ред – вид сувенири – текст с възможности: "flags", "caps", "posters", "stickers"
# •	Третият ред – брой закупени сувенири – цяло число в интервала [1…200]

team = input()
souvenir = input()
number_souvenir = int(input())
price = 0
if team == "Argentina":
    if souvenir == "flags":

        price = 3.25
    elif souvenir == "caps":
        price = 7.20
    elif souvenir == "posters":
        price =  5.10
    elif souvenir == "stickers":
        price =  1.25
elif team == "Brazil":
    if souvenir == "flags":
        price =  4.20
    elif souvenir == "caps":
        price =  8.50
    elif souvenir == "posters":
        price =  5.35
    elif souvenir == "stickers":
        price =  1.20
elif team == "Croatia":
    if souvenir == "flags":
        price =  2.75
    elif souvenir == "caps":
        price =  6.90
    elif souvenir == "posters":
        price =  4.95
    elif souvenir == "stickers":
        price =  1.10
elif team == "Denmark":
    if souvenir == "flags":
        price =  3.10
    elif souvenir == "caps":
        price =  6.50
    elif souvenir == "posters":
        price =  4.80
    elif souvenir == "stickers":
        price =  0.90

all_number_souvenir = number_souvenir * price
if team == "Argentina" or team == "Brazil" or team == "Croatia" or team == "Denmark":
    if souvenir == "flags" or souvenir == "caps" or souvenir == "posters" or souvenir == "stickers":
        if number_souvenir < 0:
            print(f"Pepi bought {number_souvenir} {souvenir} of {team} for 0.00 lv.")
        else:
            print(f"Pepi bought {number_souvenir} {souvenir} of {team} for {all_number_souvenir:.2f} lv.")

    elif souvenir != "flags" or souvenir != "caps" or souvenir != "posters" or souvenir != "stickers":
        print("Invalid stock!")

# elif team != "Argentina" or team != "Brazil" or team != "Croatia" or team != "Denmark":
else:
    print("Invalid country!")








