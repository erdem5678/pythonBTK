# 1- yaşı 18 den büyük yada veli izni varsa bir işte çalışabilir durumunu kntrol ediniz
veli_izni = False

yas  = 18 # veli izni false olsada yaş dan kurtardıgı için çıktı True olur 

sonuc = (veli_izni) or (yas >= 18)

# 2- ders notu 50-100 arasındaysa geçti degilse kalsın bilgisini yazdırınız 
dersNot = int(input("ders notu gir: ")) 

sonuc = (dersNot >= 50) and (dersNot <= 100)

print(f"ders gecme durumu:  {sonuc}")

# 3- not ort6alması en az 70 puan ve zayıf yoksa teşekkürler  belge alabilme durumunu kontrol ediniz

ortalama = int(input("ortalama gir: "))#ortalama = 70 böylede yazıla bilit

zayifsayisi = 0

sonuc = (ortalama >= 70) and (zayifsayisi == 0) 

# 4- işe girme için en az önlisans yada lisans mezunu olam durumunu kontrol ediniz. sigara kulanmama koşulu
egitim = input("egitim durumu: ")

siagara_icme = False

sonuc = (egitim == "önlisans" or egitim == "lisans") and (not(siagara_icme))

# 5- uygulmaya giriş kontrolünü "username yada email" ve "parola" için yapın

email = "info@sadikturan.com"
username = "sadikturan"
password = "12345"

girilen_bilgi = input("email yada username: ")
girilen_parola = input("parola: ")

sonuc = (email == girilen_bilgi or username == girilen_bilgi) and (password == girilen_parola)
print(sonuc)
