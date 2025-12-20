def asal_mi(sayi):
    if sayi < 2 :
        return False

## Kareköküne kadar olan sayılara bölünmüyorsa asaldır
    for i in range(2, int(sayi ** 0.5)+1): # kareköküne kadar kontrol et
        if sayi % i == 0:
            return False
        return True

# Ana Program
n = int(input("bir sayi giriniz: "))
print(f"{n} e kadar onaln asal sayilar: ")

# Asal sayılar olarak kontrol et ve yazdır
for sayi in range (2,n + 1):
    if asal_mi(sayi):
     print(sayi, end=" ")