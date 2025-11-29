class BankAccount:
    def __init__(self, owner): # Hesap sahibini ve başlangıç bakiyesini ayarla
        self.owner = owner
        self.balance = 0 
        self.yatirilan_toplam = 0
        self.cekilen_toplam = 0

# Para yatırma işlemi   
    def depozit(self, miktar):
        if miktar <= 0:
            print("yairalacak miktar pozitif olmalidir.")
            return      
        

# Bakiyeye para ekle
        self.balance += miktar
        self.yatirilan_toplam += miktar
        print(f"{miktar} dolar yatirildi. Bakiye: {self.balance}")


# Para çekme işlemi (yetersiz bakiye kontrolü)   
    def withdraw(self, miktar):
        if miktar <= 0:
            print("ceckilecek para 0 dan bütük olmalidir")
            return
           

# Yetersiz bakiye kontrolü
        if miktar > self.balance:
            print(f"yetersz bakiye mevcut baliye : {self.balance} $")
            return   
        

# Bakiyeden para çıkar
        self.balance -= miktar
        self.cekilen_toplam += miktar
        print(f"{miktar}dolar cekildi. bakiye: {self.balance} $ ")



# Dosya oluştur ve bilgileri yaz
    def kaydet(self):
        with open("hesap_bilgisi.txt", "a", encoding="utf-8")as dosya:
            dosya.write(f"Hesap bilgisi: {self.owner}\n")
            dosya.write(f"Toplam yatirim: {self.yatirilan_toplam}$\n")
            dosya.write(f"Toplam cekim: {self.cekilen_toplam}$\n")
            dosya.write(f"Güncel Bakiye: {self.balance}$\n")
            dosya.write("-" * 30 + "\n")
        print("Hesap bilgileri Kaydedildi.")


 # Hesap bilgilerini string olarak döndür   
    def __str__(self):
        return f"Hesap sahibi: {self.owner}- bakiye: {self.balance}$ "


isim = input("Adinizi giriniz: ")# Kullanıcıdan isim al
print(f"SN.{isim} Bankamiza Hoş Geldiniz.Lütfen Yatirmak İstediğiniz Tutari Giriniz.") 

# işlem döngüsü
while True:
    account = BankAccount(isim)# Hesap oluştur
    account.depozit(int(input("yatiralacak tutar: ")))
    account.withdraw(int(input("cekilecek tutar: ")))
    print(f"\n{account}")# Hesap durumunu göster



    # cls yazmazsa döngüden çık ve bilgileri kaydet
    devam = input("\n başka işlem yapmak istermsiniz(cls/exit): ")
    if devam != "cls":
        account.kaydet() # Dosyaya kaydet
        print("Bankamizi terccih ettiginiz için teşekkür ederiz. iyi günler  dileriz ")
        break # Döngüden çık