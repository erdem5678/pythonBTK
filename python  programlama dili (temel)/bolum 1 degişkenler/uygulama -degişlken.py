"""
aşagidaki müşterini bilgilerini ve satın aladıgı ürün bilgilerini degişknler içerinde saklayınız 
toplam ödenen üçret nedir 
ödenen miktarı kdv oranı nedir (%18)


bariş erdem 
544678938
info@erdem.com
bakü
 satın laınan ürünler 
 
ürün adı: kablosuz kullaklı-k
fiyat: 550 tl

ürün adi : kablosuz klavye
fiyat: 650 tl

ürün adi : dizüstü bilgisayar
fiyat:55.000 tl
"""
musteriAd  ="bariş"
musteriSoad = "erdem"
musteriTelefon = 544678938
musteriEmail = "info@erdem.com"
musteriAdres = "bakü"

urun1Ad = "kablosuz kullaklik"
urun1Fiyat = 550,

urun2Asd = " kablosuz klavye"
urun2Fiyat = 650

urun3Ad = "dizüstü bilgisayar"
urun3Fiyat = 55000

toplamOdeneUcret =urun1Fiyat,+ urun2Fiyat, + urun3Fiyat,
print("toplam ödenen miktar:" + str(toplamOdeneUcret))
print("toplam kdv orani:" + str(toplamOdeneUcret * 0.18))

#str(100) = "100" + "ali" =100ali