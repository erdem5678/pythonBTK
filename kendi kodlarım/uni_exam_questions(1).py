# # ÜNİVERSİTE SINAVI - PYTHON SORULARI (SADECE ÇIKTILAR)

# ## SORU 1: Liste İşlemleri
# **Görev:** 1'den 20'ye kadar olan sayılardan çift olanları bir listeye ekleyin ve yazdırın.
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
sayilar = []
for sayi in range(1, 21):
    if sayi % 2 == 0:
        sayilar.append(sayi)
print(sayilar)

# ## SORU 2: String İşlemleri
# **Görev:** "python programlama" metnindeki her kelimenin ilk harfini büyük yapın.
# **Beklenen Çıktı:**
# Python Programlama

metin = "python programlama"
sonuc = metin.title()
print(sonuc)

print("---soru 2---\n")

# ## SORU 3: Sözlük Kullanımı
# **Görev:** Aşağıdaki öğrenci notlarının ortalamasını hesaplayın.
# - Ali: 85, 90, 78
# - Ayşe: 92, 88, 95
# **Beklenen Çıktı:**
# Ali: 84.33
# Ayşe: 91.67
ogrenciler = {
    "Ali": [85, 90, 78],
    "Ayşe": [92, 88, 95]
}
for isim, notlar in ogrenciler.items():
    ortalama = sum(notlar) / len(notlar)
    print(f"{isim} nin ortalamasi:{ortalama:.2f}")

print("---soru 3---\n")

# ## SORU 4: For Döngüsü
# **Görev:** 1'den 10'a kadar olan sayıların toplamını bulun.
# **Beklenen Çıktı:**
# Toplam: 55

toplam = sum(range(1,11))
print(f"1 den 10 kadar sayilarin toplami: {toplam}")

topalam = 0
for i in range(1,11):
    topalam += i 
    print(f"toplam: {topalam}")

print("---soru 4---\n")

# ## SORU 5: If-Elif-Else
# **Görev:** Bir sayı 50'den büyükse "Büyük", 50'ye eşitse "Eşit", küçükse "Küçük" yazdırın. (Sayı = 75)
# **Beklenen Çıktı:**
# Büyük
sayi = 75
if sayi > 50:
    print("büyük")
elif sayi == 50:
    print("eşit")
else:
    print("küçük")

print("---soru 5---\n")


# ## SORU 6: Fonksiyon Yazma
# **Görev:** İki sayının çarpımını döndüren bir fonksiyon yazın. (5 * 8)
# **Beklenen Çıktı:**
# 40
def carpim(sayi1,sayi2):
    return sayi1*sayi2
sayi1 = int(input("sayi gir:"))
sayi2 = int(input("sayi gir:"))
sonuc = carpim(sayi1,sayi2)
print(sonuc)

print("---soru 6---\n")


# ---

# ## SORU 7: Liste Maksimum-Minimum
# **Görev:** [12, 45, 7, 23, 67, 34] listesindeki en büyük ve en küçük sayıyı bulun.

# **Beklenen Çıktı:**
# En büyük: 67
# En küçük: 7
sayilar=[12, 45, 7, 23, 67, 34] 
en_buyuk = max(sayilar)
en_kucuk = min(sayilar)
print(f"en büyük:{en_buyuk}")
print(f"en küçük:{en_kucuk}")

# ---

# ## SORU 8: While Döngüsü
# **Görev:** 1'den başlayarak 2'şer 2'şer artan ve 10'dan küçük olan sayıları yazdırın.
# **Beklenen Çıktı:**
# 1
# 3
# 5
# 7
# 9
while True:
    sayi = 1
    if sayi < 10:
        print(sayi)
        sayi += 2
    else:
        break

## SORU 9: Dosya Yazma
# **Görev:** "test.txt" dosyasına "Merhaba Dünya" yazın ve tekrar okuyun.
# **Beklenen Çıktı:*
# Merhaba Dünya
ekleme = input("ekleme yap:")
dosya = open("test.txt", "a",encoding="utf-8")
dosya.write(ekleme)
dosya.close()

dosya = open("test.txt", "r")
icerik = dosya.read()
print(icerik)

# ---

# ## SORU 10: Try-Except
# **Görev:** Kullanıcıdan sayı isteyin, harf girilirse hata mesajı verin. (Girdi: "abc")
# **Beklenen Çıktı:**
# Hata: Geçerli bir sayı girin!
try:
    sayi = int(input("Bir sayi girin: "))
    print(f"Girdiğiniz sayi: {sayi}")
except ValueError:
    print("Hata: Geçerli bir sayı girin!")


# ---

# ## SORU 11: Liste Ters Çevirme
# **Görev:** [1, 2, 3, 4, 5] listesini ters çevirin.
# **Beklenen Çıktı:**
# [5, 4, 3, 2, 1]
liste = [1, 2, 3, 4, 5]
liste.reverse()
print(liste)

# ---

# ## SORU 12: Faktöriyel Hesaplama
# **Görev:** 5! (faktöriyel) hesaplayın.
# **Beklenen Çıktı:**
# 120
sayi = int(input("faktöriyelini hesaplamak istediğiniz sayiyi girin:"))
sonuc = 1 # faktöriyel başlangıç değeri
for i in range(1, sayi+ 1):
    sonuc *=i
print(f"{sayi}! sonuc: {sonuc}")



# ---

# ## SORU 13: Çift/Tek Ayırma
# **Görev:** [1, 2, 3, 4, 5, 6, 7, 8] listesindeki çift ve tek sayıları ayırın.
# **Beklenen Çıktı:**
# Çift: [2, 4, 6, 8]
# Tek: [1, 3, 5, 7]

lambdasayi_listesi = [1, 2, 3, 4, 5, 6, 7, 8]

cift_sayilar = [list(filter(lambda x: x % 2 == 0, lambdasayi_listesi))] # çift sayıları filtreleme
tek_sayilar = [list(filter(lambda x: x % 2 != 0, lambdasayi_listesi))] # tek sayıları filtreleme

print(f"Çift: {cift_sayilar}")
print(f"Tek: {tek_sayilar}")

# ## SORU 14: String Uzunluğu
# **Görev:** "Üniversite" kelimesindeki karakter sayısını bulun.
# **Beklenen Çıktı:**
# 10
kelime = "Üniversite"
print(len(kelime))

# ---

# ## SORU 15: Asal Sayı Kontrolü
# **Görev:** 17 sayısının asal olup olmadığını kontrol edin.
# **Beklenen Çıktı:**
# 17 asal bir sayıdır

sayi = int (input("Asal sayi giriniz : "))
asl_mi = True

for i in range (sayi):
    if i>1 and (sayi % i) ==0: # sayi asal değildir
        asl_mi = False
        break
    
if asl_mi:
    print(f"{sayi} asal bir sayıdır")
else:
    print(f"{sayi} asal bir sayı değildir")


# ---

# ## SORU 16: Tuple (Demet) İşlemleri
# **Görev:** (10, 20, 30, 40) tuple'ının elemanlarını toplayın.
# **Beklenen Çıktı:**
# Toplam: 100
tuple_degerleri = (10, 20, 30, 40)
toplam = sum(tuple_degerleri)
print(f"Toplam: {toplam}")

# ---

# ## SORU 17: Mod Operatörü
# **Görev:** 17'nin 5'e bölümünden kalanı bulun.
# **Beklenen Çıktı:**
# 2
kalan = 17 % 5
print(f"kalan: {kalan}")
# ---

# ## SORU 18: Liste Elemanı Sayma
# **Görev:** [1, 2, 2, 3, 2, 4, 2, 5] listesinde 2 sayısı kaç kez geçiyor?
# **Beklenen Çıktı:**
# 4
liste = [1, 2, 2, 3, 2, 4, 2, 5]
sayi = int(input("liste içinde ssayilar: "))
adet = liste.count(sayi) # sayi adedini sayma
print(f"{sayi} sayısı liste içinde {adet} kez geçiyor.")
# ---

# ## SORU 19: Random Modülü
# **Görev:** 1 ile 100 arasında rastgele bir sayı üretin. (Örnek çıktı)
# **Beklenen Çıktı:**
# 42
import random
rasgele_sayi = random.randint(1,100)
print(f"üretilen sayi:{rasgele_sayi}")



# ---

# ## SORU 20: Sözlük Anahtarları
# **Görev:** {"isim": "Ali", "yas": 20, "sehir": "İstanbul"} sözlüğünün anahtarlarını listeleyin.
# **Beklenen Çıktı:**
# ['isim', 'yas', 'sehir']
sozluk = {"isim": "Ali", "yas": 20, "sehir": "İstanbul"}
anahtarlar = list(sozluk.keys())
print(anahtarlar)
# ---

# ## SORU 21: List Comprehension
# **Görev:** 1'den 10'a kadar olan sayıların karelerini list comprehension ile oluşturun.
# **Beklenen Çıktı:**
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
kareler= [x**2 for x in range(1,11)]
print(f"sayilarin kareleri:{kareler}")
# ---

# ## SORU 22: String Değiştirme
# **Görev:** "Python çok zor" cümlesindeki "zor" kelimesini "kolay" ile değiştirin.
# **Beklenen Çıktı:**
# Python çok kolay
metin = "Python çok zor"
yeni_metin = metin.replace("zor","kolay") # kelime değiştirme
print(f"yeni metin:{yeni_metin}")

# ---

# ## SORU 23: Range Kullanımı
# **Görev:** 5'ten 15'e kadar (15 dahil) olan sayıları yazdırın.
# **Beklenen Çıktı:**
# 5 6 7 8 9 10 11 12 13 14 15
for sayi in range(5,16):
    print(sayi,end=" ")

# ---

# ## SORU 24: Lambda Fonksiyonu
# **Görev:** Lambda ile bir sayının 3 katını bulan fonksiyon yazın ve 7 için çalıştırın.
# **Beklenen Çıktı:**
# 21
uc_kati=(lambda x : x * 3) # lambda fonksiyonu tanımlama
print(uc_kati(7))

# ---

# ## SORU 25: JSON Veri Yazma
# **Görev:** {"ad": "Mehmet", "not": 85} verisini "ogrenci.json" dosyasına kaydedin ve okuyun.
# **Beklenen Çıktı:**
# {'ad': 'Mehmet', 'not': 85}
json_veri = {"ad": "Mehmet", "not": 85}

import json # json modülünü içe aktarm

with open("ogrenci.json", "w") as json_dosya:
    json.dump(json_veri, json_dosya)# json verisini dosyaya yazma

with open("ogrenci.json", "r") as json_dosya:
    okunan_veri = json.load(json_dosya) # json verisini dosyadan okuma
print(okunan_veri)  