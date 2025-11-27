liste =["1","3","5","20b","abc","10a","60"]

# 1- liste elemanları içindeki sayısal degerleri bulunuz
for x in liste:
    try:
        sonuc = int(x)
        print(sonuc)
    except ValueError:
        continue

# 2- kullanıcı 'quit(q)' degerini girmedikce aldıgınız her inputun sayı oldugunu emin olunuz
#aksi yaktirde hata mesajı alırsınız


while True:
    sayi = input("sayi: ")
    if sayi == "q":
        break
    try:
        sonuc = float(sayi)
        print(f"girilen sai: {sonuc}")
    except ValueError:
        print("gecersiz sayi")
        continue

# 3- Dictionary ve key bilgilerini paremetre olarak alan get (dict, key ) fonksiyonu hazırlayınız
urun = {"urunAdi":"samsung s10","fiyat":10000}
# d["fiyat"] => KeyError
# get(urun, "fiyatı") => none
# get(urun, "urunAdi")=> samsung s10

def get(liste, key):

    try:
        return liste[key]
    except KeyError:
        return None
    
sonuc = get(urun, "fiyat")
sonuc = get(urun, "urunAdi")


print(sonuc)