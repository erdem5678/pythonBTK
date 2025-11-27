def not_ekle():
    not_metni = input("Notunuzu girin: ")
    with open("notlar.txt", "a", encoding="utf-8") as f:
        f.write(f"{not_metni}\n")
    print("✓ Not eklendi!")

def notlari_göster():
    try:
        with open("notlar.txt", "r", encoding="utf-8") as f:
            notlar = f.readlines()
            for i, not_metni in enumerate(notlar, 1):
                print(f"{i}. {not_metni.strip()}")
    except FileNotFoundError:
        print("Henüz not yok!")

while True:
    print("\n1. Not ekle  2. Notlari göster  3. Çıikiş")
    seçim = input("Seçim: ")
    if seçim == "1":
        not_ekle()
    elif seçim == "2":
        notlari_göster()
    elif seçim == "3":
        break

    print("---- örnek cikti ---\n")
    def öğrenci_ekle():
     ad = input("Ad: ")
     soyad = input("Soyad: ")
     numara = input("Numara: ")
    
     with open("öğrenciler.txt", "a", encoding="utf-8") as f:
        f.write(f"{numara}|{ad}|{soyad}\n")
     print("✓ Öğrenci kaydedildi!")

def öğrenci_ara():
    aranan = input("Aranacak numara: ")
    
    with open("öğrenciler.txt", "r", encoding="utf-8") as f:
        for satır in f:
            numara, ad, soyad = satır.strip().split("|")
            if numara == aranan:
                print(f"Bulundu: {ad} {soyad} ({numara})")
                return
            
    print("Öğrenci bulunamadı!")
print("---- klasör organizsasyon----\n")
import os
import shutil

def dosyaları_organize_et():
    # Uzantıya göre klasörlere ayır
    uzantılar = {
        "Resimler": [".jpg", ".png", ".gif", ".jpeg"],
        "Belgeler": [".pdf", ".docx", ".txt", ".xlsx"],
        "Videolar": [".mp4", ".avi", ".mkv"],
        "Müzik": [".mp3", ".wav", ".flac"]
    }
    
    # Klasörleri oluştur
    for klasör in uzantılar.keys():
        if not os.path.exists(klasör):
            os.mkdir(klasör)
    
    # Dosyaları taşı
    for dosya in os.listdir("."):
        if os.path.isfile(dosya):
            _, uzantı = os.path.splitext(dosya)
            
            for klasör, uzantı_listesi in uzantılar.items():
                if uzantı.lower() in uzantı_listesi:
                    hedef = os.path.join(klasör, dosya)
                    shutil.move(dosya, hedef)
                    print(f"✓ {dosya} → {klasör}/")
                    break

dosyaları_organize_et()


print("---- klasör raporu----\n")
import os

def klasör_raporu(yol="."):
    toplam_dosya = 0
    toplam_boyut = 0
    dosya_tipleri = {}
    
    print(f"\n📁 Klasör: {os.path.abspath(yol)}\n")
    
    for dosya in os.listdir(yol):
        tam_yol = os.path.join(yol, dosya)
        
        if os.path.isfile(tam_yol):
            toplam_dosya += 1
            boyut = os.path.getsize(tam_yol)
            toplam_boyut += boyut
            
            _, uzantı = os.path.splitext(dosya)
            uzantı = uzantı.lower() or "uzantısız"
            
            if uzantı in dosya_tipleri:
                dosya_tipleri[uzantı] += 1
            else:
                dosya_tipleri[uzantı] = 1
            
            print(f"  📄 {dosya} ({boyut} byte)")
    
    print(f"\n--- ÖZET ---")
    print(f"Toplam dosya: {toplam_dosya}")
    print(f"Toplam boyut: {toplam_boyut / 1024:.2f} KB")
    print(f"\nDosya tipleri:")
    for uzantı, adet in dosya_tipleri.items():
        print(f"  {uzantı}: {adet} adet")

klasör_raporu()
print("---- klasör yedek----\n")
import os
import shutil
from datetime import datetime

def dosya_yedekle(kaynak_dosya):
    if not os.path.exists(kaynak_dosya):
        print("❌ Dosya bulunamadı!")
        return
    
    # Yedek klasörü oluştur
    if not os.path.exists("Yedekler"):
        os.mkdir("Yedekler")
    
    # Tarih damgalı dosya adı
    zaman = datetime.now().strftime("%Y%m%d_%H%M%S")
    dosya_adı = os.path.basename(kaynak_dosya)
    ad, uzantı = os.path.splitext(dosya_adı)
    yedek_adı = f"{ad}_yedek_{zaman}{uzantı}"
    
    # Kopyala
    hedef = os.path.join("Yedekler", yedek_adı)
    shutil.copy2(kaynak_dosya, hedef)
    
    print(f"✓ Yedeklendi: {yedek_adı}")

# Kullanım
dosya_yedekle("önemli_dosya.txt")

print("---- işletim sistemi----\n")
import os

# İşletim sistemi adı
print(os.name)  # 'nt' (Windows), 'posix' (Linux/Mac)

# Ortam değişkenleri
print(os.environ.get("USERNAME"))  # Kullanıcı adı
print(os.environ.get("PATH"))  # Sistem PATH'i

# Komut çalıştır
os.system("dir")  # Windows
os.system("ls")   # Linux/Mac

import os

# Kriptografik güvenli rastgele bytes
os.urandom(16)  # 16 byte rastgele veri

import os
import time

# Bekle
time.sleep(2)  # 2 saniye bekle

# Zaman bilgisi
os.times()  # CPU zamanları
print("--- API KEY OLUSTURMA---\n")

import os
import secrets  # Python 3.6+ için daha kolay

def api_key_oluştur():
    """API anahtarı oluştur"""
    # os.urandom ile
    key1 = os.urandom(32).hex()
    
    # secrets ile (önerilir)
    key2 = secrets.token_hex(32)
    
    return key1, key2

key1, key2 = api_key_oluştur()
print(f"API Key 1: {key1}")
print(f"API Key 2: {key2}")