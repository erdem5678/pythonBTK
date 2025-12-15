# A = 572
# B = 600
# toplam = A + B
# ortalama = toplam / 2
# print(int(ortalama))
# carpim = ortalama * int(input("carpilacak sayi gir: "))
# print(carpim)
# print(type(A))
# print(A, B, sep='\n')
# A=B =   0
# print(A, B,toplam,sep='\n')

# print("\n----- degişkenleri birbirine aktarma----\n")

# A = 5
# B = 6
# C = A
# A = B
# B = C
# print(A)
# print(B)

# K = 'BTK'
# Y = 'AKADEMİ'
# K,Y = Y,K
# print(Y,K)

# print("\n----- degişken başlangic degerleri----\n")
# toplam = 0
# A = 35 
# B = 45
# toplam = A + B 
# print(toplam)

# toplam = 0
# for i in range(4):
#     sayi = int(input(f"{i+1}. sayi gir: "))
#     toplam += sayi
# print("toplam:", toplam)

# toplam = 0
# sayi1 = int(input("Sayi 1: "))
# sayi2 = int(input("Sayi 2: "))
# sayi3 = int(input("Sayi 3: "))
# sayi4 = int(input("Sayi 4: "))

# toplam = sayi1 + sayi2 + sayi3 + sayi4

# print("Toplam:", toplam)

# print("\n-----Operatörler----\n")
# A = 50
# B = 5
# print(A + B )
# print(A - B )
# print(A * B )
# print(A / B )
# print(A // B )
# print(A % B )
# print(A ** B )

# print("\n-----proje hesap makinesi----\n")

# A = int(input("Bir sayi giriniz: "))
# B = int(input("Bir sayi giriniz: "))
# print(A, '+', B, '=', A + B) # 9 + 15 = 24
# print(A, '-', B, '=', A - B) # 9 - 15 = -6
# print(A, '*', B, '=', A * B) # 9 * 15 = 135
# print(A, '/', B, '=', A / B) # 9 / 15 = 0.6 
# print(A, '//', B, '=', A // B) # 9 // 15 = 0
# print(A, '%', B, '=', A % B) # 9 // 15 = 0
# print(A, '**', B, '=', A ** B) # 9 ** 15 = 205891132094649

# print("\n-----işlem önceligi----\n")
# # # parantez içi ()
# # # üs alma **

# # # çarpma *
# # #  bölme  /
# # # mod %

# # # toplam +
# # # çıkarma -

# X = (2**2 + 3/5) / (3**2 - 2*5)
# print(X)

# i = 5
# j = 4
# i+=j+8
# print(i)

# print("\n-----veri tipi dönüştürme----\n")
# z =(int(9.6))
# print(z)
# x = float(5)
# print(x)
# y = str(4)
# print(y)

# print("\n----tekrar----\n")

# x,y,z = "BTK"
# print(type(x))

# i = 0
# j = 0
# i = j + i
# i += j # kısa fortmata yazıldı 

# B = 40
# C = str(B) + '5'
# print(C) # 405
# print(type(C)) # <class 'str'>

# print("\n----veri giriş komutu----\n")

# isim = input("isminizi: ")
# yas = int(input("yaşinizi girin: "))
# sinif = float(input("sinifinizi girin: "))

# print("isim:", isim)
# print("yas:", yas)
# print("sinif:", sinif)

# print(type(isim))
# print(type(yas))
# print(type(sinif))

# print("\n---- veri çikiş komutu ----\n")

# print("btk")

# print('b','t','k')

# print('b','t','k',sep=',')

# print('b','t','k',sep='*')

# x = 10
# print(x)

# a = 7
# print(a*x)
# print("btk"' '*3)

# print("yaşiniz: ", end=(''))
# yas=input()

# print("BTK \nAKADEMİ") # btk akaddemi yazsını  yan yana yazdrımaz \n ile alt alta yazdırır (\) == taksim 

# print("BTK \tAKADEMİ") # BTK  AKADEMİ olarak yaza \t yazının arasında bi tab kadar boşluk bırakır 

# print("\n---- format metodu ----\n")
# A = 10
# print("A={0}".format(A))

# print(f"A={A}")

# print('A='+ str(A))


# print("\n---- print() ile çizim ----\n")
# print(" ___\n/* *\\\n \./") 

# print("\n---- print()balik çizimi ----\n")
# print(" /\n<><\n \\")


# print("\n---- not ortalmasi hessaplama  ----\n")

# ort = 0
# Y1 = int(input("1.yazili= "))
# Y2 = int(input("2.yazili= "))
# ort = (Y1+Y2)/2
# print("ortalamaniz=",ort)


# print("\n----yaş hesaplama----\n")
# dt=int(input("Dogum tarihiniz: "))
# yas=2026-dt
# print("yasiniz=",yas)


# print("\n---- koşulu ifadeler  ----\n")

# x = int(input("sayi giriniz: "))
# y = int(input("sayi giriniz: "))
# if x == y:
#     print("eşittir")
# else:
#     print("eşit değildir")

# a = 25
# b = int(input("sayi tahmin edniz: "))
# if a == b:
#     print("tebriklr dogrubildiniz :) ")
# else:
#     print("tekrar deneyiniz :( ")

# print("\n---- koşulu ifadeler while True ile döngü   ----\n")
# a = 25
# while True:
#     b = int(input("sayi tahmin edniz: "))
#     if a == b:
#         print("tebriklr dogrubildiniz :) ")
#         break
#     else:
#         print("tekrar deneyiniz :( ")


# Not = float(input("Notunuzu giriniz: "))
# if Not >=50:
#     print("başarili")
# else:
#     print("başarisiz")

# print("\n---- kullaniciAdi şifre kontrolü ----\n")
# # data = {
# #     "admin": "1234"
# # }
# user = input("kullanici Adi: ")
# password = input("şifreyi giriniz: ")

# if user=='admin' and password == '1234': # if user in data and data[user] == password
#     print("Hoşgeldiniz...")
# else:
#     print("hatali giris")


# print("\n---- dönğüler(loop) ----\n")
# liste = ['ali','can','melisa','bariş']
# print(liste)

# liste2 = [1,2,3,4,5]
# print(liste2)

# liste3 = "Python"
# print(liste3)

# liste = ['ali','can','melisa','bariş']
# print(liste)
# print('ali'in liste)


# # print("\n----restoran(loop) ----\n")
# tabelNo = 0
# liste = {
#     "ali": 5,
#     "can": 7,
#     "melisa": 2,
#     "bariş": 10
# }
# liste2 =  ['bahar','zeynep']
# name = input("what is your name: ").lower()

# # if name == 'ali':
# #     tabelNo = 5
# # if name == 'can':
# #     tabelNo = 7
# # if name == 'melisa':
# #     tabelNo = 2
# # if name == 'bariş':
# #     tabelNo = 10

# if name in liste:
#     print(f"{tabelNo} You have a reservation at table number ")

# elif name is liste2:
#     print("Your reservation is not for tonight...")

# else:
#     print("you dont have a reservation")

#     add_user = input("would you like to make a reservation (yes/no): ").lower()
#     if add_user == 'yes':

#         new_name = input("Enter your name: ").lower()
#         new_table = int(input("Enter table number: "))

#     liste[new_name] = new_table
#     print(f"Reservation created for {new_name} at table {new_table}")

# print(liste)

# print("\n----range for while ----\n")
# for i  in range(1,10,2):
#     print(i)

# print("\n***********\n")
# for a in range (15,3,-4):
#     print(a)

# print("\n***********\n")
# for a in [0,1,2,3,4]:
#     print(a)

# for x in range(1,30):
#     if (x % 2 == 1):
#         print(x)
# print("\n******the square of a number*****\n")
# x = 1
# print("çikiş için sifira bas")
# while (x!= 0):
#     x = int(input("sayi giriniz : "))
#     print("sayinin karesi=",x*x)
# print("güle güle")

# print("\n******Break and continue*****\n")
# print("çikiş için 0 girin")
# while True:
#     x = int(input("sayi giriniz : " ))
#     print ("karesi=",x*x)
#     if (x == 0):
#         break # döngüden çık

# for a in range (0,101):
#     if (a % 7 == 0):
#         continue  # devam et
#     print(a)

# print("\n******(çok)multiple loops*****\n")
# for a in range (1,11):
#     for b in range (1,11):
#         print(a, "*" ,b, "=", a*b)
#     print("\n")

# numbers = [1,2,3,4,5]
# squared_evens = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
# print(squared_evens) #[4, 16, 36, 64, 100]


# print("\n******fonksiyonlar*****\n")
# # paremetre : these arer the value we want to be used within a function while that functions is running (bir fonksiyon içinde kullanılmasını isdedigimiz degerlerdir )
# print("can")

# A = 100
# print(A)

# input()
# def toplama (): 
#     print("addition is the process of adding two or more numbers")
#     print("for example" ,5, "+" ,7, "=", 13)
# toplama()

# print("\n****** for examaples*****\n")
# def selamlama (name):

#     print("Dear",name,"welccome to our restaurant")
# reservation = []
# max_kişi = 5
# while True:
#     if len(reservation) == (max_kişi):
#         print("The restaurant if full. We are not accepting any more guests.we apologize :( ")
#         break

#     Ad = input("Enter your name: ")
#     time = int(input("At what time do you want to come?: "))
#     selamlama(Ad)

#     # if (Ad == "exit"):
#         # break

#     reservation.append(Ad)
#     reservation.append(time)
#     print("Guest list:", reservation)


# def selamlama (name):
#     print("dear",name, "welcome to our restaurant")
# reservations = {}
# max_person = 5

# while True:
#     if len(reservations) == max_person:
#         print("The restaurant id full.no more guests.")
#         break

#     name = input("Enter your name: ")
#     if name in reservations:
#         print("This name already has a reservation.")
#         continue
    
#     time = int(input("At what time do you want to come: "))
#     if time in reservations:
#         print("This time already full. Choose another time.")
#         continue
#     reservations[name] = time
#     selamlama(name)
#     print("Guest list:", reservations)

# print("\n*************return fonksiyonu***************\n")

# # alan = uzunnluk * genişlik
# # cevre = (uzunluk + genişlik) * 2
# # alan = u * g

# def alan (u,g):
#     A = u * g 
#     return A
# def cevre (u ,g ):
#     C = 2 * (u + g)
#     return C

# u = int(input("uzunluk: "))
# g = int(input("genislik: "))
# print("alan:", alan(u,g))
# print("cevre:", cevre(u,g))


# print("\n*************global ve yerel(local) değişkenleri kullanma***************\n")

# def topla():
#     a = 5
#     b = 10
#     return (a + b)
# print(topla())
# # print(a)(error) bu degişkeni burda cagırmayız  çünkü bu dedişken  yerel (local) degişkendir 
# # bunu 2 şekilde çalışıta biliriz == print(a)

# print("\n****** 1 choice ******\n")
# def topla():
#     # a = 5
#     # b = 10
#     return (a + b)
# a = 5 # bu deişken artık global bir degişken oldu
# b = 10
# print(topla())
# print(a)
# print(b)

# print("\n****** 2 choice ******\n")
# # alt program
# def toplam():
#     global a # global a = 5 bu olmaz hatta alırız (invalid syntax) geçersiz sözdizimi
#     global b
#     a = 5
#     b = 10
#     return (a + b)
# # ana program 
# print(toplam())
# print(a)
# print(b)

# print("\n************** içerigi olmyan fonksiyon (psss)**************\n")
# # alt program
# def toplam():
#     global a 
#     global b
#     a = 5
#     b = 10
#     return (a + b)

# def carpma():
#     # pass
#     return (a * b)

# def bolem():
#     #pass
#     return (a / b)

# def cikarma():
#     #pass
#     return (a - b)
# # ana program 
# print(toplam())
# print(carpma())
# print(bolem())
# print(cikarma())
# print(a)
# print(b)


# print("\n************** fonksiyon kisatma (lambda)**************\n")

# # def dolar (TL):
# #     return (TL/41)

# dolar = lambda TL: TL/41

# TL = int(input("TL giriniz: "))
# print(TL,"Türk lirasi=",dolar(TL),"Dolar")

# print("\n❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️  Recursive (Özyinelemeli) Fonksiyon  ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ \n")
# #Kendi kendini çağıran fonksiyon
# #Bir problemi daha küçük parçalara böler
# #Base case (durdurma koşulu) olmalıdır, yoksa sonsuz döngü olur

# # alt perogram 
# def faktoriyel (n):
#     if n == 0:
#         return 1 # base case durdurma koşulu
#     else:
#         return n * faktoriyel(n-1)   
# # ana program 
# sayi = int(input("bir sayi giriniz: "))
# sonuc = faktoriyel(sayi)
# print(f"{sayi}! sayisinin sonucu= {sonuc} ")

# def ustel(a,b):
#     if b == 0 :
#         return 1 # base case ===> Eğer base case yoksa → sonsuz recursion → RecursionError
#     else: return a *ustel (a,b-1)

# a = int(input("taban girinizc: "))
# b = int (input("üssü giriniz: "))
# print(ustel(a,b))

# # pow()
# # Python’da pow() fonksiyonu üssü almak için kullanılır.
# print(pow(2, 3))  # 2^3 = 8
# print(pow(2, 3, 5))  # (2^3) % 5 = 8 % 5 = 3

# print("\n=========== Fonksiyon  tekarar =============\n")
 
# def selam():
#     isim = input("isim giriniz: ")
#     print(f"selam {isim} ❤️ ❤️ ❤️") # print("merhaba ")
# selam()

# # Kullanıcıdan sayıları alıp döndüren fonksiyon
# def hepsini_yaz():
#     a = int(input("sayi giriniz:"))
#     b = int(input("sayi giriniz: "))
#     return a,b  # İki sayıyı geri döndür

# ## İşlem fonksiyonları
# def toplam(a, b):
#     return a + b # print(a + b)

# def carpma(a, b):
#     return a * b # print(a * b)

# def cikarma(a, b):
#     return a - b # print(a - b)

# # Ana program
# a, b = hepsini_yaz()
# print("toplam:",toplam(a,b))
# print("carpim:",carpma(a,b))
# print("cikarma:",cikarma(a,b))


# elveda = lambda: print(" ❤️ ❤️ ❤️ görüşmek üzere ❤️ ❤️ ❤️ ")
# elveda()

# sayi = int(input("bir sayi giriniz: "))
# while sayi <= 100:
#     print(sayi, end=" ")
#     sayi += 1
    
print("\n=========== string işlemleri =============\n")
k = 'a'
l = "ali"
m = '''btk'''
z = 0

print(type(z))
print(type(k))
print(type(l))
print(type(m))
print(k,l,m,z)

print("\n============== index =================\n")

# Başlangıçta tek bir string tanımlıyoruz
isim = "BTK AKADEMİ"

# 1. KULLANIM:
# split() metodu ile string'i boşluklardan ayırıp liste haline getiriyoruz
parcalar = isim.split() 

# Listenin elemanlarına index ile erişiyoruz
print(parcalar[0])
print(parcalar[1])

# 2. KULLANIM:
# split() sonucunu doğrudan iki değişkene atıyoruz (tuple unpacking)
btk, akademi = isim.split()

# Değişkenleri tek tek yazdırıyoruz
print(btk)
print(akademi)

# String'in toplam karakter sayısını yazdırıyoruz (boşluk dahil)
print(len(isim))

print("\n============= index ==================\n")
Ad = "BTK AKADEMİ"# 0-1-2-3-4-5-6-7-8-9-10-11
print(len(isim))

print(Ad[7])
print(Ad[3])
print(Ad[-5])
print(Ad[0:11])

print("\n==============iki string birleştirme =================\n")
x = 'B'
y = 'T'
z = 'k'
l = x + y + z
print(l)
print(l[1])

a = "BTK"
b = "AKADEMİ"
c = a + " " + b
# bos = ' '
# c = a + bos + b
print(c)

print("\n============== string bölme =================\n")

s ='PYTHON'
print(s[:])
print(s[3:])
print(s[:3])
print(s[1:5])
print(s[1::2]) #YHN 1 indexi al 2 şer şekeilde atla 
print(s[::-1])

print("\n====================\n")
# string güncelleme

S = 'PYTHON'
S2 = S[:3] + 'T' + S[4:]
print(S2)

print("\n============== string  güncelleme / degiştirme  =================\n")

# 1 yöntem 
adres = 'Muğla - Milas'
adres2 = 'Bodrum'+ " " +  adres[:5]
print(adres2)

# 2 yöntem
Adres = adres.replace('Milas','Bodrum')
print(Adres)

print("\n============== string silme  =================\n")
# for x in range (5,0,-1):
#start = 5 → Sayaç 5’ten başlar
#stop = 0 → 0 dahil DEĞİL, 0’a gelince DURUR
#step = -1 → Her turda 1 azalt

yazi = 'PYTHON'
for x in range (5,0,-1):
    print(yazi[:-x])
print(yazi)

print("\n============== string for döngüsü ile index erişimi  =================\n")
# kelime ="btk-akademi"   #input("kelime giriniz: ")
# a = ''
# s = 0
# bulundu = False #bulundu diye kontrol bayrağı
# indis = int(input("index giriniz: "))
# for x in kelime:
#     if s == indis:
#         a = x
#         bulundu = True
#         break #Eleman bulununca break ile çıktık
#     s += 1
    
# if not bulundu:
#     print("bu indexte eleman yok")
# print(a)

print("\n============== string listeyeb  dömüştürme  =================\n")
# cumle = 'programi_cok_seviyorum'
# parca = cumle.split('_')

# cumle1 = "1234 5678 8990 4560 1247"
# parca1 = cumle1.split('_')

# print(parca)
# print(parca1)

print("\n============== string uzunlugu   =================\n")

# cumle = 'programi cok seviyorum ve çok zevkli'
# print(len(cumle)) # gives sentence length
# kelime = input("harf giriniz: ")

# sayim = cumle.count(kelime) # word counts
# print(sayim)

print("\n============== string karşilartirma   =================\n")
# kelime1 = input("kelime girinzi: ")
# kelime2 = input("kelime girinzi: ")

# karşilaştirma = kelime1 == kelime2
# # karşilaştirma = kelime1 is kelime2
# # karşilaştirma = kelime1 != kelime2
# print(karşilaştirma)


# kullanici = input("kullaniçi adinizi girin: ") # kullanici = admin
# sifre = input("şifre giriniz: ") # şifre = 1234

# veri = {
#     "kullanici": kullanici,
#     "sifre": sifre,
# } # dict ile yaptım 

# print("\n=====giriş paneline hoş geldiniz====\n")

# k_giris = input('kullanici adi giriniz: ')
# s_giris = input(' sifre giriniz: ')

# # if k_giris == kullanici and s_giris == şifre:
# if k_giris is veri["kullanici"] and s_giris is veri["sifre"]: # kullanicinin girmiş oldugu bilgileri veri (dict) cekip karşılaştırma (==,is,!=)
#     print('hoş geldiniz...')
#     print("kullanici adi:", veri["kullanici"])
#     print("şifre:", veri ["sifre"])
# else:
#     print("kullanici bilgisi veya şifre hattali")

print("\n===== string içerisndeki degişken yazdirma ====\n")

a = ' ile '
str = 'ali' + a + 'veli'
print('ali',a,'veli')
print(str)

string = 'aliveli'
str1 = string [:3] + a + string[3:]
print(str1)

string = 'ali{}veli'
str3 = string.format(a)
print(str3)

print("\n===== string ters çevirme ====\n")
