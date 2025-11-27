sayilar = [3,5,7,2,12,32,45]

# 1- "sayilar"listesindeki her bir elamanı yazdır 

for x in sayilar:
    print(x)

# 2- "sayilar" listesindeki  hangi sayının 3 katıdır 

for sayi in sayilar:
    if sayi % 3 == 0:
        print(sayi)

# 3- "sayilar" listesindeki tüm sayiları toplamı nedir 

toplam = 0
for sayi in sayilar:
    toplam += sayi
print(toplam)

urunler = ["iphone 12","samsung s24","samsung s22","iphone 15","iphone 14"]

# 4- "urunler" listesindeki tüm iphone marka rünleri listeleyiniz (find index) # index elmanı bulmasa hatta verir 
# index elmanı bulmasa hatta verir 
#find eger bulmasa -1 verir bulrsa 0 verir

for urun in urunler:
    index = urun.find('iphone')
    if index > -1:
        print(urun)

# 5- "urunler" listesinde kaç adet samsung üürün vardır 
adet = 0
for urun in urunler:
    index = urun.find('samsung')
    if index > -1:
        adet += 1
print(adet)