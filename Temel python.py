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
    
# print("\n=========== string işlemleri =============\n")
# k = 'a'
# l = "ali"
# m = '''btk'''
# z = 0

# print(type(z))
# print(type(k))
# print(type(l))
# print(type(m))
# print(k,l,m,z)

# print("\n============== index =================\n")

# # Başlangıçta tek bir string tanımlıyoruz
# isim = "BTK AKADEMİ"

# # 1. KULLANIM:
# # split() metodu ile string'i boşluklardan ayırıp liste haline getiriyoruz
# parcalar = isim.split() 

# # Listenin elemanlarına index ile erişiyoruz
# print(parcalar[0])
# print(parcalar[1])

# # 2. KULLANIM:
# # split() sonucunu doğrudan iki değişkene atıyoruz (tuple unpacking)
# btk, akademi = isim.split()

# # Değişkenleri tek tek yazdırıyoruz
# print(btk)
# print(akademi)

# # String'in toplam karakter sayısını yazdırıyoruz (boşluk dahil)
# print(len(isim))

# print("\n============= index ==================\n")
# Ad = "BTK AKADEMİ"# 0-1-2-3-4-5-6-7-8-9-10-11
# print(len(isim))

# print(Ad[7])
# print(Ad[3])
# print(Ad[-5])
# print(Ad[0:11])

# print("\n==============iki string birleştirme =================\n")
# x = 'B'
# y = 'T'
# z = 'k'
# l = x + y + z
# print(l)
# print(l[1])

# a = "BTK"
# b = "AKADEMİ"
# c = a + " " + b
# # bos = ' '
# # c = a + bos + b
# print(c)

# print("\n============== string bölme =================\n")

# s ='PYTHON'
# print(s[:])
# print(s[3:])
# print(s[:3])
# print(s[1:5])
# print(s[1::2]) #YHN 1 indexi al 2 şer şekeilde atla 
# print(s[::-1])

# print("\n====================\n")
# # string güncelleme

# S = 'PYTHON'
# S2 = S[:3] + 'T' + S[4:]
# print(S2)

# print("\n============== string  güncelleme / degiştirme  =================\n")

# # 1 yöntem 
# adres = 'Muğla - Milas'
# adres2 = 'Bodrum'+ " " +  adres[:5]
# print(adres2)

# # 2 yöntem
# Adres = adres.replace('Milas','Bodrum')
# print(Adres)

# print("\n============== string silme  =================\n")
# # for x in range (5,0,-1):
# #start = 5 → Sayaç 5’ten başlar
# #stop = 0 → 0 dahil DEĞİL, 0’a gelince DURUR
# #step = -1 → Her turda 1 azalt

# yazi = 'PYTHON'
# for x in range (5,0,-1):
#     print(yazi[:-x])
# print(yazi)

# print("\n============== string for döngüsü ile index erişimi  =================\n")
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

# print("\n============== string listeyeb  dömüştürme  =================\n")
# cumle = 'programi_cok_seviyorum'
# parca = cumle.split('_')

# cumle1 = "1234 5678 8990 4560 1247"
# parca1 = cumle1.split('_')

# print(parca)
# print(parca1)

# print("\n============== string uzunlugu   =================\n")

# cumle = 'programi cok seviyorum ve çok zevkli'
# print(len(cumle)) # gives sentence length
# kelime = input("harf giriniz: ")

# sayim = cumle.count(kelime) # word counts
# print(sayim)

# print("\n============== string karşilartirma   =================\n")
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

# print("\n===== string içerisndeki degişken yazdirma ====\n")

# a = ' ile '
# str = 'ali' + a + 'veli'
# print('ali',a,'veli')
# print(str)

# string = 'aliveli'
# str1 = string [:3] + a + string[3:]
# print(str1)

# string = 'ali{}veli'
# str3 = string.format(a)
# print(str3)

# print("\n===== string ters çevirme   ====\n")

# srt1 = 'btk'
# ters= srt1[::-1]
# ters1 = ''.join(reversed(srt1))
# ters2 = 'k'.join(reversed(srt1))
# ters3 = '.'.join(reversed(srt1))
# print(ters1)
# print(ters2)
# print(ters3)
# print(ters)

# print("\n===== string büyük küçük harfe çevirme   ====\n")
# küçük = 'bariş ERDEM'
# k = küçük.lower()
# b = küçük.upper()
# k_b = küçük.swapcase()
# başharf = küçük.capitalize()


# print(başharf)
# print(k_b)
# print(b)
# print(k)

# print("\n=====  bir string içindeki başka string nasil arariz   ====\n")
# # in - not in komutları ile denetim yaparız 
# eşitir1 = 'AT' in 'talat'
# eşitir2 = 'at' in 'talat'
# arama = 'as' not in 'selam'
# print(eşitir1)
# print(eşitir2)
# print(arama)

# print("\n====== örnek ======\n")
# veri = []
# kişi = input("kişi giriniz: ")
# str1 = input("isim girinzi...: ")

# if kişi in str1:
#     print("var")
# else:
#     print("yok")

# veri.append(kişi)
# print(veri)

# print("\n====== örnek ======\n")

# kelime = input("kelime giriniz: ")
# print(kelime,'nin tersi', kelime [::-1], 'dir')
# if kelime == kelime[::-1]:
#     print(kelime,'bir palindromdur')
# else:
#     print(kelime,'bir palindrom degildir')


print("\n====== diziler ve listeler  ======\n") 
# s = input("kelime giriniz: ")
# print(len(s))  


print("\n===== listeler  ======\n") 
liste = ['ali',5,'a'] # eger cift tırnak kullnaırsn hatta alırsın dikkat ("")
isim_liste = ['ali','veli','can']
char_liste = ['*','-','?','/','u']
sayi_liste =[1,2,3,4,5,6,7,8,9]
bos_liste = [] 
karisik_liste = ['btk',10,'a',5.6]


print("\n====== listede elemsan erişimi   ======\n") 

liste = ['ali','can',1234567,'bariş']
liste1 =liste [2]
liste2= liste [-1]
print(liste1)
print(liste2)


print("\n====== listedeki bir elemanin indeksi numarini bilmiyorsak nasil buluruz    ======\n") 
liste = [1,2,3,4,'a','2','btk']

numra1 = liste.index(2)
numra = liste.index('2')
print("liste içindeki numrali index=",numra1)
print(numra)

print("\n====== listede dilimleme işlemi ======\n")

liste = [1,2,3,4,5,6,7,8,9]
l = liste [2:] # listeden sag tarfa yazraasak  2.indexten sona kadar al
l1 = liste [:5] # listeden  sol tarfa yazrasak baştan 5.indekse kadar al
l2 = liste [::-1] # listeyi ters çevirir
l3 = liste[::2] # listeyi baştan sona 2 şer 2 şer atlayarak alır
l4 = liste [::-2] # listeyi sondan başa 2 şer 2 şer atlayarak alır
print(l)
print(l1)
print(l2)
print(l3) 
print(l4)


print("\n====== listeye yeni eleman ekleme ======\n")

liste = [1,2,3,4,5,6,7,8,9]
a = liste.append(10)# listeye sonuna 10 ekler
b = liste.insert(0,0) # listeye 0.indekse 0 ekler
c = liste.insert(5,'btk')# listeye 5.indekse btk ekler
print(liste)

print("\n====== listeden eleman eklme örnek  ======\n")

# sayi_liste = []

# for i in range (0,5):
#     sayi = int(input("sayi giriniz: "))
#     sayi_liste.append(sayi)
# print("tüm sayilarin toplami:", sum(sayi_liste))

# for i in range (0,5):
#     print("sayi_liste[",i,"]", "=", sayi_liste[i]) # indeks numarası ile liste elemanlarını yazdırma
# print("liste uzunlugu:", len(sayi_liste))
# print(sayi_liste)

print("\n====== listenin eleman uzunlugunu ögrenme  ======\n")

liste = ['ali','can','melisa','bariş',3,4,5,6,6,5,6,3,3,7]
uzunluk = liste.__len__() # uzunluk = len(liste) # listenin eleman uzunluğunu verir
ayni_eleman = liste.count(6) # liste içinde 6 elemanının kaç defa geçtiğini sayar

print("listenin eleman uzunlugu", "=",uzunluk)
print("kaçtane ayni elemandan var","=",ayni_eleman)

print("\n====== 2 listeyi birleştirme   ======\n")

l1 =[1,2,3,4]
l2 = [5,6,7,8]
l3 = l1 + l2 # liste birleştirme
print(l3)

birleştieme = l1.extend(l2) # liste birleştirme 2.yöntem
ekleme = l2.extend(l1) # [5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8] 
print(l1)
print(l2)

print("\n==== listeyi ders cevirme  ======\n")

liste = [1,2,3,4,5,6,7,8,9]
ters = liste[::-1]
print(ters)
ters1 = liste.reverse() # listeyi ters çevirir
print(liste)

print("\n==== listenin en büyük en kücük elemani ögrenem   ======\n")

liste = [2,30,40,60,300,6,1,8,100]
en_büyük = max(liste)
en_küçük = min(liste)
print(liste)
print("listedeki en büyük sayi=",en_büyük)
print("listedeki en küçük sayi=",en_küçük)

# uygulama

# boş = []
# topla = 0
# for i in range (0,5):
#     sayi = int(input("sayi giriniz: "))
#     boş.append(sayi)
#     topla += sayi

# print(boş)
# print("en büyük sayi=",max(boş))
# print("en küçük sayi=",min(boş))
# print("en küçük ve en büyük sayilarinin toplami=",min(boş)+max(boş))
# print("aritmatik ortalamasi=",topla/5)

print("\n==== string listeye dönüştürme   ======\n")
kelime = 'BTKAKADEMİ'
liste = []
liste=list(kelime)
konum = liste.count('T') # liste içinde t harfinin kaç defa geçtiğini sayar
indeks =liste.index('A') # liste içinde a harfinin ilk geçtiği index numarasını verir


print(indeks)
print(konum)
print(liste)
print(type(liste))

print("\n==== listeden eleman silme    ======\n")
kelime = 'BTKAKADEMİ'
liste = []
liste=list(kelime)# kelimeyi listeye dönüştürdük
liste.remove('A') # listeden A harfini siler
liste.remove('A') # listeden A harfini siler
liste.pop(3) # listeden 3.indeksteki elemanı siler
liste.clear() # listenin tüm elemanlarını siler
print(liste)

print("\n==== listede arama yapma ======\n")
# L = [1,2,3,4,5,6,7,8,9]
# deger = 3 in L
# print(deger)

# liste = [1,2,3,4,5,6,7,8,]
# aranan = int(input("aranan sayi giriniz: "))
# if aranan in liste:
#     indis = liste.index(aranan)
#     print("Aranan",indis,"'ci indis degerinde bulundu")
# else:
#     print("Arana indis  listede yok")
# print(aranan)
 

print("\n==== listede eleman siralama ======\n")
liste = [5,2,8,1,4,7,6,3]
liste.sort() # listeyi küçükten büyüge sıralar 
L= liste[::-1] # listeyi büyükten küçüge sıralar
print(liste)
print(L)
# uygulama

# sayi_listesi=[]
# for i in range(0,6):# 6 sayi girişi
#     sayi = int(input("ssayi giriniz: "))
#     sayi_listesi.append(sayi)# listeye ekleme
# sayi_listesi.sort()# # listeyi küçükten büyüge sıralar
# print(sayi_listesi)
# print('listenin medyani degeri=',(sayi_listesi[2] + sayi_listesi[3]) / 2)# ortalama bulma
# index:  0   1   2   3   4    5
# değer: 23  45  60  60  89  700

print("\n==== enumerate() fonksiyonu kullnaimi  ======\n")

haftanin_gunleri = ['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar']
for i, deger in enumerate(haftanin_gunleri):
    print(str(i+1)+".gün:"+deger) # i indeksi deger ise haftanin_gunleri listesindeki elemanları temsil eder
# print(f"{i}. gün: {deger}")


print("\n==== listelerden yigin oluşturma   ======\n")

# stack = [] # boş yığın oluşturma
# # yığına eleman ekleme (push),(appned)
stack = []
stack.append(3)# yığına eleman ekleme (push)
stack.append(4)
stack.append(5)
print("yiğindaki elemanlar:",stack)
stack.pop() # yığından eleman çıkarma (pop)
print("yiğindaki elemanlar:",stack)


print("\n==== lisde de kuyruk oluşturma (queue)  ======\n")
# queue = [] # boş kuyruk oluşturma
queue = []
queue.append(1) # kuyruğa eleman ekleme (enqueue)
queue.append(12) # kuyruğa eleman ekleme (enqueue)
queue.append(134) # kuyruğa eleman ekleme (enqueue)
queue.append(10) # kuyruğa eleman ekleme (enqueue)
queue.append(25)# kuyruğa eleman ekleme (enqueue)
print(queue)
queue.pop(0) # kuyruktan eleman çıkarma (dequeue)
print(queue)

# uygulama

# liste = []
# while True:
#     isim = input("isim  giriniz: ")
#     liste.append(isim) # listeye eleman ekleme

#     if isim == 'next': # 
#         liste.pop() #Listenin sonuna eklenen 'next' kelimesini siler
#         print(liste.pop(0)) # listeden eleman çıkarma

#     if isim =='bitti':
#         liste.pop() #Listenin sonuna eklenen 'bitti' kelimesini siler
#         break
# print("listede olan kişiler:",liste)

print("\n==== bölüm sonu uygulama   ======\n")
# L = []
# while True:
#     TC = (input("TC kimlik numaranizi giriniz: "))
#     if TC in L:
#         i = L.index(TC)
#         print("Muane sirasi:",i+1)

#     if TC == 'stop':
#             break
    
#     elif TC==0: # kuyruktan eleman çıkarma (dequeue)
#         print(L[0],'TC numrali hasta dokturun yaninda ')
#         L.pop(0)

#     else:
#         L.append(TC)
#         print(TC,"TC numrali hastanin kaydi yapildi")
# print(len(L),"tane hasta sirada bekliyor")
# print(L)

# 2 uygulama
hasta_kayitlari = [] # Hastaların tutulacağı boş bir liste (kuyruk) oluşturur

while True:
     # Kullanıcıdan veri girişi alırız (input her zaman metin/string döner)
     TC = input("TC kimlik numaranizi giriniz (cagirmak için 0, çikiş için stop yaziniz): ")

     # ==== ÇIKIŞ KONTROLÜ: Kullanıcı 'stop' yazarsa break komutuyla döngüden çıkar =====
     if TC == 'stop':
        break
     


     # ===== ÇAĞIRMA İŞLEMİ: Eğer kullanıcı string olarak "0" girerse bu blok çalışır =====
     if TC == "0":
        # Listenin boş olup olmadığını kontrol eder (Boş listeyi pop etmek hata verir)
        if len(hasta_kayitlari) > 0 : 
                # Listenin 0. indeksindeki (en başındaki) veriyi ekrana yazdırır
                print(hasta_kayitlari[0],'TC numarali hasta dokturun yaninda ')
                # pop(0) komutu listenin ilk elemanını siler (FIFO - İlk giren ilk çıkar mantığı)
                hasta_kayitlari.pop(0) 
        else:
            # Liste boşsa hata vermemesi için bu uyarıyı döner
            print("bekleyen hasta yok")


     # ==== SORGULAMA: Girilen TC zaten listede varsa index() ile konumunu bulur ====
     elif TC in hasta_kayitlari:
          # index() elemanın sırasını verir. Programlamada sayma 0'dan başladığı için +1 ekleriz.
          i = hasta_kayitlari.index(TC) 
          print("zaten kayitlisizsiniz muane sirasi:",i+1) 



     # ===== KAYIT EKLEME: Yukarıdaki şartlar sağlanmazsa (yeni bir TC girilirse) burası çalışır =====
     else:
          # append() metodu girilen yeni TC'yi listenin sonuna ekler
          hasta_kayitlari.append(TC) 
          # len() listenin o anki eleman sayısını vererek hastaya kaçıncı sırada olduğunu söyler
          print(TC,"TC numrali hastanin kaydi yapildi") 


# Döngü bittiğinde güncel listeyi ekrana basar
print("güncel liste:", hasta_kayitlari)