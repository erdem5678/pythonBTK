import random 
sayi = random.randint(1, 10)
hak = 3
skor = 0

print("1 ile 10 arasında bir sayı tahmin et. Toplam 3 hakkın var!")

while hak > 0:
    try: # kullanıcı hatası için 
        tahmin = int(input("Tahminin: ")) #kullanıcıdan tahmin al 
    except ValueError:# kullanıcı sayı girmezse
        print("Lütfen bir sayı gir.")# hata mesaj ver
        continue # döngünün başına dön 
    
    if tahmin == sayi:
        skor += 1
        print(f"Tebrikler! Doğru sayıyı buldun. Skorun: {skor}")# sskoru göstyer
        # Yeni sayı seç ve hakları sıfırla
        sayi = random.randint(1, 10)
        hak = 3
        print("\nYeni sayı seçildi, tekrar tahmin et!")# yeni sayı seçildigiini bildir 
    else:
        hak -= 1
        print(f"Yanlış! Kalan hakkın: {hak}")# kalan hakları göster
        if tahmin < sayi:
            print("İpucu: Daha büyük bir sayı dene.")
        else:
            print("İpucu: Daha küçük bir sayı dene.")
        
        if hak == 0:
            print(f"Üzgünüm, hakkın bitti. Skorun: {skor}")
            break # oyun  biter 