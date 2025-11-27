# bankamatik uygulaması,
# hesap bilgilerini tutacak (dict)
# mennu,paracekme,barasorgu,parayatırma fonksiyonları tanımlnacak 
# çekilme istenen tutar hesapta yoksa ek hesap kullnılmak istendigi sorulacak

#(dict) yapısı key value
hesaplar = [
    {
       "ad": "bariş",
       "hesapNo": "12345",
       "bakiye": 3000,
       "ekHesap": 2000,
        "username": "bariserdem",
        "password": "12345",

    },
     {
       "ad": "can",
       "hesapNo": "12345",
       "bakiye": 30000,
       "ekHesap": 20000,
        "username": "canerdem",
        "password": "1234",

    }
]
#menu
def menu(hesap):
    print("\n")
    print(f"merhaba, {hesap["ad"]}")
    print("1- bakiye sorgulama")
    print("2- para cekme")
    print("3- para yatirma")
    print("4- cikis")

    islem = input("yapmak istediginiz islemi seciniz: ")

    if islem == "1":
        bakiyeSorgulama(hesap)
    elif islem == "2":
        paraCekme(hesap)
    elif islem == "3":
        paraYatirma(hesap)
    elif islem == "4":
        cikis(hesap)
    else:
        print("yanliş secim yaptiniz")

    menu(hesap)

#bakiyeSorgulama
def bakiyeSorgulama(hesap):
    print(f"bakiye: {hesap["bakiye"]}")
    print(f"bakiye: {hesap["ekHesap"]}")

#paraCekme
def  paraCekme(hesap):
    miktar = float(input("cekmek istediginiz tutari giriniz: "))
    
    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("paranizi ala bilirsiniz ")
    else:
        toplam = hesap["bakiye"] + hesap["ekhesap"]
        if toplam >= miktar:
            ekHesapKullanimiİzni = input("ek hesap kullanilsin mi (evet/ hayir):  ")

            if ekHesapKullanimiİzni == "evet":
                kullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap ["ekHesap"] -= kullanilacakMiktar
                print("paranizi alabilrisiniz")
            else:
                print("üzgünüz bakiyeniz yetersiz")
        else:
                print("üzgünüz bakiyeniz yetersiz")

#paraYatirma
def  paraYatirma(hesap):
    miktar = float(input("yatimak istediginiz tutari giriniz: "))
    if miktar > 0:
        hesap["bakiye"] += miktar
        print(f"paraniz başari ile yatirimistir. yeni bakiyeniz: {hesap["bakiye"]}TL")
    else:
        print("gecersiz tutar.lütfen pozitif bir deger giriniz.")

 #cikis
def cikis(hesap):
    print(f"Hesabinizdan çikş yapiliyor, {hesap['ad']}. İyi günler dileriz.")
    return True # Menü fonksiyonuna çıkış yapılması gerektiğini bildirir

#login
def login():
    username = input("username: ")
    password = input("password: ")

    isLoggedIn = False

    for  hesap in hesaplar:
        if hesap["username"] == username and hesap["password"] == password:
            isLoggedIn = True
            menu(hesap)
            break

    if not(isLoggedIn):
        print("username yada parola yanliş")
login()