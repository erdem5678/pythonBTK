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


print("\n----restoran(loop) ----\n")
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

print("\n----range for while ----\n")
# for i  in range(1,10,2):
#     print(i)

print("\n***********\n")
# for a in range (15,3,-4):
#     print(a)

print("\n***********\n")
# for a in [0,1,2,3,4]:
#     print(a)

# for x in range(1,30):
#     if (x % 2 == 1):
#         print(x)
print("\n******the square of a number*****\n")
# x = 1
# print("çikiş için sifira bas")
# while (x!= 0):
#     x = int(input("sayi giriniz : "))
#     print("sayinin karesi=",x*x)
# print("güle güle")

print("\n******Break and continue*****\n")
# print("çikiş için 0 girin")
# while True:
#     x = int(input("sayi giriniz : " ))
#     print ("karesi=",x*x)
#     if (x == 0):
#         break # döngüden çık

for a in range (0,101):
    if (a % 7 == 0):
        continue  # devam et
    print(a)

print("\n******(çok)multiple loops*****\n")
for a in range (1,11):
    for b in range (1,11):
        print(a, "*" ,b, "=", a*b)
    print("\n")
