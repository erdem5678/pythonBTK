kurum  = "BTK Akademi" 

print(type(kurum))
print(kurum)
print(kurum[0]) # B
print(kurum[1]) # T

sayilar = [1,2,3,4,5]
isimler = ["ayşe", "mehmet", "bariş"] 

print(type(sayilar))# liste
print(type(sayilar[0])) # int
 
print(type(isimler)) # list
print(type(isimler[0])) # str

ogrenci = ["baris" , "caliskan" ,70,80,70]

print(ogrenci[0] + " " + ogrenci[1]) # baris caliskan
ortalama = (ogrenci[2] + ogrenci[3] + ogrenci[4]) / 3
print(ortalama)

ogrenci = [["baris" , "caliskan" ,70,80,70] , ["can" , "erdem" ,60,100,70]]
print(ogrenci[0][0]) # baris
print(ogrenci[1][1]) # erdem
