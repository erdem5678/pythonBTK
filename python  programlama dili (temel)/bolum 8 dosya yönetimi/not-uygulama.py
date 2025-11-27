# Not uyguluması


# 1 menu
    # 1- Not ekle
    # 2- ortalmaları göster(90-100 -> AA,8589 ->BA)      
    # 3- notları kayıt et
    # 4- çıkış

def not_hespla(satir):
    satir = satir.strip()
    liste = satir.split(":")
    
    ogreciAdi = liste[0]
    notlar = liste[1].split(",")
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ortalama = (not1 + not2 + not3) / 3

    if 90 >= ortalama <= 100:
        harf = "AA"
    elif 80 >=  ortalama <= 89:
        harf = "BA"
    elif 75 >= ortalama <= 79:
        harf = "BB"
    elif 70 >=  ortalama <= 74:
        harf = "CB"
    elif 65 >= ortalama <= 69:
        harf = "CC"
    elif 60>= ortalama <= 64:
        harf = "DC"
    elif 50 >= ortalama <= 59:
        harf = "DD"
    elif 40 >=  ortalama <= 49:
        harf = "FD"
    elif 0 >= ortalama <= 39:
        harf = "FF"

    return f"{ogreciAdi} : {harf}-({ortalama})\n"

def not_gir():
    ad = input("Öğrenci adi: ")
    soyad = input("Öğrenci soyad: ")
    not1 = input("Not1: ")
    not2 = input("Not2: ")
    not3 = input("Not3: ")

    with open("notlar.txt", "a", encoding="utf-8") as file:  # 'a' = ekleme modu
        file.write(ad + ' ' + soyad + ':' + not1 + ',' + not2 + ',' + not3 + '\n')

def notlari_oku():
        with open("notlar.txt", "r", encoding="utf-8") as file:
            for satir in file:
                print(not_hespla(satir))

def notlari_kaydet():
        liste = []
        with open("notlar.txt", "r", encoding="utf-8") as file:
            for satir in file:
                liste.append(not_hespla(satir) + '\n')

        with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            file2.writelines(liste)

# Ana döngü
while True:
    islem = input("1- Not gir\n2- Notlari oku\n3- Notlari kaydet\n4- Çikiş\nSeçim: ")

    if islem == "1":
        not_gir()
    elif islem == "2":
        notlari_oku()
    elif islem == "3":
        notlari_kaydet()
    elif islem == "4":
            break