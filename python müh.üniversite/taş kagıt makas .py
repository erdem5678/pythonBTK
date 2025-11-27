import random
secenekler = ["taş", "kağit", "makas"]# seçenekleri tanımla
kullanici_skor = 0
bilgisayar_skor = 0
while kullanici_skor < 4 and bilgisayar_skor < 4:# skor 3 olana kadar devam et
     kullanici_secim = input("taş, kağit veya makas seçiniz: ").lower()# kullanıcıdan seçim al
     bilgisayar_secim = random.choice(secenekler)# bilgisayarın rastgele seçimi
     print(f"senin seçimin: {kullanici_secim}")# kullanıcı seçimini yazdır
     print(f"bilgisayarin seçimi: {bilgisayar_secim}")# bilgisayar seçimini yazdır
     if kullanici_secim not in secenekler:# geçersiz seçim kontrolü
         print("geçersiz seçim, lütfen tekrar deneyin.")
         continue
     if kullanici_secim == bilgisayar_secim:
          print("berabere!")
     elif (kullanici_secim == "taş")and (bilgisayar_secim == "makas") or \
               (kullanici_secim == "kağit")and (bilgisayar_secim == "taş") or \
               (kullanici_secim == "makas")and (bilgisayar_secim == "kağit"):
          print("sen kazandın!")
          kullanici_skor += 1
     else:
          print("bilgisyar kazandı")
          bilgisayar_skor += 1
          print(f"skor: sen {kullanici_skor} - bilgisayar {bilgisayar_skor}")
          if kullanici_skor == 3:
               print ("\n tebrikler oyunu kazandınız")
          else:
               print("\n bilgisayar 3 skora ulaştı, oyun bitti.")