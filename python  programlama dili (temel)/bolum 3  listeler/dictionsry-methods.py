#  dictionary Metotları

yemekTarifi = {
    "yemekAdi": "Musakka",
    "yemekTarifi": "tarif aciklamasi",
    "resim": "1.jpg"
}

# access items

sonuc = yemekTarifi["yemekAdi"]
sonuc = yemekTarifi.get("yemekAdi") # belirlenen key ile value  degerlerini döndürür
sonuc = yemekTarifi.keys() # listedeki key bilgilerini liste şekline döndürür
sonuc = yemekTarifi.values()#listedeki value bilgilerini liste şekline döndürür
sonuc = yemekTarifi.items() # key-value degerini liste şekline döndürür

# uptade items

yemekTarifi["yemekAdi"] = "Manti" #yemekTarifi["yemekAdi2"] = "Manti" eger deger yoksa yeni bir deger yaratır 
yemekTarifi.update({"yemekAdi":"Manti"}) # güncellme için kullanılır 
yemekTarifi.update({"yemekAdi2":"Manti"})


# delet items

yemekTarifi.pop("yemekAdi")
yemekTarifi.popitem()
yemekTarifi.clear()

# copy => referans
sonuc = yemekTarifi
print(sonuc)
