# 1 - kendisine gönderilen bir kelimeyi belirtile kez ekrana gösteren fonksiyonu yazınız
def yazdir(kelime,adet):
    return kelime * adet
# print(yazdir("merhaba ", 5)) # input ilede girdi alına bilir

# 2 - dikdörtgenin alanı ve cevresini hesaplayan fonksiyonu yazınız 
def hesapla(kisa, uzun):
    alan = kisa * uzun
    cevre = 2 * (kisa + uzun)

    return f"alan: {alan}, cevre: {cevre}"
sonuc = hesapla(3,5)
print(sonuc)

# 3 - yazı tura uygulmasını fonksiyon kullanarak yapınız(random modülü)
def yaziTura():
    import random
    sayi = random.random()

    if sayi > 0.5:
        return "Tura"
    else:
        return "yazi"
sonuc = yaziTura()
print(sonuc)

# 4 - kedisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız 

def asalSayilarBul(sayi1,sayi2):
    for sayi in range(sayi1, sayi2 + 1):
        if (sayi > 1):
         for i in range(2, sayi):
             if sayi % i == 0 :
                 break
             else:
                 print(sayi)
asalSayilarBul(10,50)

# 5 - kedisine gönderilen bir sayının tam bölnelerini bir liste şeklinede döndüren fonksiyon yazınız
def tambolenler(sayi):
    tambolenler = []
    for i in range(2, sayi):
        if (sayi % i == 0):
            tambolenler.append(i)

    return tambolenler
print(tambolenler(20))