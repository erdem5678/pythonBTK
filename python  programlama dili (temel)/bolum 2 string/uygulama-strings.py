title = "python ile programlama dersleri"

# 1 - 'title'  degişken içindeki karakter sayısı nedir 

adet=len(title)# 31
print(adet)
# 2 - 'title' içerisindeki 'python' kelimesini alın 
print(title[:6])

# 3 - 'title' degişkenin ilk 5 ve son 5 karakterin alın
print(title[:6])
print(title[-8:])
# 4 - 'title' degişkenini tersden yazdrının 
print(title[::-1])
print(title[::1])
# 5 - klavyeden girilen  ögrenci bilgisini göre örnek verilen çümleyi yazdırınız.
#  örnek : çınar turan isimli ögrencinin 1.notu 60, 2. notu 60 ve not ortalmasını 60 olarak hesaplayınız 
ad = input('ad: ')
soyad = input('soyad:') 
not1 = input('1. not:')
not2 = input('2. not:')
ortalama = (float(not1) + float(not2)) / 2


sonuc = f" {ad} {soyad} isimli ögrencinin 1. notu {not1}, 2 notu {not2} ve not ortalmasini {ortalama} olarak hesaplanmiştir "
print(sonuc)