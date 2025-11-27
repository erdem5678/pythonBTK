mesaj = "  btk Akademi python kursu"
sonuc = mesaj.upper() # tük karakterleri  büyük harfle yazar
sonuc = mesaj.lower() # tük karakterler küçük harfe cevrilir 
sonuc = mesaj.title() # tüm kelimlerin baş harflerini büyük yapar
sonuc = mesaj.capitalize() # sadece stringin baş harfini büyük harf yapar'Btk' olur
sonuc = "abc".isupper() # büyük harf mi
sonuc = "abc".islower() # küçük harf mi
print(mesaj) 
sonuc = mesaj.strip()# çıktının başına boşluk şekilde karakterlerini  alır 
sonuc = mesaj.split() # karakterleri   boş lukta ayırı ['btk' , 'akademi',  'python' , 'kursu'] liste gönderir
sonuc = mesaj.split()[0] # btk
sonuc = mesaj.split(',') #  virgülerden ayırara 2 liste verir ['btk akademi' , 'python kursu']

sonuc = mesaj.index("akademi") # 4 index  burada akdemi kaçıncı index de başlıyor 
sonuc = mesaj.startswith("b")  #karakter dizisi 'b' ile mi başlıyor True
sonuc = mesaj.startswith("a")#karakter dizisi 'a' ile mi başlıyor false
sonuc  = mesaj.endswith("u") #karakter dizisi 'u' ile mi bitiyor True

sonuc = mesaj.replace("python" , "javascript") # pythonu bulur bunu yerine Javascripti ekler 
# cıktı : 'btk Akademi javascript kursu' olarak cıktı gelir 
print(sonuc)