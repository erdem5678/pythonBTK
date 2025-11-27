import module

sonuc = module.sayi
sonuc = module.sayilar
sonuc = module.urun
sonuc = module.urun["urunAdi"]
sonuc = module.urun["renkler"]
sonuc = module.toplam(10,20)


import module as m # module takma isimde verile bilir 
sonuc = m.sayilar

from module import sayi, sayilar, urun  # from kulanarak modul ekini kullnamamıza gerek kalmaz 
sonuc = sayi
sonuc = sayilar
sonuc = urun

from module import * # burda ise modele.py dosyasının içindki tüm degişkenleri ala bilirim 
sonuc = urun
sonuc = toplam(10,20)
print(sonuc)



