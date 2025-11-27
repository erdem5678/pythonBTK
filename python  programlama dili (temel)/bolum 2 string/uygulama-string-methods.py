kursAdi ="Btk Akademi Python ile Programlama Dersleri çalışmaları"
website = "https://www.btkadademi.gov.tr/"

# 1 - 'Btk Akademi' karkater dizisinin baş  ve sonraki boşluk karakterlerini siliniz 
sonuc = ' Btk Akademi '.strip()
# 2 - kursAdi degişkenindeki tük karakterleri küçük harfe cevir
sonuc = kursAdi.lower()
# 3 - website degişkeninde kaç tane '.' karakteri vardır 
sonuc = website.count('.')
# 4- website değişkeni 'https' ile mi başlıyor?
sonuc = website.startswith('https')
# 5- website 'tr' ile mi bitiyor?
sonuc  = website.endswith("tr")
# 6- kursAdi içerisindeki tüm karakterler harflerden mi oluşuyor?
sonuc = kursAdi.isalpha() # kuras adı  harflerden mi oluşuyo mu  diye sorar True döner

# 7- kursAdi değişkenindeki tüm boşlukları '-' ile değiştiriniz.
sonuc = kursAdi.replace(' ' , '-').replace('ç', 'c').replace('ı', 'i').replace('ş', 's').lower()
# 8- kursAdi değişkenindeki Python kelimesini ReactJs ile değiştiriniz.
sonuc =kursAdi.replace('Python','Reactjs')

# 9- website değişkeni 'www' içeriyor mu?
sonuc = website.find('www') #'aaa'  arandıgnda buluna masa '-1 'cıktısı verir
sonuc = website.index('www')#'aaa'  arandıgnda buluna masa  ValueError hattası verir'aaa' 
# 10- kursAdi değişkenini listeye çeviriniz.
sonuc = kursAdi.split(' ')
print(sonuc[3])
print(sonuc)