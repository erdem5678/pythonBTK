def asal_mi(sayi):
    if sayi < 2 :
        return False
    for i in range(2, int(sayi ** 0.5)+1):
        if sayi % i == 0:
            return False
        return True
n = int(input("bir sayi giriniz: "))
print(f"{n} e kadar onaln asal sayilar: ")
for sayi in range (2,n + 1):
    if asal_mi(sayi):
     print(sayi, end=" ")