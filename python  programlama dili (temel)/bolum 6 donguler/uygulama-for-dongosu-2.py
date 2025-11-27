urunler =[
{"urunAdi": "Hp Victus", "fiyat": 32999},
{"urunAdi": "Lenovo ThinkPad", "fiyat": 25499}, 
{"urunAdi": "Apple Macbook","fiyat": 49999},
{"urunAdi": "Huawei Matebook", "fiyat": 26999},
{"urunAdi": "Casper Nirvana","fiyat": 20000},
{"urunAdi": "Hp Victus", "fiyat": 30000},
]

# 1- Aşagıdaki örnek çümleyi tüm ürünleri uygulayınız 
# "hp victus marka ürünün fiyatı 32999 türk lirsı "
for urun in urunler:
    print(f"{urun["urunAdi"]}marka urunun fiyati {urun["fiyat"]} TL ")

# 2-ürünleri fiyatını toplamı nedir 
toplam = 0
for urun in urunler:
    toplam += urun["fiyat"]
print(f"urun tolami: {toplam} ")


# 3- 2500 ile 4000 arasındaki ürünlerin isteleyiniz 
for  urun in urunler:
    if (urun["fiyat"] >= 25000 and urun ["fiyat"] <= 40000):
        print(f"{urun["urunAdi"]}")
# 4 - kullanıcıdan alınan anhtar kelimeyi göre ürünleri listeleyiniz 
kelime = input("aramak isdediginiz urun: ")

for urun in urunler:
    if(urun["urunAdi"].lower().find(kelime.lower()) > -1):
        print(f"{urun['urunAdi']}")