# 1 - "toyota , Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
markalar = ["Toyota", "Bmw", "Renault", "Mercedes"]
# 2- Liste kaç elemanlıdır?
sonuc = len(markalar)
#3-Listenin ilk ve son elemanı nedir
sonuc = markalar[0]
sonuc = markalar[-1]

# 4-"Renault" markasını "Togg" ile güncelleyiniz.
markalar[2] = "togg"
sonuc = markalar

#5-"Togg" listenin bir elemanı mıdır?
sonuc = "togg" in markalar
sonuc = "togg" not in markalar
# 6- Listenin ilk 2 elemanını alınız.
sonuc = markalar[:2]

# 7- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
sonuc = markalar + ["ford" , "Citroen"]

#8- Listenin son elemanını siliniz.
del markalar[-1]
sonuc = markalar


# 9- Aşağıdaki verileri liste içerisinde saklayınız.
# öğrencil: Yiğit Bilgi 2010 [70,80,90]
#öğrenci2: Ada Bilgi2011 [70,70,80]
#öğrenci3: Çınar Turan 2017 [60,60,90]

ogrenci1 = ["yigit" , "bilgi" , 2010 ,[70,80,90]]
ogrenci2 = ["ada" , "bilgi" , 2012 ,[70,70,80]]
ogrenci3 = ["cinar" , "turan" , 2017 ,[60,60,90]]

ogrenciler = [ogrenci1,ogrenci2,ogrenci3] #print(ogrenciler[0])

#10- Öğrencilerin yaşlarını hesaplayınız.
#yasYigit = 2024 - ogrenci1[2]
# yasAda = 2024 - ogrenci2[2]
# yasCinar = 2024 - ogrenci3[2]

yasYigit = 2024 - ogrenciler[0][2]
yasAda = 2024 - ogrenciler[1][2]
yasCinar = 2024 - ogrenciler[2][2]
print(yasYigit, yasAda ,yasCinar)
#11- Öğrencilerin not ortalamalarını hesaplayınız

notYigit = (ogrenciler[0][3][0] + ogrenciler[0][3][1]  + ogrenciler[0][3][2])/ 3 # yigit alıyor ve sonra [70,80,90] buraya geliyor :ve bu liste içinde 0 index alıyor yani '70'
notada = (ogrenciler[1][3][0] + ogrenciler[1][3][1]  + ogrenciler[1][3][2])/ 3 
notCinar = (ogrenciler[0][3][0] + ogrenciler[0][3][1]  + ogrenciler[0][3][2])/ 3

print(notYigit , notada , notCinar)
print(sonuc)