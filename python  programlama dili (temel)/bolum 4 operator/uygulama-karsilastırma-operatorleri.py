# 1- girilen 2 sayıdan hangisis büyüktür 
sayi1 = int(input("sayi1: "))
sayi2 = int(input("sayi2: "))

sonuc = (sayi1 > sayi2 )
print(f"{sayi1} {sayi2} den büyüktür {sonuc}")


# 2- girilen sayının tek miçift mi oldugunu kontrol ediniz 
sayi = int(input("sayi : "))
sonuc = (sayi % 2 == 0) #  tek mi çift mi sorgular 
print(f"sayi çift{sonuc}")

# 3- bir ögrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz 50 ce üstünü başaralı .
not1 = int(input("not 1 giriniz: "))
not2 = int(input("not 2 giriniz: "))
not3 = int(input("not 3 giriniz: "))

ortalama = (not1 + not2 + not3)/3
print(f"ogrencinin not ortalmasi: {round(ortalama)}, başari durumu {ortalama >= 50}")# round fonsiyonu çıkan ortlama yı yuvralar 