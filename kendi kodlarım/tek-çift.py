tekler = []
ciftler =[]
for i in range (10):
    sayi = int(input("sayi gir: "))

    if sayi % 2 == 0:
        ciftler.append(sayi)
    else:
         tekler.append(sayi)
print("tekler: " , tekler)
print("ciftler: " , ciftler) 