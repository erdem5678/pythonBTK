A = 572
B = 600
toplam = A + B
ortalama = toplam / 2
print(int(ortalama))
carpim = ortalama * int(input("carpilacak sayi gir: "))
print(carpim)
print(type(A))
print(A, B, sep='\n')
A=B =   0
print(A, B,toplam,sep='\n')

print("\n----- degişkenleri birbirine aktarma----\n")

A = 5
B = 6
C = A
A = B
B = C
print(A)
print(B)

K = 'BTK'
Y = 'AKADEMİ'
K,Y = Y,K
print(Y,K)

print("\n----- degişken başlangic degerleri----\n")
toplam = 0
A = 35 
B = 45
toplam = A + B 
print(toplam)

toplam = 0
for i in range(4):
    sayi = int(input(f"{i+1}. sayi gir: "))
    toplam += sayi
print("toplam:", toplam)

toplam = 0
sayi1 = int(input("Sayi 1: "))
sayi2 = int(input("Sayi 2: "))
sayi3 = int(input("Sayi 3: "))
sayi4 = int(input("Sayi 4: "))

toplam = sayi1 + sayi2 + sayi3 + sayi4

print("Toplam:", toplam)

print("\n-----Operatörler----\n")
A = 50
B = 5
print(A + B )
print(A - B )
print(A * B )
print(A / B )
print(A // B )
print(A % B )
print(A ** B )

print("\n-----proje hesap makinesi----\n")

A = int(input("Bir sayi giriniz: "))
B = int(input("Bir sayi giriniz: "))
print(A, '+', B, '=', A + B) # 9 + 15 = 24
print(A, '-', B, '=', A - B) # 9 - 15 = -6
print(A, '*', B, '=', A * B) # 9 * 15 = 135
print(A, '/', B, '=', A / B) # 9 / 15 = 0.6 
print(A, '//', B, '=', A // B) # 9 // 15 = 0
print(A, '%', B, '=', A % B) # 9 // 15 = 0
print(A, '**', B, '=', A ** B) # 9 ** 15 = 205891132094649

print("\n-----işlem önceligi----\n")
# parantez içi ()
# üs alma **

# çarpma *
#  bölme  /
# mod %

# toplam +
# çıkarma -

X = (2**2 + 3/5) / (3**2 - 2*5)
print(X)

i = 5
j = 4
i+=j+8
print(i)

print("\n-----veri tipi dönüştürme----\n")
z =(int(9.6))
print(z)
x = float(5)
print(x)
y = str(4)
print(y)

print("\n----tekrar----\n")

x,y,z = "BTK"
print(type(x))

i = 0
j = 0
i = j + i
i += j # kısa fortmata yazıldı 

B = 40
C = str(B) + '5'
print(C) # 405
print(type(C)) # <class 'str'>

print("\n----veri giriş komutu----\n")

isim = input("isminizi: ")
yas = int(input("yaşinizi girin: "))
sinif = float(input("sinifinizi girin: "))

print("isim:", isim)
print("yas:", yas)
print("sinif:", sinif)

print(type(isim))
print(type(yas))
print(type(sinif))

print("\n---- veri çikiş komutu ----\n")

print("btk")

print('b','t','k')

print('b','t','k',sep=',')

print('b','t','k',sep='*')

x = 10
print(x)

a = 7
print(a*x)
print("btk"' '*3)

print("yaşiniz: ", end=(''))
yas=input()

print("BTK \nAKADEMİ") # btk akaddemi yazsını  yan yana yazdrımaz \n ile alt alta yazdırır (\) == taksim 

print("BTK \tAKADEMİ") # BTK  AKADEMİ olarak yaza \t yazının arasında bi tab kadar boşluk bırakır 

print("\n---- format metodu ----\n")
A = 10
print("A={0}".format(A))

print(f"A={A}")

print('A='+ str(A))


print("\n---- print() ile çizim ----\n")
print(" ___\n/* *\\\n \./") 

print("\n---- print()balik çizimi ----\n")
print(" /\n<><\n \\")


print("\n---- not ortalmasi hessaplama  ----\n")

ort = 0
Y1 = int(input("1.yazili= "))
Y2 = int(input("2.yazili= "))
ort = (Y1+Y2)/2
print("ortalamaniz=",ort)


print("\n----yaş hesaplama----\n")
dt=int(input("Dogum tarihiniz: "))
yas=2026-dt
print("yasiniz=",yas)