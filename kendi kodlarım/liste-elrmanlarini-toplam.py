# num1 = int(input("sayi gir 1: "))
# num2 = int(input("sayi gir 2: "))
# num3 = int(input("sayi gir 3: "))
# num4 = int(input("sayi gir 4: "))
# num5 = int(input("sayi gir 5: "))

# toplam=(num1 + num2 + num3 + num4 + num5)
# print(toplam)

liste = []
for i in range(5):
    sayi = int(input("Sayi gir: "))
    liste.append(sayi)
toplam = sum(liste)

print("Toplam =", toplam)
