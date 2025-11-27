#Çift toplam = 42
#Tek adet = 3
#Kullanıcıdan 10 adet tam sayı alıp bir listeye kaydet.
#Sonra bu listede:
#Çift sayıların toplamını
#Tek sayıların sayısını
#hesaplayıp ekrana yazdır.

liste = []
cift_toplam = 0     
tek_adet = 0

for i in range(10):
    sayi = int(input("Sayi gir: "))
    liste.append(sayi)

for sayi in liste:
   if sayi % 2 == 0:
      cift_toplam += sayi
   else:
       tek_adet += 1


print("cift topam = ", cift_toplam)
print("tek adet = ", tek_adet)
