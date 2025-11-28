def not_ekle():  # Not ekleme fonksiyonu
    not_metni = input("Notunuzu girin: ")  # Kullanıcıdan not al
    with open("notlar.txt", "a", encoding="utf-8") as f:  # Dosyayı ekleme modunda aç (a = append)
        f.write(f"{not_metni}\n")  # Notu dosyaya yaz ve satır atla
    print("✓ Not eklendi!")  # Başarı mesajı göster

def notlari_göster():  # Tüm notları gösterme fonksiyonu
    try:  # Hata yakalama bloğu başlat
        with open("notlar.txt", "r", encoding="utf-8") as f:  # Dosyayı okuma modunda aç (r = read)
            notlar = f.readlines()  # Tüm satırları liste olarak oku
            for i, not_metni in enumerate(notlar, 1):  # Her satırı numaralandırarak döngüye sok (1'den başla)
                print(f"{i}. {not_metni.strip()}")  # Numaralı notu yazdır (strip ile boşlukları temizle)
    except FileNotFoundError:  # Eğer dosya bulunamazsa
        print("Henüz not yok!")  # Hata mesajı göster

while True:  # Sonsuz döngü başlat
    print("\n1. Not ekle  2. Notlari göster  3. Çıikiş")  # Menüyü göster
    seçim = input("Seçim: ")  # Kullanıcıdan seçim al
    if seçim == "1":  # Eğer 1 seçildiyse
        not_ekle()  # Not ekleme fonksiyonunu çağır
    elif seçim == "2":  # Eğer 2 seçildiyse
        notlari_göster()  # Notları gösterme fonksiyonunu çağır
    elif seçim == "3":  # Eğer 3 seçildiyse
        break  # Döngüden çık (programı bitir)

    print("---- örnek cikti ---\n")  # Bölüm ayırıcı yazdır
    def öğrenci_ekle():  # Öğrenci ekleme fonksiyonu
     ad = input("Ad: ")  # Öğrenci adını al
     soyad = input("Soyad: ")  # Öğrenci soyadını al
     numara = input("Numara: ")  # Öğrenci numarasını al
    
     with open("öğrenciler.txt", "a", encoding="utf-8") as f:  # Dosyayı ekleme modunda aç
        f.write(f"{numara}|{ad}|{soyad}\n")  # Öğrenci bilgilerini | ile ayırarak yaz
     print("✓ Öğrenci kaydedildi!")  # Başarı mesajı

def öğrenci_ara():  # Öğrenci arama fonksiyonu
    aranan = input("Aranacak numara: ")  # Aranacak numarayı al
    
    with open("öğrenciler.txt", "r", encoding="utf-8") as f:  # Dosyayı okuma modunda aç
        for satır in f:  # Her satırı döngüyle oku
            numara, ad, soyad = satır.strip().split("|")  # Satırı | işaretinden böl ve değişkenlere ata
            if numara == aranan:  # Eğer numara eşleşirse
                print(f"Bulundu: {ad} {soyad} ({numara})")  # Öğrenci bilgisini göster
                return  # Fonksiyondan çık
            
    print("Öğrenci bulunamadı!")  # Hiç eşleşme yoksa mesaj göster
print("---- klasör organizsasyon----\n")  # Bölüm ayırıcı
import os  # İşletim sistemi işlemleri için modül
import shutil  # Dosya taşıma/kopyalama için modül

def dosyaları_organize_et():  # Dosyaları organize etme fonksiyonu
    # Uzantıya göre klasörlere ayır
    uzantılar = {  # Dosya uzantıları ve hedef klasörler sözlüğü
        "Resimler": [".jpg", ".png", ".gif", ".jpeg"],  # Resim formatları
        "Belgeler": [".pdf", ".docx", ".txt", ".xlsx"],  # Belge formatları
        "Videolar": [".mp4", ".avi", ".mkv"],  # Video formatları
        "Müzik": [".mp3", ".wav", ".flac"]  # Müzik formatları
    }
    
    # Klasörleri oluştur
    for klasör in uzantılar.keys():  # Her klasör adı için döngü
        if not os.path.exists(klasör):  # Eğer klasör yoksa
            os.mkdir(klasör)  # Klasörü oluştur
    
    # Dosyaları taşı
    for dosya in os.listdir("."):  # Şu anki dizindeki tüm dosyaları listele
        if os.path.isfile(dosya):  # Eğer dosyaysa (klasör değilse)
            _, uzantı = os.path.splitext(dosya)  # Dosya adını ve uzantısını ayır
            
            for klasör, uzantı_listesi in uzantılar.items():  # Her klasör ve uzantı listesi için
                if uzantı.lower() in uzantı_listesi:  # Eğer uzantı listede varsa
                    hedef = os.path.join(klasör, dosya)  # Hedef yolu oluştur
                    shutil.move(dosya, hedef)  # Dosyayı taşı
                    print(f"✓ {dosya} → {klasör}/")  # Taşıma bilgisini göster
                    break  # Bu dosya için döngüden çık

dosyaları_organize_et()  # Fonksiyonu çalıştır


print("---- klasör raporu----\n")  # Bölüm ayırıcı
import os  # İşletim sistemi modülü

def klasör_raporu(yol="."):  # Klasör raporu oluşturma fonksiyonu (varsayılan: şu anki dizin)
    toplam_dosya = 0  # Dosya sayacı
    toplam_boyut = 0  # Toplam boyut sayacı
    dosya_tipleri = {}  # Dosya tipi sayıları için sözlük
    
    print(f"\n📁 Klasör: {os.path.abspath(yol)}\n")  # Tam yolu göster
    
    for dosya in os.listdir(yol):  # Klasördeki her öğe için
        tam_yol = os.path.join(yol, dosya)  # Tam yolu oluştur
        
        if os.path.isfile(tam_yol):  # Eğer dosyaysa
            toplam_dosya += 1  # Dosya sayısını artır
            boyut = os.path.getsize(tam_yol)  # Dosya boyutunu al (byte)
            toplam_boyut += boyut  # Toplam boyuta ekle
            
            _, uzantı = os.path.splitext(dosya)  # Uzantıyı ayır
            uzantı = uzantı.lower() or "uzantısız"  # Küçük harfe çevir, yoksa "uzantısız" yaz
            
            if uzantı in dosya_tipleri:  # Eğer bu uzantı daha önce görüldüyse
                dosya_tipleri[uzantı] += 1  # Sayısını artır
            else:  # Görülmediyse
                dosya_tipleri[uzantı] = 1  # İlk kez ekle
            
            print(f"  📄 {dosya} ({boyut} byte)")  # Dosya adı ve boyutunu göster
    
    print(f"\n--- ÖZET ---")  # Özet bölümü başlat
    print(f"Toplam dosya: {toplam_dosya}")  # Toplam dosya sayısı
    print(f"Toplam boyut: {toplam_boyut / 1024:.2f} KB")  # Toplam boyut KB cinsinden
    print(f"\nDosya tipleri:")  # Dosya tipleri başlığı
    for uzantı, adet in dosya_tipleri.items():  # Her uzantı ve adeti için
        print(f"  {uzantı}: {adet} adet")  # Uzantı ve adetini yazdır

klasör_raporu()  # Fonksiyonu çalıştır
print("---- klasör yedek----\n")  # Bölüm ayırıcı
import os  # İşletim sistemi modülü
import shutil  # Dosya kopyalama modülü
from datetime import datetime  # Tarih/saat işlemleri için

def dosya_yedekle(kaynak_dosya):  # Dosya yedekleme fonksiyonu
    if not os.path.exists(kaynak_dosya):  # Eğer dosya yoksa
        print("❌ Dosya bulunamadı!")  # Hata mesajı
        return  # Fonksiyondan çık
    
    # Yedek klasörü oluştur
    if not os.path.exists("Yedekler"):  # Eğer Yedekler klasörü yoksa
        os.mkdir("Yedekler")  # Klasörü oluştur
    
    # Tarih damgalı dosya adı
    zaman = datetime.now().strftime("%Y%m%d_%H%M%S")  # Şu anki zamanı formatla (20241129_153045 gibi)
    dosya_adı = os.path.basename(kaynak_dosya)  # Sadece dosya adını al (yol olmadan)
    ad, uzantı = os.path.splitext(dosya_adı)  # Dosya adı ve uzantısını ayır
    yedek_adı = f"{ad}_yedek_{zaman}{uzantı}"  # Yeni dosya adı oluştur
    
    # Kopyala
    hedef = os.path.join("Yedekler", yedek_adı)  # Hedef yolunu oluştur
    shutil.copy2(kaynak_dosya, hedef)  # Dosyayı kopyala (metadata ile birlikte)
    
    print(f"✓ Yedeklendi: {yedek_adı}")  # Başarı mesajı

# Kullanım
dosya_yedekle("önemli_dosya.txt")  # Örnek dosyayı yedekle

print("---- işletim sistemi----\n")  # Bölüm ayırıcı
import os  # İşletim sistemi modülü

# İşletim sistemi adı
print(os.name)  # 'nt' (Windows), 'posix' (Linux/Mac) yazdırır

# Ortam değişkenleri
print(os.environ.get("USERNAME"))  # Kullanıcı adını al ve yazdır
print(os.environ.get("PATH"))  # Sistem PATH değişkenini al ve yazdır

# Komut çalıştır
os.system("dir")  # Windows'ta dizin listele
os.system("ls")   # Linux/Mac'te dizin listele

import os  # İşletim sistemi modülü (tekrar import)

# Kriptografik güvenli rastgele bytes
os.urandom(16)  # 16 byte rastgele veri oluştur (güvenli)

import os  # İşletim sistemi modülü (tekrar import)
import time  # Zaman işlemleri için modül

# Bekle
time.sleep(2)  # 2 saniye bekle (programı duraklat)

# Zaman bilgisi
os.times()  # CPU zamanlarını döndür (sistem, kullanıcı zamanı vb.)
print("--- API KEY OLUSTURMA---\n")  # Bölüm ayırıcı

import os  # İşletim sistemi modülü
import secrets  # Python 3.6+ için güvenli rastgele sayı üretimi

def api_key_oluştur():  # API anahtarı oluşturma fonksiyonu
    """API anahtarı oluştur"""  # Fonksiyon açıklaması (docstring)
    # os.urandom ile
    key1 = os.urandom(32).hex()  # 32 byte rastgele veri oluştur ve hex'e çevir
    
    # secrets ile (önerilir)
    key2 = secrets.token_hex(32)  # 32 byte hex token oluştur (daha güvenli)
    
    return key1, key2  # İki anahtarı da döndür

key1, key2 = api_key_oluştur()  # Fonksiyonu çağır ve anahtarları al
print(f"API Key 1: {key1}")  # İlk anahtarı yazdır
print(f"API Key 2: {key2}")  # İkinci anahtarı yazdır