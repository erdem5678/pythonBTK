# liste = [12, 45, -3, 7, 0, 33]
# sonuc = min(liste)
# sonuc = max(liste)
# print(sonuc)
liste = [12, 45, -3, 7, 0, 33]

en_kucuk = liste[0]
en_buyuk = liste[0]

for i in liste:
    if i < en_kucuk:
        en_kucuk = i
    if i > en_buyuk:
        en_buyuk = i

print("En kucuk:", en_kucuk)
print("En buyuk:", en_buyuk)

