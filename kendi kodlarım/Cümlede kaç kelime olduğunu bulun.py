# cümle = input("bir çümle giriniz: ")
# kelime_sayisi = len(cümle.split())
# print(kelime_sayisi)

cumle = input("Bir cumle girin: ")

kelime_sayisi = 0
onceki_bosluk = True

for karakter in cumle:
    if karakter != ' ':
        if onceki_bosluk:
            kelime_sayisi += 1
        onceki_bosluk = False
    else:
        onceki_bosluk = True

print("Kelime sayisi:", kelime_sayisi)
