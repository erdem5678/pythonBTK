'''
   module1 (db)  : urunler
   module2 (methods)  : urunEkle(), urunGuncelle(), urunGetir()
   moduel3 (app)

        yeni ürün ekle => urunEkle("İPhone 15", 60000)
        ürürn güncelleme => urunGuncelleme(1, "İphone 15 pro", 80000)
        ürünleri listele =>urunleriGetir()
'''

from methods import *
sonuc =urunleriGetir()

urunEkle("İphone 20", 90000)
urunEkle("samsung s20", 90000)

for i in urunleriGetir():
    print(i["urunAdi"]) #  print(i["urunAdi"])

urunGuncelle(1, "İPhone 15 pro", 80000)

for i in urunleriGetir():
    print(i["urunAdi"])