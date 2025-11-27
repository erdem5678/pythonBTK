# bir aracın yakıt tipin göre (benzindizel,lpg) belirtilen bir mesafede nekadar yakıt masrafı oldugunu hesaplayan uygulmayı yapınız 
# benzin     : 39.35
# dizel      : 41.71
# lpg        : 20.28 

benzinFiyat = 39.35
dizelFiyat = 41.71
lpgFiyat = 20.28

toplamTakitUcreti = 0
ortalamaYakittuketimi = float(input("100 km deki ortalama yakit tuketimi: "))
gidilecekYol = float(input("gidilen mesafe: "))
yakitTipi = input("yakit tipi: ")

toplamTakitTuketimi = gidilecekYol * (ortalamaYakittuketimi / 100)

if(yakitTipi == "benzin"):
    toplamTakitUcreti = benzinFiyat * toplamTakitTuketimi   # burada pass yer tutcu olarak görev alır 
elif (yakitTipi == "dizel"):
    toplamTakitUcreti = dizelFiyat * toplamTakitTuketimi  
elif (yakitTipi == "lpg"):
   toplamTakitUcreti = lpgFiyat * toplamTakitTuketimi  
else:
   print("yanlis yakit tipi")

if(toplamTakitUcreti != 0):
    print(toplamTakitUcreti)

# bir ögrencinin 2 yazılı bir sözl notunu alarak ortalma hesaplayınız ve hesaplanan ortalmayı göre not aralıgını karşılık gelen degerlendrimeyi yazdırınız 
#   0-24 => 0
#   25-44 => 1
#   45-54 => 2
#   55-69 => 3
#   70-84 => 4
#   85-100 => 5