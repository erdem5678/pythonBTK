# 1- başlangıç ve bitiş degerlerini kullanıcıdan alınız ve bu  degerler arasındaki tüm çift sayıları yazdırınız 
baslangic = int(input("başlangic: "))
bitis = int(input("bitiş: "))
i = baslangic

while(i < bitis):
    if(i % 2 == 0):
        print(i)
    i += 1

# (1-100) arasındaki sayıların azalan şekilde yazdırınız 

i = 100
while(i > 0):
    print(i)
    i -= 1

# kullanıcıdan  alacagımız 5 sayıyı ekara sırala bir şekilde yazdırın 

i = 0
sayilar =[]

while (i < 5):
    sayi = int(input("sayi: "))
    sayilar.append(sayi)
    i += 1

sayilar.sort()

print(sayilar)

# klavyeden girişi istene username bilgisi için boşluk girildigi süürece tekrar username girişi isteyiniz


username = " "


while not username:
    username = input("kullanici adi: ")

print("girilen username: " + username)