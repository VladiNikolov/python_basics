# •	Първият ред – отбор – текст с възможности: "Argentina", "Brazil", "Croatia", "Denmark"
# •	Вторият ред – вид сувенири – текст с възможности: "flags", "caps", "posters", "stickers"
# •	Третият ред – брой закупени сувенири – цяло число в интервала [1…200]

team = input()
souvenir = input()
number_souvenir = int(input())


if team == "Argentina":
    if souvenir == "flags":
        all_number_souvenir = number_souvenir * 3.25
    elif souvenir == "caps":
        all_number_souvenir = number_souvenir * 7.20
    elif souvenir == "posters":
        all_number_souvenir = number_souvenir * 5.10
    elif souvenir == "stickers":
        all_number_souvenir = number_souvenir * 1.25
elif team == "Brazil":
    if souvenir == "flags":
        all_number_souvenir = number_souvenir * 4.20
    elif souvenir == "caps":
        all_number_souvenir = number_souvenir * 8.50
    elif souvenir == "posters":
        all_number_souvenir = number_souvenir * 5.35
    elif souvenir == "stickers":
        all_number_souvenir = number_souvenir * 1.20
elif team == "Croatia":
    if souvenir == "flags":
        all_number_souvenir = number_souvenir * 2.75
    elif souvenir == "caps":
        all_number_souvenir = number_souvenir * 6.90
    elif souvenir == "posters":
        all_number_souvenir = number_souvenir * 4.95
    elif souvenir == "stickers":
        all_number_souvenir = number_souvenir * 1.10
elif team == "Denmark":
    if souvenir == "flags":
        all_number_souvenir = number_souvenir * 3.10
    elif souvenir == "caps":
        all_number_souvenir = number_souvenir * 6.50
    elif souvenir == "posters":
        all_number_souvenir = number_souvenir * 4.80
    elif souvenir == "stickers":
        all_number_souvenir = number_souvenir * 0.90

if team == "Argentina" or team == "Brazil" or team == "Croatia" or team == "Denmark":
    if souvenir == "flags" or souvenir == "caps" or souvenir == "posters" or souvenir == "stickers":
        if number_souvenir < 0:
            print(f"Pepi bought {number_souvenir} {souvenir} of {team} for 0.00 lv.")
        else:
            print(f"Pepi bought {number_souvenir} {souvenir} of {team} for {all_number_souvenir:.2f} lv.")

    elif souvenir != "flags" or souvenir != "caps" or souvenir != "posters" or souvenir != "stickers":
        print("Invalid stock!")

#elif team != "Argentina" or team != "Brazil" or team != "Croatia" or team != "Denmark":
else:
    print("Invalid country!")








