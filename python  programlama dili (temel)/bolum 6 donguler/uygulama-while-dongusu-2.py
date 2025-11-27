# klavyeden girilen n sayusının ögrencii bilgilerini liste içersinde saklayınız
#     ** dictionary listesi yapısı (ogrencino , oogrenciAdi, ogrendiSoyadi) şeklinde olsun 
#     ** ögrenci ekleme işlemi bittiginde  ögrenciler listeleyinz 
devammi = "e" # evet
ogrenciler = []
while (devammi != "h"): # hayır
    ogrenciNo = input("ogrenci no: ") 
    ogrenciAdi = input("ogrenci adi: ") 
    ogrencisoyadi = input("ogrenci soyadi: ") 
    ogrenciler.append({
        "ogrenciNo" : ogrenciNo,
        "ogrenciAdi" : ogrenciAdi,
        "ogrencisoyadi" : ogrencisoyadi,
    })

    devammi = input("devam mi  (e/h): ")


for ogreci in ogrenciler:
    print(f"{ogreci["ogrenciNo"]} numrasi ogrecinin adi {ogreci["ogrenciAdi"]} {ogreci["ogrencisoyadi"]}")