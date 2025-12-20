# #Hesap Sahibi: Ahmet, Güncel Bakiye: 1500 AZN

print("\n************Hesap Sahibi: Ahmet, Güncel Bakiye: 1500 AZN**************\n")
class BankAccount:
    def __init__(self, account_holder, initial_balance=0): 
        self.account_holder = account_holder
        self.balance = initial_balance          


# başlangıç bakiyesi negatifse 0 yap
        if initial_balance < 0:
            print("Başlangiç bakiyesi negatif olamaz. Bakiye 0 olarak ayarlandi.")
            self.balance = 0
        else:
            self.balance = initial_balance
            print(f"Hesap oluşturuldu. Hesap Sahibi: {self.account_holder}, Başlangıç Bakiyesi: {self.balance} Dolar")



# depozite fonksiyonu
    def depozito(self, amount):
        if amount <= 0:  # Eğer miktar 0 veya daha küçükse (eksi ise)
            print(f"Hata: {amount} geçersiz bir miktardır! Lütfen pozitif bir sayı girin.")
            return  # İşlemi sonlandır
        else:  # Miktar 0'dan büyükse (pozitifse)
            self.balance += amount
            print(f"{amount} Dolar yatırıldı. Güncel bakiye: {self.balance} Dolar")
    


# çekme fonksiyonu
    def cekme(self,amount): #Withdraw money
        if amount <= 0:
            print("Hata: Geçersiz cekme miktar! Lütfen pozitif bir sayı girin.")
            return
        
        elif 0 < amount <= self.balance: # çekilecek miktar bakiyeden küçük veya eşit olmalı
            self.balance -= amount # bakiyeden çıkar
            print(f"{amount} Dolar çekildi.")
            print("iyi günler diileriz.....")
        else:
            print("Yetersiz bakiye veya geçersiz miktar.")

# bakiye sorgulama fonksiyonu
    def bakiye_sorgula(self):
        return f"Hesap Sahibi: {self.account_holder}, Güncel Bakiye: {self.balance} Dolar"
    


# Kullanıcıdan bilgi alma  
hesap = input("Hesap Sahibi Adi: ")
bakiye = int(input("Bakiye: "))
para_cekme = int(input("Çekmek İstediğiniz Miktar: "))


hesap = BankAccount(hesap, bakiye)
hesap.cekme(para_cekme)
print(hesap.bakiye_sorgula())






print("\n************Miras Alma (Inheritance**************\n")
#Kullanıcı Adı: ali_admin, Yetki Seviyesi: Tam Yetki
class user:
        def __init__(self,kullanici_adi:str):
            self.kullanici_adi = kullanici_adi

        def bilgi_goster(self):
            print(f"kullanicci adi: {self.kullanici_adi}")

class Admin(user):
    def __init__(self,kullanici_adi:str,sistem_yetkisi:str):
        super().__init__(kullanici_adi) # 
        self.sistem_yetkisi = sistem_yetkisi


    def bilgi_goster(self):
        super().bilgi_goster()# Kullanıcı sınıfındaki bilgi_goster metodunu çağırır
        print(f"sistem yetkisi: {self.sistem_yetkisi}")

isim = input("Admin kullanıcı adını giriniz: ")
yetki = input("Yetki seviyesini giriniz: ")

admin_nesnesi = Admin(isim, yetki)
admin_nesnesi.bilgi_goster()






print("\n************#Metod Kullanimi ve Hesaplama (Geometri)**************\n")
class Geometri:
     def __init__(self,genişlik,uzunluk):
        self.genişlik = genişlik
        self.uzunluk = uzunluk


# Alan hesaplama 
     def alan_hesapla(self):
        return self.genişlik * self.uzunluk
     

#cevre hesaplama
     def cevre_hesapla(self):
        return 2 * (self.genişlik + self.uzunluk)   
     

# kullancı girişi
alan = int(input("Alan giriniz:"))
cevre = int(input("Cevre giriniz:"))

## Nesnemizi oluşturuyoruz
sekil = Geometri(alan, cevre)

# Sonuçları ekrana yazdırıyoruz
print(f"Alan: {sekil.alan_hesapla()}")
print(f"Cevre: {sekil.cevre_hesapla()}")







print("\n************#Liste ve Class İlişkisi (Öğrenci Kayıt)**************\n")
class Ogrenci:
    def __init__(self, isim, not_ortalamasi):
        self.isim = isim
        self.not_ortalamasi = not_ortalamasi

# 1. Boş bir liste oluşturuyoruz
ogrenci_listesi = []

# 2. 3 adet öğrenci nesnesi oluşturup listeye ekliyoruz
# (Burada manuel ekliyoruz, istersen döngüyle input da alabilirsin)
ogrenci_listesi.append(Ogrenci("Leyla", 95))
ogrenci_listesi.append(Ogrenci("Murad", 82))
ogrenci_listesi.append(Ogrenci("Elvin", 78))


isimler = []
for ogrenci in ogrenci_listesi:
    isimler.append(ogrenci.isim)

# İsimleri aralarına virgül koyarak yazdıralım
print("Kayitli Öğrenciler:", end=" ") # 
print(", ".join(isimler))






print("\n************#Kapsülleme (Encapsulation)**************\n")
class Bilgisayar:
    def __init__(self,marka,fiyat):
        self.marka = marka
        self.__fiyat = fiyat #Değişkenin başına __ koyarak onu "Private" (Gizli) hale getiriyoruz



    def fiyat_goster(self):
        ## Gizli değişkene sadece sınıfın içindeki bu metodla erişebiliriz
        return f"{self.__fiyat} $"
    

# Gizli değişkeni dışarıdan değil, kontrollü bir şekilde içeriden değiştiriyoruz
    def fiyat_guncelle(self,yeni_fiyat):
        if yeni_fiyat > 0:  # Negatif fiyat girilmesini engelleyen güvenlik kontrolü
            self.__fiyat = yeni_fiyat
        else:
            print("hatta: Gecersiz fiyat!")


laptop = Bilgisayar("Asus",2500)
print(f"Marka: {laptop.marka}")
print(f"Bilgisayarın gizli fiyatı: {laptop.fiyat_goster()}")

fiyat =int (input("fiyat giriniz: ")) 
laptop.fiyat_guncelle(fiyat)
print(f"Güncellenmiş fiyat: {laptop.fiyat_goster()}")
# print(laptop.__fiyat) #AttributeError: 'Bilgisayar' object has no attribute '__fiyat'
# DİKKAT: print(laptop.__fiyat) yazarsan Python "AttributeError" hatası verir.
# Çünkü __fiyat artık dışarıdan görünmez.







        

        
     