# 1- faktöriyel fonksiyonu oluşturnuz ve fonksiyona gelen deger için hata mesaji verin.

def faktoriyel(x):
    x = int (x)
    if (x < 0) :
        raise ValueError("negatif deger olamaz")
    
    sonuc = 1

    for i in range(1, x + 1):
        sonuc *= i

    return sonuc
    
for i in [3, 6, 7, '2a',-1, -7 , 9]:
    try:
        x = faktoriyel(i)
    except ValueError as ex:
        print(ex)
        continue
    else:
        print(x)


# 2- girilen parola içindeki türkce karakterleeri hatsı veriniz.

def parolakontrol(parola):
    turkce_karakter = "şçğüöıİ"

    for i in parola:
        if i in turkce_karakter: 
            raise TypeError("parola türkce karakter icermemeli")
        
    print("gecerli parola")

parola = input("parola: ")

try:
    parolakontrol(parola) # parola kontrol 
except TypeError as ex:
    print(ex)
        